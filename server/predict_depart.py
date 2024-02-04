import torch
import json
from transformers import BertTokenizer, BertForSequenceClassification
from orgcode_from_id import OrgCodeLookup

class TextClassifier:
    def __init__(self):
        model_path = './models/predict_dept'
        device = 'cuda' if torch.cuda.is_available() else 'cpu'  # Use GPU if available
        self.tokenizer = BertTokenizer.from_pretrained(model_path)
        self.model = BertForSequenceClassification.from_pretrained(model_path)
        self.model.to(device)
        self.device = device
        csv_path = f'post_process_csv/out_dept_code_reg_no.csv'  # Update this to the path of your actual CSV file
        self.lookup = OrgCodeLookup(csv_path)
        # self.text_processor = TextProcessor()
    
    def classify_text(self, text):
        inputs = self.tokenizer.encode_plus(
            text,
            add_special_tokens=True,
            max_length=512,
            return_token_type_ids=False,
            padding='max_length',
            return_attention_mask=True,
            return_tensors='pt',
        )
        
        input_ids = inputs['input_ids'].to(self.device)
        attention_mask = inputs['attention_mask'].to(self.device)

        self.model.eval()
        with torch.no_grad():
            outputs = self.model(input_ids, attention_mask=attention_mask)

        logits = outputs.logits
        probabilities = torch.nn.functional.softmax(logits, dim=1)
        predicted_class = torch.argmax(probabilities, dim=1).item()
        confidence = probabilities[0][predicted_class].item()
        
        return predicted_class, confidence
    
    def predict_dept(self, text_msg):
        predicted_class, confidence = self.classify_text(text_msg)
        result = {
            "predicted_dept": predicted_class,
            "dept_code": self.lookup.get_org_code_from_id(predicted_class),
            "confidence": confidence
        }
        json_result = json.dumps(result)
        return json_result

# text_classifier = TextClassifier()
# text_to_classify = "telecommunication malpractice corruption complaint related financial irregularity employee related case airtel broadband miss behav technician landline number x6x1x4x9x2x complain number service reqst number reference number x0x2x1x1x8x mere service reqst pe koi v action kyon nahi liya gayatechnician ne mujhse otp pucha happy code maine otp nahi batayatechnician ne mera broadband wired pole se nikal diya technician rahul kumar technician ka mobile number x0x1x0x4x3 regard pankaj kumar mobile x1x3x1x0x5"
# print(text_classifier.predict_dept(text_to_classify))
# # print(f"Predicted class: {predicted_class} with confidence {confidence}")

