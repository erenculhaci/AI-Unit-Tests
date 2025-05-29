# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

import re
from datetime import datetime

def valid_date(date_str):
    if not isinstance(date_str, str):
        raise AttributeError("Input must be a string.")

    # Ensure strict format MM-DD-YYYY with two digits for MM and DD, and four for YYYY
    if not re.match(r"^\d{2}-\d{2}-\d{4}$", date_str):
        return False

    try:
        datetime.strptime(date_str, "%m-%d-%Y")
        return True
    except ValueError:
        return False
