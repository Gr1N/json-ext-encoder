from datetime import timedelta
from typing import Tuple

__all__ = (
    'iso_string',
)


def iso_string(duration: timedelta) -> str:
    if duration < timedelta(0):
        sign = '-'
        duration *= -1
    else:
        sign = ''

    days, hours, minutes, seconds, microseconds = _get_components(duration)
    ms = f'.{microseconds:06d}' if microseconds else ''
    return f'{sign}P{days}DT{hours:02d}H{minutes:02d}M{seconds:02d}{ms}S'


def _get_components(duration: timedelta) -> Tuple[int, int, int, int, int]:
    days = duration.days
    seconds = duration.seconds
    microseconds = duration.microseconds

    minutes = seconds // 60
    seconds = seconds % 60

    hours = minutes // 60
    minutes = minutes % 60

    return days, hours, minutes, seconds, microseconds
