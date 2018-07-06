# json-ext-encoder [![Build Status](https://travis-ci.org/Gr1N/json-ext-encoder.svg?branch=master)](https://travis-ci.org/Gr1N/json-ext-encoder) [![codecov](https://codecov.io/gh/Gr1N/json-ext-encoder/branch/master/graph/badge.svg)](https://codecov.io/gh/Gr1N/json-ext-encoder) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

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

## Contributing

To work on the `json-ext-encoder` codebase, you'll want to clone the project locally and install the required dependencies via [poetry](https://poetry.eustace.io):

    $ git clone git@github.com:Gr1N/json-ext-encoder.git
    $ poetry install

To run tests and linters use command below:

    $ poetry run tox

If you want to run only tests or linters you can explicitly specify which test environment you want to run, e.g.:

    $ poetry run tox -e py37-tests

## License

`json-ext-encoder` is licensed under the MIT license. See the license file for details.
