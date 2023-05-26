# datasette-sqlite-url-lite

[![PyPI](https://img.shields.io/pypi/v/datasette-sqlite-url-lite.svg)](https://pypi.org/project/datasette-sqlite-url-lite/)
[![Changelog](https://img.shields.io/github/v/release/simonw/datasette-sqlite-url-lite?include_prereleases&label=changelog)](https://github.com/simonw/datasette-sqlite-url-lite/releases)
[![Tests](https://github.com/simonw/datasette-sqlite-url-lite/workflows/Test/badge.svg)](https://github.com/simonw/datasette-sqlite-url-lite/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/simonw/datasette-sqlite-url-lite/blob/main/LICENSE)

A pure Python alternative to [sqlite-url](https://github.com/asg017/sqlite-url) ready to be used in [Datasette Lite](https://lite.datasette.io/)

## Installation

Install this plugin in the same environment as Datasette.

    datasette install datasette-sqlite-url-lite

Or add it to Datasette Lite with `https://lite.datasette.io/?install=datasette-sqlite-url-lite`.

## Usage

This plugin adds the following SQL functions:

```sql
select url_valid('https://sqlite.org'); -- 1
select url_scheme('https://www.sqlite.org/vtab.html#usage'); -- 'https'
select url_host('https://www.sqlite.org/vtab.html#usage'); -- 'www.sqlite.org'
select url_path('https://www.sqlite.org/vtab.html#usage'); -- '/vtab.html'
select url_fragment('https://www.sqlite.org/vtab.html#usage'); -- 'usage'
```

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:

    cd datasette-sqlite-url-lite
    python3 -m venv venv
    source venv/bin/activate

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest
