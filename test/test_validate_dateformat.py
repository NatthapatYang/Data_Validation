import sys
sys.path.append('./src')

from validate_date_format import validate_dateformat

class TestValidDateCase:
    def test_valid_dates(self):
        assert "2024-05-21" == validate_dateformat("2024-05-21")
        assert "1900-01-01" == validate_dateformat("1900-01-01")
        assert "0001-01-01" == validate_dateformat("0001-01-01")
        assert "9999-12-31" == validate_dateformat("9999-12-31")
        assert "2024-05-12" == validate_dateformat("2024-05-12")

    def test_valid_datetimes(self):
        assert "2024-05-21" ==  validate_dateformat("2024-05-21 00:00:00")
        assert "2024-05-21" ==  validate_dateformat("2024-05-21 23:59:59")

class TestInvalidDateCase:
    def test_invalid_dates(self):
        assert not "2024-05-32" == validate_dateformat("2024-05-32")
        assert not "2024-06-31" == validate_dateformat("2024-06-31")
        assert not "2024-13-01" == validate_dateformat("2024-13-01")
        assert not "2024-06-1" == validate_dateformat("2024-06-1")
        assert not "2024-6-01" == validate_dateformat("2024-6-01")
        assert not "10000-01-01" == validate_dateformat("10000-01-01")

    def test_invalid_datetimes(self):
        assert not "2024-05-21 any string" == validate_dateformat("2024-05-21 any string")
        assert not "2024-05-21 0:00:0" == validate_dateformat("2024-05-21 0:00:0")
        assert not "2024-05-21 -1:00:0" == validate_dateformat("2024-05-21 -1:00:0")
        assert not "2024-05-21 25:00:00" == validate_dateformat("2024-05-21 25:00:00")
        assert not "2024-05-21 22:61:00" == validate_dateformat("2024-05-21 22:61:00")
        assert not "2024-05-21 22:00:60" == validate_dateformat("2024-05-21 22:00:60")
        assert not "2024-05-21 22:00" == validate_dateformat("2024-05-21 22:00")
        assert not "2024-05-21 22" == validate_dateformat("2024-05-21 22")