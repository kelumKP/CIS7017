import pandas as pd
import os

# Path to the directory containing the CSV files
directory_path = '/Users/kelumrubasin/Desktop/MSC_DATA_SCIENCE/8_Technology_Dissertation/Assignment_CIS7017/CIS7017/DATASETS/CSE_DATA/COMPANY_DATA/DAILY_SHARE_TRADING_STATISTICS_SUMMARY_2006_2022/'

# List all CSV files in the directory
csv_files = [file for file in os.listdir(directory_path) if file.endswith('.csv')]

# Initialize a variable to store the total row count
total_row_count = 0

# Iterate through each CSV file and count rows
for csv_file in csv_files:
    csv_path = os.path.join(directory_path, csv_file)
    df = pd.read_csv(csv_path)
    rows_count = df.shape[0]
    print(f"File: {csv_file}, Rows: {rows_count}")    
    total_row_count += rows_count

# Print the final total row count
print(f"Total Rows Across All CSV Files: {total_row_count}")