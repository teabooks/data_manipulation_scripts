import os
import pandas as pd

# specify the directory where the spreadsheets are located
directory = 'path/to/spreadsheets'

# create an empty dataframe to store the rows
rows = pd.DataFrame()

# iterate over the spreadsheets in the directory
for filename in os.listdir(directory):
    # only process excel files
    if filename.endswith('.xlsx'):
        # read the spreadsheet into a dataframe
        df = pd.read_excel(os.path.join(directory, filename))
        # append the rows to the dataframe
        rows = rows.append(df, ignore_index=True)

# drop duplicates from the dataframe
rows = rows.drop_duplicates()

# write the deduplicated rows to a new spreadsheet
rows.to_excel('deduped_rows.xlsx', index=False)

#This script first import the pandas library and specify the directory where the spreadsheets are located. Then it creates an empty dataframe called rows, which will be used to store the rows from the spreadsheets. It iterates over the spreadsheets in the directory and for each spreadsheet it reads the spreadsheet into a dataframe, and appends the rows to the dataframe. Finally, it drops the duplicates from the dataframe and writes the deduplicated rows to a new spreadsheet named deduped_rows.xlsx

#Note that the script only processes excel files that end with the '.xlsx' extension, you can modify it to include any spreadsheet file types you desire.
#Also it's worth noting that to work with other spreadsheet formats such as csv, you have to use pd.read_csv instead of pd.read_excel and use .csv instead of .xlsx