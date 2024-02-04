import pandas as pd

# Assuming your data is in a DataFrame
df = pd.read_csv(f'post_process_csv/text_label_dept.csv')

# Check for NaN values
print(df.isna().sum())

# Option 1: Drop rows with NaN values
df.dropna(inplace=True)

# Assuming 'df' is your DataFrame
df.to_csv(f'post_process_csv/text_label_dept.csv', index=False)
