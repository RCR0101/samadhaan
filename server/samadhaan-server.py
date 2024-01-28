from contextlib import nullcontext
from flask import Flask, jsonify, request
import json
from flask import Flask, request, jsonify
import requests
from flask_cors import CORS
from requests.auth import HTTPBasicAuth
from urllib.parse import unquote
from common_func import clean_text, generate_id, get_diary_date, load_user_json_file, save_dept_json_file, update_dept_status
from enhance_complaint import enhance_complaint
from predict_dept_text import set_predict_pipe
from rephrase_text import init_rephrase_model, init_summarize_model
from sentiment_text import init_sentiment_model
from severity_text import init_severity_model

from common_func import load_dept_json_file, load_json_file, save_json_file
from predict_dept_text import set_predict_pipe

app = Flask(__name__)
CORS(app)



@app.route('/Complaints', methods=['GET'])
def get_json():
    # data = load_json_file()
    
    # Get pagination parameters from request, default is first 10 items
    start = int(request.args.get('start', 0))
    end = int(request.args.get('end', 100))
    total_count = len(data)

    # Paginate data
    paginated_data = data[start:end]

    selected_fields_data = [
        {field: item.get(field) for field in ['id', 'registration_no', 'DiaryDate', 'dist_name', 'org_code', 'title', 'UserCode', 'state']}
        for item in paginated_data if item.get('status') == '2'
    ]

    response = jsonify(selected_fields_data)
    response.headers['Access-Control-Expose-Headers'] = 'Content-Range, X-Total-Count'
    response.headers['Content-Range'] = f'items {start}-{end}/{total_count}'
    response.headers['X-Total-Count'] = total_count
    return response

@app.route('/Complaints/<path:id>', methods=['GET'])
def get_specific_json(id):
    # data = load_json_file()
    # decoded_id = unquote(id)
    specific_item = next((item for item in data if item['id'] == id), None)

    if specific_item:
        response = jsonify(specific_item)
        response.headers['Access-Control-Expose-Headers'] = 'X-Total-Count'
        response.headers['X-Total-Count'] = len(data)
        return response
    else:
        return jsonify({"error": "Item not found"}), 404

@app.route('/Complaints/User/<user_code>', methods=['GET'])
def get_complaints_by_user(user_code):
    # data = load_json_file()
    filtered_data = [
        {'registration_no': item['id'], 'status': item['status']}
        for item in data if item['UserCode'] == user_code and (item['status'] == "2" or item['status'] == "3")
    ]

    if filtered_data:
        response = jsonify(filtered_data)
        response.headers['Access-Control-Expose-Headers'] = 'X-Total-Count'
        response.headers['X-Total-Count'] = len(filtered_data)
        return response
    else:
        return jsonify({"error": "No items found for the given UserCode"}), 404

@app.route('/Departments', methods=['GET'])
def get_dept_json():
    # data = load_dept_json_file()
    # Get pagination parameters from request, default is first 10 items
    start = int(request.args.get('start', 0))
    end = int(request.args.get('end', 100))
    total_count = len(dept_data)

    # Paginate data
    paginated_data = dept_data[start:end]

    response = jsonify(paginated_data)
    response.headers['Access-Control-Expose-Headers'] = 'Content-Range, X-Total-Count'
    response.headers['Content-Range'] = f'items {start}-{end}/{total_count}'
    response.headers['X-Total-Count'] = 500
    return response

@app.route('/Users', methods=['GET'])
def get_users():
    user_data = load_user_json_file()
    start = int(request.args.get('start', 0))
    end = int(request.args.get('end', 100))
    total_count = len(user_data)

    # Paginate data
    paginated_data = user_data[start:end]

    response = jsonify(paginated_data)
    response.headers['Access-Control-Expose-Headers'] = 'Content-Range, X-Total-Count'
    response.headers['Content-Range'] = f'items {start}-{end}/{total_count}'
    response.headers['X-Total-Count'] = 500
    return response

@app.route('/Users', methods=['POST'])
def add_user():
    new_user = request.json
    try:
        with open(f'json/users.json', 'r+') as file:
            # Read the existing data
            users = json.load(file)
            new_user['UserCode'] = new_user['id']
            # Check if the user ID already exists
            if any(user['id'] == new_user['id'] for user in users):
                return jsonify({"error": "User with this ID already exists"}), 400

            # Add the new user
            users.append(new_user)

            # Move the file pointer to the beginning of the file
            file.seek(0)

            # Write the updated list back to the file
            json.dump(users, file, indent=4)

            # Truncate the file to the new size
            file.truncate()

        return jsonify(new_user), 201
    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404
    except json.JSONDecodeError:
        return jsonify({"error": "Error reading JSON file"}), 500
    

@app.route('/Departments/<int:id>', methods=['GET'])
def get_specific_dept_json(id):
    # data = load_dept_json_file()
    specific_item = next((item for item in dept_data if item['id'] == id), None)
    if specific_item:
        response = jsonify(specific_item)
        response.headers['Access-Control-Expose-Headers'] = 'X-Total-Count'
        response.headers['X-Total-Count'] = len(dept_data)
        return response
    else:
        return jsonify({"error": "Item not found"}), 404

@app.route('/Users/<id>', methods=['GET'])
def get_specific_user_json(id):
    # data = load_dept_json_file()
    specific_item = next((item for item in user_data if item['id'] == id), None)
    if specific_item:
        response = jsonify(specific_item)
        response.headers['Access-Control-Expose-Headers'] = 'X-Total-Count'
        response.headers['X-Total-Count'] = len(dept_data)
        return response
    else:
        return jsonify({"error": "Item not found"}), 404
    
@app.route('/Complaints', methods=['POST', 'PUT'])
def update_json():
    new_data = request.get_json()

    if request.method == 'POST':
        dept_code = "TBD" 
        # enhance_grievance(new_data)
        category = "T"
        # count = get_total_complaints(dept_code, "KN")
        generated_id = generate_id(dept_code, category, 100)
        new_data["id"]=generated_id
        new_data["org_code"]=dept_code
        new_data["attributes"] = ""
        new_data["status"]="1"
        new_data["DiaryDate"]= get_diary_date()
        new_data["remarks_text"]=""
        new_data["resolution_date"]= ""
        data.append(new_data)
    elif request.method == 'PUT':
        for item in data:
            if item['id'] == new_data['id']:
                new_data["status"] = "3"
                new_data["resolution_date"]= get_diary_date()
                item.update(new_data)
                update_dept_status(item['org_code'], "RESOLVE")
                break
            
    # save_dept_json_file()
    save_json_file(data)
    return jsonify(new_data)


user_data = load_user_json_file()
data = load_json_file()
dept_data = load_dept_json_file()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5008)