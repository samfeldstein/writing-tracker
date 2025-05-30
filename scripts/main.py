import csv

from log_date import log_date
from log_project import log_project
from log_start_time import log_start_time
from log_start_words import log_start_words
from log_end_time import log_end_time
from log_end_words import log_end_words
from calc import calc_words_today, calc_words_this_year, calc_words_all_time, calc_avg_words

today = log_date()
project = log_project()
start_time = log_start_time()
start_words = log_start_words()
end_time = log_end_time()
end_words = log_end_words()

# Calc time and words
session_time = end_time - start_time
session_words = end_words - start_words

# Format times
start_str = start_time.strftime("%H:%M")
end_str = end_time.strftime("%H:%M")
session_str = str(session_time)[:-3] # removes seconds

# Open the CSV file in append mode and add the new entry
with open("log.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([today, project, start_str, start_words, end_str, end_words, session_str,session_words])

# Calculations. Must come after the data is entered in the csv.
words_today = calc_words_today()
words_this_year = calc_words_this_year()
words_all_time = calc_words_all_time()
avg_words = calc_avg_words()

# Add words from old timesheets to all time total. Adding separate here so it doesn't fuck up avg
words_all_time = words_all_time + 79562

# Print results
spacing = 20
print("-" * 30)
print("STATS")
print(f"{'Session time:':<{spacing}}{session_str:>6}")
print(f"{'Session words:':<{spacing}}{session_words:>6}")
print(f"{'Words today:':<{spacing}}{words_today:>6}")
print(f"{'Avg/day:':<{spacing}}{avg_words:>6}")
print(f"{'Words this year:':<{spacing}}{words_this_year:>6}")
print(f"{'Words all time:':<{spacing}}{words_all_time:>6}")
print("-" * 30)