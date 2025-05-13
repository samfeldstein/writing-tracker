import csv
from log_date import log_date
from log_project import log_project
from log_start_time import log_start_time
from log_start_words import log_start_words
from log_end_time import log_end_time
from log_end_words import log_end_words

today = log_date()
project = log_project()
start_time = log_start_time()
start_words = log_start_words()
end_time = log_end_time()
end_words = log_end_words()

# Open the CSV file in append mode and add the new entry
with open("log.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([today, project, start_time, start_words, end_time, end_words])