from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split

from common_func import clean_text

# Sample data (texts and their urgency labels)
def init_severity_model():
    texts = ["urgent request please respond", "normal inquiry", "critical system failure"]
    labels = ["urgent", "normal", "critical"]

# Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.2, random_state=42)

# Create a model pipeline
    model = make_pipeline(TfidfVectorizer(), MultinomialNB())

# Train the model
    model.fit(X_train, y_train)
    return model

# new code


# import torch
# from torch.utils.data import DataLoader, TensorDataset, random_split
# from transformers import BertTokenizer, BertForSequenceClassification, AdamW
# from torch.nn import CrossEntropyLoss
# from common_func import clean_text

# # Define the label map
# urgency_map = {
#     "low": 0,
#     "normal": 1,
#     "med": 2,
#     "high": 3,
#     "urgent": 4,
#     "critical" : 5
# }

# texts = [
#     "urgent system failure, please respond immediately",
#     "routine checkup required, no immediate action needed",
#     "high priority: server downtime reported",
#     "customer inquiry, please respond within standard timeframes",
#     "critical performance issue affecting multiple users",
#     "normal maintenance scheduled for next week",
#     "urgent: security breach detected in the database",
#     "feedback on services, not urgent",
#     "software update required, medium priority",
#     "low priority: update documentation",
#     "server performance optimization, high importance",
#     "general question about account settings",
#     "urgent assistance required for system outage",
#     "non-critical bug found in the application",
#     "high-priority customer complaint, immediate attention needed",
#     "reminder: team meeting tomorrow",
#     "urgent: compliance issue needs to be addressed",
#     "normal query regarding billing",
#     "critical: data loss incident reported",
#     "feedback request on recent update, not urgent"
# ]

# labels = [
#     "urgent",  # urgent system failure
#     "low",     # routine checkup
#     "high",    # high priority server downtime
#     "normal",  # customer inquiry
#     "critical",# critical performance issue
#     "normal",  # normal maintenance
#     "urgent",  # urgent security breach
#     "low",     # feedback, not urgent
#     "med",     # software update, medium priority
#     "low",     # low priority documentation update
#     "high",    # high importance server optimization
#     "normal",  # general account question
#     "urgent",  # urgent system outage
#     "low",     # non-critical bug
#     "high",    # high-priority customer complaint
#     "low",     # meeting reminder
#     "urgent",  # urgent compliance issue
#     "normal",  # normal billing query
#     "critical",# critical data loss
#     "low"      # feedback request, not urgent
# ]

# # Convert labels to numerical format
# labels = [urgency_map[label] for label in labels]

# # Tokenize the texts
# tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
# tokenized_texts = tokenizer(texts, padding=True, truncation=True, return_tensors="pt")

# # Prepare dataset
# input_ids = tokenized_texts['input_ids']
# attention_mask = tokenized_texts['attention_mask']
# labels = torch.tensor(labels)
# dataset = TensorDataset(input_ids, attention_mask, labels)

# # Split the dataset
# train_size = int(0.8 * len(dataset))
# val_size = len(dataset) - train_size
# train_dataset, val_dataset = random_split(dataset, [train_size, val_size])

# # Load the pre-trained BERT model
# model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=len(urgency_map))

# # Initialize the optimizer
# optimizer = AdamW(model.parameters(), lr=1e-5)
# criterion = CrossEntropyLoss()

# # Training loop
# model.train()
# for epoch in range(3):  # Example: 3 training epochs
#     for batch in DataLoader(train_dataset, batch_size=2, shuffle=True):
#         input_ids, attention_mask, batch_labels = batch
#         model.zero_grad()
#         outputs = model(input_ids, attention_mask=attention_mask)
#         loss = criterion(outputs.logits, batch_labels)
#         loss.backward()
#         optimizer.step()

#     print(f"Epoch {epoch} complete, Loss: {loss.item()}")

# # Prediction function
# def init_severity_model():
#     # Clean and tokenize the complaint
#     # cleaned_complaint = clean_text(complaint)
#     inputs = tokenizer(cleaned_complaint, padding=True, truncation=True, return_tensors="pt")

#     # Predict with the model
#     model.eval()
#     with torch.no_grad():
#         outputs = model(**inputs)
    
#     logits = outputs.logits
#     predicted_urgency_index = torch.argmax(logits, dim=1).item()

#     # Convert index to urgency label
#     predicted_urgency = [k for k, v in urgency_map.items() if v == predicted_urgency_index][0]
#     return predicted_urgency

# # Test the model with a new complaint
# # new_complaint_text = "telecommunication mobile related activationdeactivationfault sim card mobile number x4x7x2x3x2 service provider bharat sanchar nigam limited corporate office respected sir reference issue faced would like lodge complaint bsnl kalyani exchange wherein issued duplicate sim mother39s name aruna chakraborty without permission knowledge hence would like register complaint would like necessary action taken bsnl kalyani exchange carried transaction issuance sim card 17th dec 2022 confirmed bsnl customer care said date following number x4x7x2x3x2 would also like inform taking legal action mistake issuing sim without verifying detail caused financial fraud saving account 19th dec 2022 amounting rs1374000 also went kalyani bsnl exchange 22nd dec shared document duplicate sim issued looking could clearly see document fake verified bsnl official also attaching fake document received exchange used issue sim card along original document regard anita rao chakraborty alternate contact x0x1x4x0x7 x0x3x6x4x4 x2x2x2x4x5"
# # cleaned_text = clean_text(new_complaint_text)
# # # predicted_urgency = predict_urgency(cleaned_text)
# # print(f"The text '{cleaned_text}' is predicted as: {predicted_urgency}")
