from datasette import hookimpl
from urllib.parse import urlparse, ParseResult


def url_valid(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


def url_scheme(url):
    try:
        return urlparse(url).scheme
    except ValueError:
        return None


def url_host(url):
    try:
        return urlparse(url).netloc
    except ValueError:
        return None


def url_path(url):
    try:
        return urlparse(url).path
    except ValueError:
        return None


def url_fragment(url):
    try:
        return urlparse(url).fragment
    except ValueError:
        return None


@hookimpl
def prepare_connection(conn):
    conn.create_function("url_valid", 1, url_valid)
    conn.create_function("url_scheme", 1, url_scheme)
    conn.create_function("url_host", 1, url_host)
    conn.create_function("url_path", 1, url_path)
    conn.create_function("url_fragment", 1, url_fragment)
