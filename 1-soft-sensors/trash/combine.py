import pandas as pd
import numpy as np

# Read the CSV file into a DataFrame
df = pd.read_csv('data.csv')

# Determine the number of rows per split
num_splits = 6
rows_per_split = int(np.ceil(len(df) / num_splits))

# Split the DataFrame into 5 equal parts
for i in range(num_splits):
    # Get the start and end indices for the current split
    start_idx = i * rows_per_split
    end_idx = start_idx + rows_per_split
    
    # Slice the DataFrame to get the current part
    df_part = df.iloc[start_idx:end_idx]
    
    # Save the current part to a new CSV file
    df_part.to_csv(f'data{i+1}.csv', index=False)

print("Data has been successfully split into 5 parts.")
