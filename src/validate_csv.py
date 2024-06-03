import sys
sys.path.append('./src')

from validate_date_format import date_month_year_format
import pandas as pd
import numpy as np

df = pd.read_csv("demo_purchase.csv", sep=",", header=None, skiprows=[0] , on_bad_lines='skip')
df.index = np.arange(1, len(df) + 1)
total_valid = 0
total_invalid = 0
list_invalid_dateformat = []
list_valid_dateformat = []
for index, row in df.iterrows():
    if date_month_year_format(row[2]):
        list_valid_dateformat.append(index)
        total_valid += 1
    else :
        list_invalid_dateformat.append(index)
        total_invalid += 1

print("List of invalid dateformat line : {} ".format(list_invalid_dateformat))
print("List of valid dateformat line : {} ".format(list_valid_dateformat))
print("Total valid dateformat : {}".format(total_valid))
print("Total invalid dateformat : {}".format(total_invalid))

print(df)