from datetime import datetime
import pytest

def validate_dates(date_str1):
    try:
        datetime.strptime(date_str1,'%Y-%m-%d')
        return True
    except ValueError:
        return False

def validate_datetime(date_str2):
    try :
        datetime.strptime(date_str2,'%Y-%m-%d %H:%M:%S')
        return True
    except ValueError :
        return False
    
def validate_dateformat(date_str):
    if len(date_str) == 10 :
        return validate_dates(date_str)
    elif len(date_str) == 19 :
        return validate_datetime(date_str)
    else :
        return False

class TestValidDateCase:
    def test_valid_dates(self):
        assert validate_dateformat("2024-05-21") 
        assert validate_dateformat("1900-01-01")
        assert validate_dateformat("0001-01-01")
        assert validate_dateformat("9999-12-31")
        assert validate_dateformat("2024-05-12")

    def test_valid_datetimes(self):
        assert validate_dateformat("2024-05-21 00:00:00")
        assert validate_dateformat("2024-05-21 23:59:59")

class TestInvalidDateCase:
    def test_invalid_dates(self):
        assert not validate_dateformat("2024-05-32")
        assert not validate_dateformat("2024-06-31")
        assert not validate_dateformat("2024-13-01")
        assert not validate_dateformat("2024-06-1")
        assert not validate_dateformat("2024-6-01")
        assert not validate_dateformat("10000-01-01")
        

    def test_invalid_datetimes(self):
        assert not validate_dateformat("2024-05-21 any string")
        assert not validate_dateformat("2024-05-21 0:00:0")
        assert not validate_dateformat("2024-05-21 -1:00:0")
        assert not validate_dateformat("2024-05-21 25:00:00")
        assert not validate_dateformat("2024-05-21 22:61:00")
        assert not validate_dateformat("2024-05-21 22:00:60")
        assert not validate_dateformat("2024-05-21 22:00")
        assert not validate_dateformat("2024-05-21 22")

# pytest -q validation2.py