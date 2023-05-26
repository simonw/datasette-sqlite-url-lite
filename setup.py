from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="datasette-sqlite-url-lite",
    description="A pure Python alternative to sqlite-url ready to be used in Datasette Lite",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    url="https://github.com/simonw/datasette-sqlite-url-lite",
    project_urls={
        "Issues": "https://github.com/simonw/datasette-sqlite-url-lite/issues",
        "CI": "https://github.com/simonw/datasette-sqlite-url-lite/actions",
        "Changelog": "https://github.com/simonw/datasette-sqlite-url-lite/releases",
    },
    license="Apache License, Version 2.0",
    classifiers=[
        "Framework :: Datasette",
        "License :: OSI Approved :: Apache Software License",
    ],
    version=VERSION,
    packages=["datasette_sqlite_url_lite"],
    entry_points={"datasette": ["sqlite_url_lite = datasette_sqlite_url_lite"]},
    install_requires=["datasette"],
    extras_require={"test": ["pytest", "pytest-asyncio"]},
    python_requires=">=3.7",
)
