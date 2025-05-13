from datetime import datetime

def log_end_time():
    while True:
        try:
            return datetime.strptime(
                input("End time: "), "%H%M"
            ).time().isoformat(timespec="minutes")
        except ValueError:
            print("Invalid format. Please use HHMM (e.g. 0930).")
