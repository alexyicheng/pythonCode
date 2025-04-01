# 31.03.2025

import pandas as pd

pd.read_excel('insert path')

file_path = r''

excel_file = pd.ExcelFile(file_path)

data_list = []
sheets = excel_file.sheet_names
for s in sheets:
    data = excel_file.parse(s)
    if not data.empty:
        data_list.append(data)

df = pd.concat(data_list)
# df.index =