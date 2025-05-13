# 🖋️ The Simplest Writing Tracker

A simple terminal-based application to track my writing. It comprises a `log.csv` and three Python scripts.

The first Python script is `add_words.py`. It contains a function that prompts you to enter the number of words you wrote. It logs that number in `log.csv` along with the current date.

The second Python script is `calc.py`. It contains a function that calculates words written today, average words per day, words written this year, and words written all time, and prints those numbers to the terminal.

The last script is `main.py`. It runs the other two scripts. When you run `python scripts/main.py`, it prompts you to enter your words written and immediately prints your stats.
