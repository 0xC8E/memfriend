# Memfriend
Simple in-memory database that uses a protocol similar to the REDIS protocol.

## Installing
1. Set up [`poetry`](https://python-poetry.org/) for dependency management.
2. Run `poetry install`.

## Running
1. Run `./bin/start.sh` with the input file of your choice (or leave it empty for direct stdin access).

## Testing
1. Run `./bin/test.sh` to run the test suite.

## Review
1. The pattern that I used for transactions in data commands is not my favorite - I'd've liked to do something cleaner (like a decorator, perhaps), but I decided to get the feature done before being fancy.
2. The tests for transactions are a bit lacking. I could only do some quick and dirty testing, so I wouldn't be surprised if something isn't quite right.

This was a fun exercise!


Built by `jc@fractalreef.com` for `Friendbuy`.