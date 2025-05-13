import csv
from datetime import date

def calc():
    # Open the CSV file and read the data
    with open("log.csv", "r") as file:
        reader = csv.reader(file)
        rows = list(reader)

    # Skip the header row
    data = rows[1:]

    # Calculate words written today
    today = date.today().isoformat()
    # Sum all entries for today
    words_today = 0
    for row in data:
        # strip whitespace and compare to today’s date
        if row[0].strip() == today:
            words_today += int(row[-1])

    # Calculate words written this year
    current_year = date.today().year
    # Calculate words written this year
    words_this_year = sum(
        int(row[-1])
        for row in data
        if row[0].startswith(str(current_year))
    )

    # Calculate words written all time
    words_all_time = sum(int(row[-1]) for row in data)

    # Calculate average words per logged day
    avg_day = round(words_all_time / len({row[0].strip() for row in data})) if data else 0

    # Print results
    print("-" * 30)
    print(f"{'Day:':<10}{words_today:>6}")
    print(f"{'Avg/day:':<10}{avg_day:>6}")
    print(f"{'Year:':<10}{words_this_year:>6}")
    print(f"{'All:':<10}{words_all_time:>6}")
    print("-" * 30)
