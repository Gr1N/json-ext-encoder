# json-ext-encoder [![Build Status](https://travis-ci.org/Gr1N/json-ext-encoder.svg?branch=master)](https://travis-ci.org/Gr1N/json-ext-encoder) [![codecov](https://codecov.io/gh/Gr1N/json-ext-encoder/branch/master/graph/badge.svg)](https://codecov.io/gh/Gr1N/json-ext-encoder)

Extended JSON encoder for Python data structures.

A subclass of [JSONEncoder](https://docs.python.org/3/library/json.html#json.JSONEncoder), it handles these additional types:

- `datetime.datetime` — a string of the form `YYYY-MM-DDTHH:mm:ss.sssZ` or `YYYY-MM-DDTHH:mm:ss.sss+HH:MM` as defined in [ECMA-262](https://www.ecma-international.org/ecma-262/5.1/#sec-15.9.1.15).
- `datetime.date` — a string of the form `YYYY-MM-DD` as defined in [ECMA-262](https://www.ecma-international.org/ecma-262/5.1/#sec-15.9.1.15).
- `datetime.time` — a string of the form `HH:MM:ss.sss` as defined in [ECMA-262](https://www.ecma-international.org/ecma-262/5.1/#sec-15.9.1.15).
- `datetime.timedelta` - a string representing a duration as defined in [ISO-8601](https://www.iso.org/iso-8601-date-and-time-format.html). For example, `timedelta(days=1, hours=2, seconds=3.4)` is represented as `P1DT02H00M03.400000S`.
- `decimal.Decimal`, `uuid.UUID` — a string representation of the object.
- `enum.Enum` — a `.value` property of enum member.

## Installation

    $ pip install json-ext-encoder

## Usage

    import json
    from json_ext_encoder import JSONEncoder

    json.dumps({...}, cls=JSONEncoder)

## Testing and linting

For testing and linting install [tox](http://tox.readthedocs.io):

    $ pip install tox

...and run:

    $ tox

## License

`json-ext-encoder` is licensed under the MIT license. See the license file for details.
