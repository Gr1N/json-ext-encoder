import datetime
import decimal
import enum
import json
import uuid

import dateutil.tz
import iso8601
import pytest

from json_ext_encoder import JSONEncoder


def test_ok():
    test_time = iso8601.parse_date('2017-09-29T11:33:28.668280+00:00')

    class TestEnum(enum.Enum):
        FOO = 'foo'

    in_ = {
        'datetime': test_time,
        'date': test_time.date(),
        'time': test_time.time(),
        'timedelta': datetime.timedelta(seconds=42),
        'decimal': decimal.Decimal('42.24'),
        'uuid': uuid.UUID('9518e078-9b02-43b5-8a25-f8b25d99374b'),
        'enum': TestEnum.FOO,
    }

    out = json.dumps(in_, cls=JSONEncoder)
    assert out == (
        '{"datetime": "2017-09-29T11:33:28.668Z",'
        ' "date": "2017-09-29",'
        ' "time": "11:33:28.668",'
        ' "timedelta": "P0DT00H00M42S",'
        ' "decimal": "42.24",'
        ' "uuid": "9518e078-9b02-43b5-8a25-f8b25d99374b",'
        ' "enum": "foo"}'
    )
    assert json.loads(out) == {
        'datetime': '2017-09-29T11:33:28.668Z',
        'date': '2017-09-29',
        'time': '11:33:28.668',
        'timedelta': 'P0DT00H00M42S',
        'decimal': '42.24',
        'uuid': '9518e078-9b02-43b5-8a25-f8b25d99374b',
        'enum': TestEnum.FOO.value,
    }


def test_unknown_obj():
    in_ = {
        'unknown_obj': object(),
    }

    with pytest.raises(TypeError):
        json.dumps(in_, cls=JSONEncoder)


def test_timezone_aware():
    in_ = {
        'timezone_aware': datetime.time(tzinfo=dateutil.tz.tzoffset(None, 9 * 60 * 60)),
    }

    with pytest.raises(ValueError):
        json.dumps(in_, cls=JSONEncoder)
