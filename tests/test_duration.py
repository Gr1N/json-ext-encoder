from datetime import timedelta

from json_ext_encoder import duration


def test_iso_simple():
    td = timedelta(hours=1, minutes=3, seconds=5)
    assert duration.iso_string(td) == "P0DT01H03M05S"


def test_iso_days():
    td = timedelta(days=1, hours=1, minutes=3, seconds=5)
    assert duration.iso_string(td) == "P1DT01H03M05S"


def test_iso_microseconds():
    td = timedelta(hours=1, minutes=3, seconds=5, microseconds=12345)
    assert duration.iso_string(td) == "P0DT01H03M05.012345S"


def test_iso_negative():
    td = -1 * timedelta(days=1, hours=1, minutes=3, seconds=5)
    assert duration.iso_string(td) == "-P1DT01H03M05S"
