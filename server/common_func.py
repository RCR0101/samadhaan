# Function to load JSON data
import json
import re
from flask import jsonify
import nltk
import pandas as pd
import json
from datetime import datetime

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

from datetime import datetime

def add_complaints(data):
    data['total_complaints'] += 1
    data['new_complaints'] += 1
    return data

def resolve_complaints(data):
    data['resolved_complaints'] += 1
    data['new_complaints'] -= 1
    return data

def update_org_data(org_list, org_code, new_data):
    # Iterate through the list of organizations
    for org in org_list:
        # Check if the current organization matches the org_code
        if org['org_code'] == org_code:
            # Update the organization's data with new_data
            org.update(new_data)
            return "Organization data updated successfully."
    return "Organization code not found."

def update_dept_status(code, type):
    dept_data = load_dept_json_file()
    new_data = next((item for item in dept_data if item['org_code'] == code), None)
    if type == "NEW":
        new_data = add_complaints(new_data)
    elif type == "RESOLVE":
        new_data = resolve_complaints(new_data)
    
    update_org_data(dept_data, code, new_data)  
    # new_data.update(dept_data) 
    save_dept_json_file(dept_data)
    # return jsonify(new_data)

def load_json_file():
    with open(f'json/complaints.json', 'r') as file:
        data = json.load(file)
    return data

def load_user_json_file():
    with open(f'json/users.json', 'r') as file:
        data = json.load(file)
    return data

def load_dept_json_file():
    with open(f'json/target_depts.json', 'r') as file:
        data = json.load(file)
    return data

# Function to save JSON data
def save_json_file(data):
    with open(f'json/complaints.json', 'w') as file:
        json.dump(data, file, indent=4)
        
# Function to save JSON data
def save_dept_json_file(data):
    with open(f'json/target_depts.json', 'w') as file:
        json.dump(data, file, indent=4)

def clean_text(text):
    # Text normalization
    text = re.sub(r'\r\n', ' ', text)  # Remove new lines
    text = re.sub(r'\s+', ' ', text)   # Remove extra spaces
    text = text.lower()                # Convert to lowercase
    # Remove punctuation (optional based on the need)
    text = re.sub(r'[^\w\s]', '', text)
    # Tokenization
    tokens = word_tokenize(text)
    # Stop words removal
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words]
    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]
    # Joining the tokens back into a string
    return ' '.join(lemmatized_tokens)



def generate_id(organization, category, count):
    current_year = datetime.now().year
    formatted_count = str(count + 1).zfill(7)  # Pad the count with zeros to make it 7 digits
    return f"{organization}/{category}/{current_year}/{formatted_count}"

# Create the dictionary with the nested structure
def get_diary_date():
    data = {
    # "DiaryDate": {
        "$date": datetime.utcnow().isoformat() + "Z"  # generates current UTC time in ISO format
    # }
    }   
    return data
    # Convert the dictionary to a JSON string
    json_data = json.dumps(data, indent=4)

    # # Print or use the JSON data as needed
    # print(json_data)
    return json_data


# Example usage
# organization = "MODEF"
# category = "E"
# count = 1
# generated_id = generate_id(organization, category, count)
# print(f"_id: {generated_id}")