import pandas as pd
from math import ceil

def split_csv(filename, chunk_size=5000):
    # Read the CSV file
    df = pd.read_csv(filename)

    # Calculate the number of chunks
    number_of_chunks = ceil(len(df) / chunk_size)

    # Split the DataFrame into chunks
    chunks = [df[i:i + chunk_size] for i in range(0, len(df), chunk_size)]

    # Save each chunk into a new CSV file
    for i, chunk in enumerate(chunks):
        chunk.to_csv(f'text_dept_{i+1}.csv', index=False)

    print(f"CSV file '{filename}' has been split into {number_of_chunks} chunks.")

# Replace 'yourfile.csv' with the path to your CSV file
split_csv(f'post_process_full.csv')
