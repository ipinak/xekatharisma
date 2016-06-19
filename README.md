# Xekatharisma Scrapper

It's an python module that scrapes data from a number of pre-defined web pages.
It implements specific crawlers that will work only on those sites.

# Usage

## Installation

    $ virtualenv xekatharisma.venv
    $ source xekatharisma.venv/bin/activate
    $ pip install -e .

The above installs the modules in your current environment.

## Tests

To run the tests you need to use `py.test`.

    $ pip install -r requirements.dev.txt
    $ py.test -s tests/ -n 2

With the above commands you will install the development dependencies, i.e.
the normal dependencies of this module plus a few other eggs that are required
for testing such as `py.test` and `xdist`. `xdist` is a plugin for `py.test`
which allows you running tests in parallel and `py.test` for actually running
the tests.

# License

BSD License
