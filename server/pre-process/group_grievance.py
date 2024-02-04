import csv
import json

# Load the JSON data from a file (replace 'data.json' with the path to your JSON file)
with open(f'json/valid_grievance_all.json', 'r') as file:
    json_data = json.load(file)

# Load the CSV data into a dictionary for quick look-up
csv_data = {}
with open(f'post_process_csv/out_dept_code_reg_no.csv', mode='r') as infile:
    reader = csv.reader(infile)
    next(reader, None)  # Skip the header
    for rows in reader:
        registration_no, org_code, org_id = rows
        csv_data[registration_no] = org_id

# Create a new CSV file and write the matched data
with open(f'post_process_csv/text_label_dept.csv', 'w', newline='', encoding='utf-8') as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(['text', 'label'])  # Write the header

    # Go through the JSON data and find the matching registration numbers in the CSV data
    for entry in json_data:
        reg_no = entry.get('registration_no')
        if reg_no in csv_data:
            text = entry.get('subject_content_text', '').replace('\r\n', ' ').replace('\t', ' ').strip()
            label = csv_data[reg_no]
            csvwriter.writerow([text, label])

print('New CSV file has been created with text and label columns.')


