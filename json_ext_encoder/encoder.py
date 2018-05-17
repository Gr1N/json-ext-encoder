import datetime
import decimal
import enum
import json
import uuid

from json_ext_encoder import (
    duration,
    timezone,
)

__all__ = (
    'JSONEncoder',
)


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.datetime):
            r = o.isoformat()
            if o.microsecond:
                r = r[:23] + r[26:]
            if r.endswith('+00:00'):
                r = r[:-6] + 'Z'
            return r
        elif isinstance(o, datetime.date):
            return o.isoformat()
        elif isinstance(o, datetime.time):
            if timezone.is_aware(o):
                raise ValueError('JSON can\'t represent timezone-aware times.')
            r = o.isoformat()
            if o.microsecond:
                r = r[:12]
            return r
        elif isinstance(o, datetime.timedelta):
            return duration.iso_string(o)
        elif isinstance(o, (decimal.Decimal, uuid.UUID)):
            return str(o)
        elif isinstance(o, enum.Enum):
            return o.value

        return super().default(o)
