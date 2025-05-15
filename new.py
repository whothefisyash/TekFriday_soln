import pandas as pd

xls = pd.ExcelFile("dataset.xlsx")

sheet_names = xls.sheet_names

for sheet in sheet_names:
    df = xls.parse(sheet)
    df.to_csv(f"datasets/{sheet}.csv", index=False)
