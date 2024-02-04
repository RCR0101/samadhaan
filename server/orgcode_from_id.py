import pandas as pd

class OrgCodeLookup:
    def __init__(self, csv_path):
        # Load the CSV file into a DataFrame only once during initialization
        self.df = pd.read_csv(csv_path)
    
    def get_org_code_from_id(self, org_id):
        # Use the loaded DataFrame to find the row with the matching org_id
        matching_rows = self.df[self.df['org_id'] == org_id]
        
        # If there's at least one match, return the first 'org_code' found
        if not matching_rows.empty:
            return matching_rows.iloc[0]['org_code']
        else:
            # Return some indication that the org_id was not found
            return "Org ID not found"

# Example usage
# csv_path = f'post_process_csv/out_dept_code_reg_no.csv'  # Update this to the path of your actual CSV file
# lookup = OrgCodeLookup(csv_path)

# # Now you can call get_org_code_from_id multiple times without reloading the CSV
# org_id_to_lookup = 8
# print(f"Org Code for ID {org_id_to_lookup}: {lookup.get_org_code_from_id(org_id_to_lookup)}")

# org_id_to_lookup = 339
# print(f"Org Code for ID {org_id_to_lookup}: {lookup.get_org_code_from_id(org_id_to_lookup)}")
