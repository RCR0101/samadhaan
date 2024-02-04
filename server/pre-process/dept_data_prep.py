import json
import csv

# Load the JSON data from a file (replace 'data.json' with the path to your JSON file)
with open(f'json/valid_action_history.json', 'r') as file:
    data = json.load(file)

# A dictionary to store org_code to org_id mapping to ensure uniqueness
org_id_mapping = {}
current_org_id = 0

# Open a CSV file for writing
with open(f'post_process_csv/out_dept_code_reg_no.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    # Write the header
    csvwriter.writerow(['registration_no', 'org_code', 'org_id'])

    # Process each item in the JSON data
    for item in data:
        # Check if action_status is "50"
        if item.get('action_status') == "50":
            reg_no = item.get('registration_no', '')
            org_code = item.get('org_code', '')

            # Generate or retrieve unique org_id
            if org_code not in org_id_mapping:
                org_id_mapping[org_code] = current_org_id
                current_org_id += 1
            org_id = org_id_mapping[org_code]

            # Write the data row to the CSV
            csvwriter.writerow([reg_no, org_code, org_id])

print('CSV file has been created successfully.')
