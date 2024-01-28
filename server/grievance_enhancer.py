import time
import json

from flask import jsonify
from common_func import generate_id, load_dept_json_file, load_json_file, save_dept_json_file, save_json_file, update_dept_status
from enhance_complaint import enhance_complaint
from new_pred import set_new_predict_pipe
from predict_dept_text import set_predict_pipe
from rephrase_text import init_rephrase_model, init_summarize_model
from sentiment_text import init_sentiment_model

from severity_text import init_severity_model

def process_records():
    try:
        data = load_json_file()
        for record in data:
            # record = jsonify(rc)
            if 'status' in record and record['status'] == "1":
                attrs =  enhance_grievance(record['subject_content_text'])
                dept_code = attrs["predicted_dept"]
                count = get_total_complaints(dept_code, "KN")
                generated_id = generate_id(dept_code, "E", count)
                record["id"]=generated_id
                record["registration_no"]=generated_id
                record["attributes"] = attrs
                record["status"] = "2"
                record["org_code"] = dept_code
                # rc.update(record)
                update_dept_status(dept_code, "NEW")
                print(f"Processing record with id: {record.get('id')}")
                # Add your processing logic here
        save_json_file(data)
    except FileNotFoundError:
        print(f"The file was not found.")
    except json.JSONDecodeError:
        print(f"Error decoding JSON from the file")

def main():
    while True:
        print("Checking for records...")
        process_records()
        print("Waiting for 10 minutes before next check...")
        time.sleep(100)  # Wait for 10 minutes (600 seconds)
      
        
def enhance_grievance(new_data):
    json_d = enhance_complaint(sev_model, predict_pipe_model, 
        sentiment_model, rephrase_model, summarize_model, 
        new_data)
    attributes = json.loads(json_d)
    return attributes

def initialize_new_dept(org_code, state):
    new_dept = {
    "id": org_code,
    "org_code": org_code,
    "year": "2024",
    "state": state,
    "total_complaints": 0,
    "new_complaints": 0,
    "in_process_complaints": 0,
    "resolved_complaints": 0,
    "reopened_complaints": 0,
    "feedback_score": 0.0
    }
    return new_dept

def get_total_complaints(org_code, state):
    dept_data = load_dept_json_file()
    for ditem in dept_data:
        if ditem['org_code'] == org_code:
            return ditem['total_complaints']
    # add new dept in case org_code not found
    new_d = initialize_new_dept(org_code, state)
    dept_data.append(new_d)
    save_dept_json_file(dept_data)
    dept_data = load_dept_json_file()
    return 0

sev_model = init_severity_model()
predict_pipe_model = set_new_predict_pipe()
sentiment_model = init_sentiment_model()
rephrase_model = init_rephrase_model()
summarize_model = init_summarize_model()


if __name__ == "__main__":
    main()
