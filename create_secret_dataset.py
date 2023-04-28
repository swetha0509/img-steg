import csv
import re

# Define the name of the CSV file
csv_filename = "spam.csv"

# Define the name of the column to extract
column_name = "v2"

# Define the regular expression to clean the rows
regex = r"[^a-zA-Z0-9\s]"

# Define the maximum number of rows to save
max_rows = 700

# Open the CSV file
with open(csv_filename, "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    # Extract the column and clean the rows
    column_data = [re.sub(regex, "", row[column_name]) for row in csv_reader][:max_rows]
    
    # Save each row as a separate text file
    for i, row in enumerate(column_data):
        filename = f"secret_msg_{i + 1}.txt"
        with open(filename, "w") as text_file:
            text_file.write(row)
