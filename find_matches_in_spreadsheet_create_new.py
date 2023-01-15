import pandas as pd

# Load spreadsheet
df = pd.read_excel('spreadsheet.xlsx')

# Define the column to check and the value to search for
column_to_check = 'Name'
value_to_search = 'John Smith'

# Use boolean mask to filter rows that contain the value
mask = df[column_to_check].str.contains(value_to_search)

# Save filtered DataFrame to a new Excel file
df[mask].to_excel('filtered_spreadsheet.xlsx', index=False)


#This will generate a new Excel file named 'filtered_spreadsheet.xlsx'
# in the same directory as the Python script, which will only contain the
# rows that match the value.
#Please make sure that the library openpyxl is installed in your system, 
#it's a dependency of pandas.

#!pip install openpyxl
