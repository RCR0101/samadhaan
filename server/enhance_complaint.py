import json
from common_func import clean_text
from predict_depart import TextClassifier
from infer_severity import TextProcessor

def enhance_complaint(text, processor, classifier):
    c_text = clean_text(text)
    # sentiment_value = sentiment_model(c_text)
    # severity_value = sev_model.predict([c_text])
    # predict_dept_value = predict_pipe_model.predict([c_text])
    # response = rephrase_model(c_text, max_length=100, num_beams=5, early_stopping=True)
    # rephrase_value = response[0]['generated_text']
    # # summary = summarize_model(c_text, max_length=100, min_length=30, do_sample=False)
    summary_text = processor.get_summary_text(text)
    severity_value = processor.get_severity(summary_text)
    dept_json = json.loads(classifier.predict_dept(text))
    print(severity_value)
    print(dept_json)
    # Creating a dictionary with all values
    data = {
        "clean_text": c_text,
        "severity": severity_value,
        "predicted_dept": dept_json["dept_code"],
        "predicted_dept_confidence": dept_json["confidence"],
        "summary": summary_text
    }

    # Convert the dictionary to a JSON string
    json_data = json.dumps(data)
    print(json_data)
    return json_data

