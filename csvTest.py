from pprint import pprint

import pandas as pd

# read excel data file, convert to csv
read_file = pd.read_excel(r"C:\Users\Rachel\Documents\nba rookie data.xlsx", sheet_name="nba rookies", usecols="G:L")
csvData = read_file.to_csv(r'C:\Users\Rachel\Documents\rookie_csv.csv', index=bool, header=True)
print(csvData)
