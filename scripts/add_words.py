import csv
from datetime import date

def add_words():
    project = input("Project: ")
    start = input("Start time (HH:MM): ")
    end   = input("End   time (HH:MM): ")
    words = input("Words: ")

    # Convert the input to an integer
    words = int(words)

    # Get today's date in YYYY-MM-DD format
    today = date.today().isoformat()

    # Open the CSV file in append mode and add the new entry
    with open("log.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([today, project, start, end, words])
