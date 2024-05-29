import sys
sys.path.append('./src')
from validate_date_format import iso8601_format
import pandas as pd
import numpy as np

# read text file into pandas DataFrame and
# create header
df = pd.read_csv("datelist.txt", sep=",",header=None ,on_bad_lines='skip',
                 names=["Order ID","Customer Name","Dates","Product ID","Quantity","Total Price"])
df.index = np.arange(1, len(df) + 1)

total_row = len(df)
current_line = 0
total_valid = 0
total_invalid = 0
list_invalid_dateformat = []
list_valid_dateformat = []
for i in range(total_row):
    current_line += 1
    if iso8601_format(df.loc[i+1,"Dates"]):
        list_valid_dateformat.append(current_line)
        total_valid += 1
    else :
        list_invalid_dateformat.append(current_line)
        total_invalid += 1

print("List of invalid dateformat line : {} ".format(list_invalid_dateformat))
print("List of valid dateformat line : {} ".format(list_valid_dateformat))
print("Total valid dateformat : {}".format(total_valid))
print("Total invalid dateformat : {}".format(total_invalid))

print(df)