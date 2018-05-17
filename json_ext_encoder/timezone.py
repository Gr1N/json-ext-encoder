from datetime import (
    datetime,
    time,
)
from typing import Union

__all__ = (
    'is_aware',
)


def is_aware(value: Union[datetime, time]) -> bool:
    """
    Determine if a given datetime.datetime or datetime.time is aware.

    The concept is defined in Python's docs:
    http://docs.python.org/library/datetime.html#datetime.tzinfo

    Assuming value.tzinfo is either None or a proper datetime.tzinfo,
    value.utcoffset() implements the appropriate logic.
    """
    return value.utcoffset() is not None
