from datetime import datetime
import sys

def validate_dates(str_date):
    try:
        datetime.strptime(str_date,'%Y-%m-%d')
        return str_date
    except ValueError:
        return False

def validate_datetime(str_date):
    try :
        datetime.strptime(str_date,'%Y-%m-%d %H:%M:%S')
        return str_date.split(' ')[0]
    except ValueError :
        return False

def validate_dateformat(str_date):
    if len(str_date) == 10:
        return validate_dates(str_date)
    elif len(str_date) == 19:
        return validate_datetime(str_date)
    else :
        return False

if __name__ == '__main__':
	valid_date = validate_dateformat(sys.argv[1])
	print(valid_date)