import json
import re
import nltk
import pandas as pd
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

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


count = 1
# Initialize empty lists for training data
texts = []
depts = []
officers = []

# Load the JSON files
with open(f"C:\\Users\\milid\\apps\\samadhaan\\scripts\\json\\valid_no_pii_grievance-part1.json") as f1:
    data1 = json.load(f1)
with open(f"C:\\Users\\milid\\apps\\samadhaan\\scripts\\json\\valid_no_pii_action_history.json") as f2:
    data2 = json.load(f2)

# Extract relevant information from JSON files
for entry in data1:  # Assuming each file contains a list of entries
    if "subject_content_text" in entry:
        cleaned_text = clean_text(entry["subject_content_text"])

    # Define your filter criteria
    target_registration_no = entry["registration_no"]
    target_action_status = "50"

    # Filter the data
    filtered_data = [element for element in data2 if element.get("registration_no") == target_registration_no and element.get("action_status") == target_action_status]
    for item in filtered_data:
        texts.append(cleaned_text)
        depts.append(item["org_code"])
        officers.append(item["OfficerDetail"])
        print(count)
        count = count + 1

df = pd.DataFrame({'Text': texts, 'Depts': depts, "Officers": officers})

df.to_csv('co-related_data-part1.csv', index=False)

# df = pd.read_json('co-related_data.json')
# features = df['Text']  # Column containing text data
# labels = df['Label']   # Column containing the labels

# for entry in data2:  # Assuming each file contains a list of entries
#     if "OfficerDetail" in entry:      
#         labels.append(entry["OfficerDetail"])

# Create a pipeline for text classification
pipeline = Pipeline([
("tfidf", TfidfVectorizer()),
("clf", LinearSVC())
])

pipeline.fit(texts, depts)

new_complaint_text = "Allegations of corruption in MGNREGA schemes"
new_complaint_text_cleaned = clean_text(new_complaint_text)
predicted_officer = pipeline.predict([new_complaint_text_cleaned])

print("Predicted Officer:", predicted_officer[0])