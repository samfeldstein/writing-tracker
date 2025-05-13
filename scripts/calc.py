import csv
from datetime import date

def _read_rows():
    with open("log.csv", newline="") as f:
        rows = list(csv.reader(f))
    # Skip the header row (first line) and any blank lines
    return [r for r in rows[1:] if r]

def calc_words_today():
    today = date.today().isoformat()
    rows = _read_rows()
    return sum(
        int(r[-1])
        for r in rows
        if r[0] == today
    )

def calc_words_all_time():
    rows = _read_rows()
    return sum(int(r[-1]) for r in rows)

def calc_words_this_year():
    year = str(date.today().year)
    rows = _read_rows()
    return sum(
        int(r[-1])
        for r in rows
        if r[0].startswith(year)
    )

def calc_avg_words():
    rows = _read_rows()
    unique_days = {r[0] for r in rows}
    total = calc_words_all_time()
    return round(total / len(unique_days)) if unique_days else 0
