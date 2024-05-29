import sys
sys.path.append('./src')
from datetime import datetime
import pytest
from validate_date_format import iso8601_format
import pandas as pd
import numpy as np

# read text file into pandas DataFrame and
# create header
df = pd.read_csv("datelist.txt", sep=",",header=None ,on_bad_lines='skip',
                 names=["Order ID","Customer Name","Dates","Product ID","Quantity","Total Price"])
df.index = np.arange(1, len(df) + 1)

totalrow = len(df)
currentline = 0
totalvalid = 0
totalinvalid = 0
list_invalid_dateformat = []
list_valid_dateformat = []
for i in range(totalrow):
    currentline += 1
    if iso8601_format(df.loc[i+1,"Dates"]):
        list_valid_dateformat.append(currentline)
        totalvalid += 1
    else :
        list_invalid_dateformat.append(currentline)
        totalinvalid += 1

print("list of invalid dateformat line : {} ".format(list_invalid_dateformat))
print("list of valid dateformat line : {} ".format(list_valid_dateformat))
print("total valid dateformat : {}".format(totalvalid))
print("total invalid dateformat : {}".format(totalinvalid))

print(df)