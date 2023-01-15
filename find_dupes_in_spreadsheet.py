import pandas as pd

def find_duplicates(filepath, columns):
    df = pd.read_excel(filepath)
    return list(df.loc[df.duplicated(subset=columns)])

filepath = 'path/to/excel/file.xlsx'
columns = ['column1', 'column2']
duplicates = find_duplicates(filepath, columns)
print("Duplicate values:", duplicates)

#In this code, the pandas library is used to read the Excel file using the read_excel() function. The duplicated() function is used to identify duplicate rows in the DataFrame. The subset parameter is passed with a list of columns ['column1', 'column2'] to check for duplicate only in these columns. The loc property is used to select only the duplicate rows. Finally, the selected rows are converted to a list and returned.

#You can replace 'path/to/excel/file.xlsx' with the path to your Excel file, and replace ['column1', 'column2'] with the list of column names you want to check for duplicates in.