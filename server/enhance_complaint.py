import json
from common_func import clean_text
from predict_dept_text import set_predict_pipe
from rephrase_text import init_rephrase_model, init_summarize_model
from sentiment_text import init_sentiment_model
from severity_text import init_severity_model

def enhance_complaint(sev_model, predict_pipe_model, sentiment_model, rephrase_model, summarize_model, text):
    c_text = clean_text(text)
    sentiment_value = sentiment_model(c_text)
    severity_value = sev_model.predict([c_text])
    predict_dept_value = predict_pipe_model.predict([c_text])
    response = rephrase_model(c_text, max_length=100, num_beams=5, early_stopping=True)
    rephrase_value = response[0]['generated_text']
    summary = summarize_model(c_text, max_length=100, min_length=30, do_sample=False)
    summary_value = summary[0]['summary_text']

    # Creating a dictionary with all values
    data = {
        "clean_text": c_text,
        "sentiment": sentiment_value,
        "severity": severity_value[0],
        "predicted_dept": predict_dept_value[0],
        "rephrased_text": rephrase_value,
        "summary": summary_value
    }

    # Convert the dictionary to a JSON string
    json_data = json.dumps(data)
    print(json_data)
    return json_data

