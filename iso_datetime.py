import re
from datetime import datetime


def parse(iso_representation):
    match = _regex.fullmatch(iso_representation)

    if not match:
        raise ValueError('Illegal ISO8601 timestamp: ' + iso_representation)

    year = int(match.group(1))
    month = int(match.group(2))
    day = int(match.group(3))
    hour = int(match.group(4))
    minute = int(match.group(5))
    second = int(match.group(6)) if match.lastindex >= 6 else 0
    microsecond = _parse_microseconds(match.group(7)) if match.lastindex >= 7 else 0

    return datetime(
        year,
        month,
        day,
        hour,
        minute,
        second,
        microsecond)


def _parse_microseconds(fraction_string):
    num_digits = len(fraction_string)
    if num_digits > 6:
        raise ValueError('Illegal microsecond value: ' + str(fraction_string))
    missing_digits = 6 - num_digits
    multiplier = 10 ** missing_digits
    return int(fraction_string) * multiplier


_regex = re.compile(r'(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2})(?::(\d{2})(?:.(\d+))?)?')
