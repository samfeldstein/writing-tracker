import csv

def log_words():
    words = input("Words: ")

    # Convert the input to an integer
    words = int(words)

    # Open the CSV file in append mode and add the new entry
    with open("log.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([words])
