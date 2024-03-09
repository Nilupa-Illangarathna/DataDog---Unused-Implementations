# Datadog One-Way Socket Communication

This project includes two distinct scripts for working with Datadog services. The first script (`datadog_query.py`) performs a one-way socket communication to query Datadog logs using the Datadog API, while the second script (`datadog_logging.py`) generates fake data and sends logs to Datadog using the Datadog API.

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/downloads/release)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE.md)
[![Issues](https://img.shields.io/github/issues/YourUsername/YourRepository.svg)](https://github.com/YourUsername/YourRepository/issues)


## datadog_query.py

### Prerequisites
- Datadog API key
- Datadog Application key

### Usage

1. Set your Datadog API key and Application key in the `api_key` and `app_key` variables.
2. Customize the `query` variable to define the logs query.
3. Run the script (`datadog_query.py`).

The script will send a POST request to Datadog API and print the response, providing insights into the queried logs.

## datadog_logging.py

### Prerequisites
- Datadog API key
- Datadog Application key
- Datadog Site (e.g., "US" or "EU")

### Usage

1. Set your Datadog API key, Application key, and Site in the environment variables (`DD_API_KEY`, `DD_APP_KEY`, `DD_SITE`).
2. Customize the environment variable `ENV` to specify the environment (e.g., "DEV").
3. Run the script (`datadog_logging.py`).

The script generates fake data using the Faker library and sends logs at different levels (info, warning, error) to Datadog.

## Dependencies

- [Requests](https://docs.python-requests.org/en/latest/)
- [Datadog API Client](https://github.com/DataDog/datadog-api-client-python)
- [Faker](https://faker.readthedocs.io/en/master/)

### Installation

```bash
pip install requests datadog-api-client faker
