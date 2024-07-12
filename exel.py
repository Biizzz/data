import pandas as pd

# Replace 'your_file.xlsx' with the path to your Excel file
excel_file_path = 'your_file.xlsx'

# Read the Excel file
df = pd.read_excel(excel_file_path)

# Replace 'your_file.csv' with the desired path for the CSV file
csv_file_path = 'your_file.csv'

# Save the DataFrame as a CSV file
df.to_csv(csv_file_path, index=False)

print(f"Excel file {excel_file_path} has been converted to CSV file {csv_file_path}")
