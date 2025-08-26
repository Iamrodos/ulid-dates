from ulid import ULID
from datetime import datetime


def ulid_prefix_range_for_dates(start: datetime, end: datetime) -> tuple[str, str]:
    """
    Returns the time prefixes for a ULID based on the dates
    This can be used to find ULIDs in a range of time such as logs for a day or range of days.
    """
    start_time = int(start.timestamp())
    end_time = int(end.timestamp())
    # We can generate a ULID from a seed, so we can use the time to generate a prefix
    start_prefix = ULID(seed=start_time).generate()[:10]
    end_prefix = ULID(seed=end_time).generate()[:10]
    return start_prefix, end_prefix
