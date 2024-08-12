# Illumio Technical Assignment

## Language Selection
Python

Note: While the tests require `pytest`, the program itself can be run without any external dependencies.

## Run
```
docker compose up --build
```
This will run the application.

To inspect the outputs run (for reference see [docs.docker.com/reference/cli/docker/container/exec](https://docs.docker.com/reference/cli/docker/container/exec/)):
```
docker exec -it illumio sh
```
The outputs will be found in the `/outputs` directory. If they are missing run `poetry run python3 src/app.py`

## Tests
To run the tests inspect the Docker container and run:
```
poetry run pytest
```

Tests include:
- Large log files (up to 10 MB)
- Large maps (up to 10000 mappings)
- Test different forms of log records (i.e. accepted/rejected traffic, IPv6 Traffic, etc.)
- Module unit testing

## Assumptions
- Input data is well-formed (consistent formatting and fields with respect to [docs.aws.amazon.com/vpc/latest/userguide/flow-log-records.html](https://docs.aws.amazon.com/vpc/latest/userguide/flow-log-records.html))
- Valid protocol decimals found in [iana.org/assignments/protocol-numbers/protocol-numbers.xhtml](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml)
