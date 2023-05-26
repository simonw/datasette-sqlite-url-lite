from datasette_sqlite_url_lite import (
    url_valid,
    url_scheme,
    url_host,
    url_path,
    url_fragment,
)
import sqlite3
import pytest


@pytest.fixture
def conn():
    return sqlite3.connect(":memory:")


def test_url_valid(conn):
    conn.create_function("url_valid", 1, url_valid)
    cursor = conn.cursor()

    cursor.execute("SELECT url_valid('https://sqlite.org')")
    assert cursor.fetchone()[0]

    cursor.execute("SELECT url_valid('not_a_url')")
    assert not cursor.fetchone()[0]


def test_url_scheme(conn):
    conn.create_function("url_scheme", 1, url_scheme)
    cursor = conn.cursor()

    cursor.execute("SELECT url_scheme('https://www.sqlite.org/vtab.html#usage')")
    assert cursor.fetchone()[0] == "https"

    cursor.execute("SELECT url_scheme('ftp://example.com')")
    assert cursor.fetchone()[0] == "ftp"


def test_url_host(conn):
    conn.create_function("url_host", 1, url_host)
    cursor = conn.cursor()

    cursor.execute("SELECT url_host('https://www.sqlite.org/vtab.html#usage')")
    assert cursor.fetchone()[0] == "www.sqlite.org"

    cursor.execute("SELECT url_host('https://example.com')")
    assert cursor.fetchone()[0] == "example.com"


def test_url_path(conn):
    conn.create_function("url_path", 1, url_path)
    cursor = conn.cursor()

    cursor.execute("SELECT url_path('https://www.sqlite.org/vtab.html#usage')")
    assert cursor.fetchone()[0] == "/vtab.html"

    cursor.execute("SELECT url_path('https://example.com/test')")
    assert cursor.fetchone()[0] == "/test"


def test_url_fragment(conn):
    conn.create_function("url_fragment", 1, url_fragment)
    cursor = conn.cursor()

    cursor.execute("SELECT url_fragment('https://www.sqlite.org/vtab.html#usage')")
    assert cursor.fetchone()[0] == "usage"

    cursor.execute("SELECT url_fragment('https://example.com/test#fragment')")
    assert cursor.fetchone()[0] == "fragment"
