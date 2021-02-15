import excel2json

import pandas

excel_data_df = pandas.read_excel('./downloads/Chunmun PP Stock Sheet to be Uploaded.xlsx', sheet_name='Sheet1')

json_str = excel_data_df.to_json(orient='records')

print('Excel Sheet to JSON:\n', json_str)