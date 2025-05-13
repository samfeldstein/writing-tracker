from datetime import datetime

def log_end_time():
    while True:
        s = input("End time (HHMM): ")
        try:
            return datetime.strptime(s, "%H%M")
        except ValueError:
            print("Invalid. Use HHMM, e.g. 1730.")
