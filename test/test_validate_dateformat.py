import sys
sys.path.append('./src')

from validate_date_format import iso8601_format , date_month_year_format

class TestValidDateCase:
    def test_valid_dates(self):
        assert "2024-05-21" == iso8601_format("2024-05-21")
        assert "1900-01-01" == iso8601_format("1900-01-01")
        assert "0001-01-01" == iso8601_format("0001-01-01")
        assert "9999-12-31" == iso8601_format("9999-12-31")
        assert "2024-05-12" == iso8601_format("2024-05-12")
        assert "11/02/2024" == date_month_year_format("11/02/2024")
        assert "31/05/2024" == date_month_year_format("31/05/2024")

    def test_valid_datetimes(self):
        assert "2024-05-21" ==  iso8601_format("2024-05-21 00:00:00")
        assert "2024-05-21" ==  iso8601_format("2024-05-21 23:59:59")
        assert "27/02/2024" == date_month_year_format("27/02/2024 01:12:12")
        assert "10/02/2024" == date_month_year_format("10/02/2024 23:38:43")
        
class TestInvalidDateCase:
    def test_invalid_dates(self):
        assert not "2024-05-32" == iso8601_format("2024-05-32")
        assert not "2024-06-31" == iso8601_format("2024-06-31")
        assert not "2024-13-01" == iso8601_format("2024-13-01")
        assert not "2024-06-1" == iso8601_format("2024-06-1")
        assert not "2024-6-01" == iso8601_format("2024-6-01")
        assert not "10000-01-01" == iso8601_format("10000-01-01")
        assert not "11/24/2024" == date_month_year_format("11/24/2024")
        assert not "32/07/2024" == date_month_year_format("32/07/2024")

    def test_invalid_datetimes(self):
        assert not "2024-05-21" == iso8601_format("2024-05-21 any string")
        assert not "2024-05-21" == iso8601_format("2024-05-21 0:00:0")
        assert not "2024-05-21" == iso8601_format("2024-05-21 -1:00:0")
        assert not "2024-05-21" == iso8601_format("2024-05-21 25:00:00")
        assert not "2024-05-21" == iso8601_format("2024-05-21 22:61:00")
        assert not "2024-05-21" == iso8601_format("2024-05-21 22:00:60")
        assert not "2024-05-21" == iso8601_format("2024-05-21 22:00")
        assert not "2024-05-21" == iso8601_format("2024-05-21 22")
        assert not "27/22/2024" == date_month_year_format("27/22/2024 01:12:12")
        assert not "17/02/2024" == date_month_year_format("17/02/2024 25:34:24")
