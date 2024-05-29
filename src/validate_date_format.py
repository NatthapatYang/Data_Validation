from datetime import datetime
import sys

# Validate ISO 8601 Format
def validate_dates_iso8601format(str_date):
    try:
        datetime.strptime(str_date,'%Y-%m-%d')
        return str_date
    except ValueError:
        return False

def validate_datetime_iso8601format(str_date):
    try :
        datetime.strptime(str_date,'%Y-%m-%d %H:%M:%S')
        return str_date.split(' ')[0]
    except ValueError :
        return False

def iso8601_format(str_date):
    if len(str_date) == 10:
        return validate_dates_iso8601format(str_date)
    elif len(str_date) == 19:
        return validate_datetime_iso8601format(str_date)
    else :
        return False

# Validate Date-Month-Year Format
def validate_dates_date_month_year_format(str_date):
    try:
        datetime.strptime(str_date,'%d/%m/%Y')
        return str_date
    except ValueError:
        return False

def validate_datetime_date_month_year_format(str_date):
    try :
        datetime.strptime(str_date,'%d/%m/%Y %H:%M:%S')
        return str_date.split(' ')[0]
    except ValueError :
        return False

def date_month_year_format(str_date):
    if len(str_date) == 10:
        return validate_dates_date_month_year_format(str_date)
    elif len(str_date) == 19:
        return validate_datetime_date_month_year_format(str_date)
    else :
        return False

if __name__ == '__main__':
	valid_date = iso8601_format(sys.argv[1])
	print(valid_date)