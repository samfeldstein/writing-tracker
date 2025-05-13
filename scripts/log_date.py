from datetime import date

def log_date():
    # Get today's date in YYYY-MM-DD format
    today = date.today().isoformat()

    return today