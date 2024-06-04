import sys
sys.path.append('./src')

from validate_date_format import iso8601_format
import pandas as pd

df = pd.read_csv("datelist.txt", sep=",",header=None ,on_bad_lines='skip',
                 names=["Order ID","Customer Name","Dates","Product ID","Quantity","Total Price"])
df.index = list(range(1, len(df) + 1))

total_valid = 0
total_invalid = 0
list_invalid_dateformat = []
list_valid_dateformat = []
for row, column in df.iterrows():
    if iso8601_format(column["Dates"]):
        list_valid_dateformat.append(row)
        total_valid += 1
    else :
        list_invalid_dateformat.append(row)
        total_invalid += 1

print("List of invalid dateformat line : {} ".format(list_invalid_dateformat))
print("List of valid dateformat line : {} ".format(list_valid_dateformat))
print("Total valid dateformat : {}".format(total_valid))
print("Total invalid dateformat : {}".format(total_invalid))

print(df)