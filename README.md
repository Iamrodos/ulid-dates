# ULID Dates

A Python utility to determine ULID prefixes for date ranges.

This can be useful for querying databases or logs for ULIDs that fall within a specific time period.

## Installation

Install the package using `pip`:

```bash
pip install ulid-dates
```

Alternatively, using `uv`:

```bash
uv pip install ulid-dates
```

## Usage

```python
from datetime import datetime, timedelta
from ulid_dates import ulid_prefix_range_for_dates

start_date = datetime(2023, 1, 1)
end_date = start_date + timedelta(days=1)

start_prefix, end_prefix = ulid_prefix_range_for_dates(start_date, end_date)

print(f"ULID prefix for {start_date}: {start_prefix}")
print(f"ULID prefix for {end_date}: {end_prefix}")
```

## Development

To set up the development environment:

1. Clone the repository.
2. Create a virtual environment and activate it.
3. Install the dependencies in editable mode.

Using `pip`:
```bash
pip install -e .[dev]
```

Alternatively, using `uv`:

```bash
uv pip install -e .[dev]
```

### Running Tests

To run the tests, use `pytest`:

```bash
pytest
```
