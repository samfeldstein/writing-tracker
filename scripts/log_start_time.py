from datetime import datetime

def log_start_time():
    while True:
        s = input("Start time (HHMM): ")
        try:
            return datetime.strptime(s, "%H%M")
        except ValueError:
            print("Invalid. Use HHMM, e.g. 0930.")