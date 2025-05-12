# 🖋️ The Simplest Writing Tracker

A simple terminal-based application to track my writing. It comprises a `log.csv` file, two Python scripts, and a shell script.

The first Python script is called `entry.py`. It prompts you to enter the number of words you wrote. It logs that number in `log.csv` along with the current date.

The second Python script is called `calc.py`. It calculates words written today, average words per day, words written this year, and words written all time, and prints those numbers to the terminal.

The shell script (`log-writing.zsh`) runs both python scripts. When you run `~/path/to/script/log-writing.zsh` in your terminal, it prompts you to enter your words written and immediately prints your stats.
