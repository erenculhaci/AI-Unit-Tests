def valid_date(date_str):
    """
    Returns True if the input string is a valid date in the format MM-DD-YYYY,
    and False otherwise.

    Rules:
    - The string must be in the exact format MM-DD-YYYY
    - MM must be between 01 and 12
    - DD must be a valid day for the given month, accounting for leap years
    - YYYY must be between 0001 and 9999
    - Separators must be hyphens only
    - The input must not contain letters, whitespace, or extra symbols

    Args:
        date_str: A string representing a date

    Returns:
        bool: True if valid date, False otherwise

    Raises:
        AttributeError: If the input is not a string
    """
    # Check if input is a string
    if not isinstance(date_str, str):
        raise AttributeError("Input must be a string")

    # Check if string is empty
    if not date_str:
        return False

    # Split by hyphen and check if we have exactly 3 parts
    parts = date_str.split('-')
    if len(parts) != 3:
        return False

    month_str, day_str, year_str = parts

    # Check if all parts have correct length
    if len(month_str) != 2 or len(day_str) != 2 or len(year_str) != 4:
        return False

    # Check if all parts are numeric (no letters, spaces, or symbols)
    if not (month_str.isdigit() and day_str.isdigit() and year_str.isdigit()):
        return False

    # Convert to integers
    try:
        month = int(month_str)
        day = int(day_str)
        year = int(year_str)
    except ValueError:
        return False

    # Check year range
    if year < 1 or year > 9999:
        return False

    # Check month range
    if month < 1 or month > 12:
        return False

    # Check day range based on month
    if day < 1:
        return False

    # Days in each month (non-leap year)
    days_in_month = {
        1: 31,  # January
        2: 28,  # February (29 in leap year)
        3: 31,  # March
        4: 30,  # April
        5: 31,  # May
        6: 30,  # June
        7: 31,  # July
        8: 31,  # August
        9: 30,  # September
        10: 31,  # October
        11: 30,  # November
        12: 31  # December
    }

    # Check for leap year
    def is_leap_year(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    # Get maximum days for the month
    max_days = days_in_month[month]
    if month == 2 and is_leap_year(year):
        max_days = 29

    # Check if day is valid for the month
    if day > max_days:
        return False

    return True