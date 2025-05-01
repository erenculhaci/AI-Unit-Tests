def valid_date(date):
    """
    Validates if the given date string is in the correct format (mm-dd-yyyy)
    and represents a valid date.
    
    Args:
        date (str): The date string to validate
        
    Returns:
        bool: True if the date is valid, False otherwise
    """
    # Check if date is empty
    if not date:
        return False
    
    # Check the format
    if '-' not in date or date.count('-') != 2:
        return False
    
    # Split the date parts
    try:
        month_str, day_str, year_str = date.split('-')
    except ValueError:
        return False
    
    # Check if all parts are numeric
    if not (month_str.isdigit() and day_str.isdigit() and year_str.isdigit()):
        return False
    
    # Convert to integers
    try:
        month = int(month_str)
        day = int(day_str)
        year = int(year_str)
    except ValueError:
        return False
    
    # Check month range
    if month < 1 or month > 12:
        return False
    
    # Check day ranges based on month
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 1 <= day <= 31
    elif month in [4, 6, 9, 11]:
        return 1 <= day <= 30
    elif month == 2:
        return 1 <= day <= 29
    
    return False