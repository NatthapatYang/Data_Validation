import sys
sys.path.append('./src')

from validate_date_format import validate_dateformat

f = open("./datelist.txt", "r")
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

print("List of invalid dateformat line : {} ".format(list_invalid_dateformat))
print("Total valid dateformat : {}".format(totalvalid))
print("Total invalid dateformat : {}".format(totalinvalid))