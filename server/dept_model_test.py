import torch
from transformers import BertTokenizer, BertForSequenceClassification

def load_model_and_tokenizer(model_path):
    tokenizer = BertTokenizer.from_pretrained(model_path)
    model = BertForSequenceClassification.from_pretrained(model_path)
    return tokenizer, model

def classify_text(text, tokenizer, model, device='cpu'):
    inputs = ""
    inputs = tokenizer.encode_plus(
        text,
        add_special_tokens=True,
        max_length=512,
        # truncation=True,
        return_token_type_ids=False,
        padding='max_length',
        return_attention_mask=True,
        return_tensors='pt',
    )
    input_ids = ""
    input_ids = inputs['input_ids'].to(device)
    attention_mask = inputs['attention_mask'].to(device)

    model.eval()
    with torch.no_grad():
        outputs = model(input_ids, attention_mask=attention_mask)

    logits = outputs.logits
    probabilities = torch.nn.functional.softmax(logits, dim=1)
    print(probabilities.shape)
    predicted_class = torch.argmax(probabilities, dim=1).item()
    return predicted_class, probabilities[0][predicted_class].item()

def main():
    # Load the model and tokenizer
    model_path = './models/predict_dept'
    tokenizer, model = load_model_and_tokenizer(model_path)

    # Classify text
    text_to_classify = "labour employment others epfo name address establishment adecco india pvt ltd uan x0x2x2x1x5x1 pf code pf account xyxoxx4x7xx8x4x6 ppo provided scheme certificate number provided pf office regional office bommasandra would like tell working addeco india pvt ltd said company trust although company closed 2018 company paid full pf pension money left since pension money deposited pf office could withdraw kyced time company completely closed idea company established bangalore gave u address two three time paper couriour get response pmo grievance regarding gave mobile asked call receiving call first pmo grievance xoxbxxx0x2x9x6x7 request kindly consider complaint withdraw pension"
    # text_to_classify = "railway railway board miscellaneous railway board zone psu pu office railway board railway board railway board sdah er location madhyamgram informing temporary railway line crossing near madhyamgram station bt end bad condition stone side line moved far enough cause great danger yraincommon people train passenger time please look matter although said place fixed done thanking truly bhaskar mitra 112023"
    # text_to_classify = "central board direct tax income tax technical issue website subject error income tax portal filing form 15cb dsc quot something went wrong please try agian laterquot id xxxxx dear sir reference error showing income tax portal filing form 15cb dsc tried file form 15cb however attaching dsc verification showing error quot thing went wrong please try laterquot trying file form week however error showing need file said form comply law regulation therefore request good self kindly resolve soon possible"
    # text_to_classify = "telecommunication malpractice corruption complaint related financial irregularity employee related case airtel broadband miss behav technician landline number x6x1x4x9x2x complain number service reqst number reference number x0x2x1x1x8x mere service reqst pe koi v action kyon nahi liya gayatechnician ne mujhse otp pucha happy code maine otp nahi batayatechnician ne mera broadband wired pole se nikal diya technician rahul kumar technician ka mobile number x0x1x0x4x3 regard pankaj kumar mobile x1x3x1x0x5"
    # text_to_classify = "telecommunication mobile related data speed lower commited mobile number x4x3x1x0x2 service provider msbharti airtel ltd mobile internet speed slow hanuman hatha near rajpurohit sabha bhwan bikaner rajasthan 334001"
    predicted_class, confidence = classify_text(text_to_classify, tokenizer, model)
    print(f"Predicted class: {predicted_class} with confidence {confidence}")

if __name__ == "__main__":
    main()
