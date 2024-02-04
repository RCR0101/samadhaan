import torch
from torch.utils.data import DataLoader, Dataset
from transformers import BertTokenizer, BertForSequenceClassification, AdamW
import pandas as pd

# Assuming you have a dataset in CSV format
class TextDataset(Dataset):
    def __init__(self, filename, tokenizer, max_len=128):
        self.dataframe = pd.read_csv(filename)
        self.tokenizer = tokenizer
        self.max_len = max_len

    def __len__(self):
        return len(self.dataframe)

    def __getitem__(self, idx):
        text = self.dataframe.iloc[idx, 0]  # Assuming text is in the first column
        label = self.dataframe.iloc[idx, 1] # Assuming label is in the second column
        encoding = self.tokenizer.encode_plus(
            text,
            add_special_tokens=True,
            max_length=self.max_len,
            truncation=True,
            padding='max_length',
            return_attention_mask=True,
            return_tensors='pt',
        )
        return {
            'text': text,
            'input_ids': encoding['input_ids'].flatten(),
            'attention_mask': encoding['attention_mask'].flatten(),
            'labels': torch.tensor(label, dtype=torch.long)
        }

def custom_collate_fn(batch):
    batch_input_ids = [item['input_ids'] for item in batch]
    batch_attention_mask = [item['attention_mask'] for item in batch]
    batch_labels = [item['labels'] for item in batch]

    input_ids = torch.nn.utils.rnn.pad_sequence(batch_input_ids, batch_first=True, padding_value=0)
    attention_mask = torch.nn.utils.rnn.pad_sequence(batch_attention_mask, batch_first=True, padding_value=0)
    labels = torch.tensor(batch_labels)

    return {'input_ids': input_ids, 'attention_mask': attention_mask, 'labels': labels}

def train(model, data_loader, optimizer, device, num_epochs=3):
    model = model.train()

    for epoch in range(num_epochs):
        for batch in data_loader:
            input_ids = batch['input_ids'].to(device)
            attention_mask = batch['attention_mask'].to(device)
            labels = batch['labels'].to(device)

            outputs = model(input_ids, attention_mask=attention_mask, labels=labels)
            loss = outputs.loss

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

def main():
    # Use MPS device if available, else CPU
    DEVICE = 'mps' if torch.backends.mps.is_available() else 'cpu'
    print(f"Using device: {DEVICE}")

    # from transformers import BertTokenizer, BertForSequenceClassification
    # from torch.utils.data import DataLoader
    # from your_module import TextDataset, custom_collate_fn, train  # Ensure you have these functions/modules

    tokenizer = BertTokenizer.from_pretrained('bert-base-multilingual-cased')
    model = BertForSequenceClassification.from_pretrained('bert-base-multilingual-cased', num_labels=3841).to(DEVICE)

    train_dataset = TextDataset('post_process_csv/text_label_dept.csv', tokenizer)
    train_loader = DataLoader(train_dataset, batch_size=16, shuffle=True, collate_fn=custom_collate_fn)

    optimizer = torch.optim.AdamW(model.parameters(), lr=2e-5)

    train(model, train_loader, optimizer, DEVICE)

    # Save the model and tokenizer
    model.save_pretrained('./models/predict_dept')
    tokenizer.save_pretrained('./models/predict_dept')

def old_main():
    DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'

    tokenizer = BertTokenizer.from_pretrained('bert-base-multilingual-cased')
    model = BertForSequenceClassification.from_pretrained('bert-base-multilingual-cased', num_labels=3841).to(DEVICE)

    train_dataset = TextDataset(f'post_process_csv/text_label_dept.csv', tokenizer)
    # train_loader = DataLoader(train_dataset, batch_size=16, shuffle=True)
    train_loader = DataLoader(train_dataset, batch_size=16, shuffle=True, collate_fn=custom_collate_fn)

    optimizer = torch.optim.AdamW(model.parameters(), lr=2e-5)

    train(model, train_loader, optimizer, DEVICE)

    # Save the model and tokenizer
    model.save_pretrained('./models/predict_dept')
    tokenizer.save_pretrained('./models/predict_dept')

if __name__ == "__main__":
    main()
