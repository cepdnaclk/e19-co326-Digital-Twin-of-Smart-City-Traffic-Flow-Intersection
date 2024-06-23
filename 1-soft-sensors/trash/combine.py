import pandas as pd
import numpy as np

# Read the CSV file into a DataFrame
df = pd.read_csv('data.csv')

# Determine the number of rows per split
num_splits = 3
rows_per_split = int(np.ceil(len(df) / num_splits))

# Split the DataFrame into 3 parts
splits = []
for i in range(num_splits):
    # Get the start and end indices for the current split
    start_idx = i * rows_per_split
    end_idx = start_idx + rows_per_split
    
    # Slice the DataFrame to get the current part
    df_part = df.iloc[start_idx:end_idx]
    splits.append(df_part)

# Replace columns 1, 2, and 3 in parts 2 and 3 with those from part 1
columns_to_replace = ['Time', 'Date', 'Day of the week']  # Replace with actual column names

for i in range(1, num_splits):
    splits[i][columns_to_replace] = splits[0][columns_to_replace].values

# Save each part to a new CSV file
for i, df_part in enumerate(splits):
    df_part.to_csv(f'data{i+1}.csv', index=False)

print("Data has been successfully split and columns replaced.")
