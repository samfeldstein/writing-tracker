from datetime import datetime

def log_start_time():
    while True:
        try:
            return datetime.strptime(
                input("Start time (HHMM): "), "%H%M"
            ).time().isoformat(timespec="minutes")
        except ValueError:
            print("Invalid format. Please use HHMM (e.g. 0930).")
