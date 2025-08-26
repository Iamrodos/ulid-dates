from datetime import datetime, timedelta
from ulid_dates import ulid_prefix_range_for_dates


def test_ulid_prefix_range_for_dates():
    start_date = datetime(2023, 1, 1)
    end_date = start_date + timedelta(days=1)

    start_prefix, end_prefix = ulid_prefix_range_for_dates(start_date, end_date)
    assert isinstance(start_prefix, str)
    assert isinstance(end_prefix, str)
    assert len(start_prefix) == 10
    assert len(end_prefix) == 10
