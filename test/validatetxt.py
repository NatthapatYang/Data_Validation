import sys
sys.path.append('../src')

from datetime import datetime
import pytest
from validate_date_format import validate_dateformat

f = open("../datelist.txt", "r")
totalline = f.readlines()

currentline = 0
totalvalid = 0
totalinvalid = 0
list_invalid_dateformat = []
for i in totalline:
    currentline += 1
    if validate_dateformat(i.strip()):
        totalvalid += 1
    else :
        list_invalid_dateformat.append(currentline)
        totalinvalid += 1

print("list of invalid dateformat line : {} ".format(list_invalid_dateformat))
print("total valid dateformat : {}".format(totalvalid))
print("total invalid dateformat : {}".format(totalinvalid))
    
""" form datelist.txt result after check valid or invalid dateformat
    valid = 7 
    invalid = 14 
    list of invalid dateformat line = [ 6 7 8 9 10 11 14 15 16 17 18 19 20 21 ] """