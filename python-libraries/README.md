# CLI Game Data Entry App

This project is a simple command-line data curation application written in Python. It allows users to enter video game data in the terminal, review their entries, confirm whether the information is correct, and then save the confirmed data to a JSON file.

## What This Script Does

This script:

- uses the **Rich** library to display formatted text and a sample data table in the terminal
- asks the user to enter new video game data
- allows the user to review each entry before saving it
- lets the user re-enter the data if something is incorrect
- supports entering multiple data entries
- saves all confirmed entries to a file called `game_data.json`
- prints the full file path after the data is saved

## Topic

The topic of this CLI application is **video game data**.

Each entry includes the following fields:

- `title`
- `release_year`
- `genre`
- `platform`

This project connects to cultural data because video games are a form of media and popular culture, and this script can be used to manually build a small structured dataset about games.

## File Included

This project includes:

- `cli_data_entry.py` — the main Python script
- `game_data.json` — the output file generated after running the script
- `README.md` — this file

## Requirements

Before running the script, make sure Python is installed on your computer.

You also need to install the Rich library.

## Installation

Install Rich with: pip install rich

If that does not work, try: pip3 install rich

How to Run the Script

Open your terminal, go to the python-libraries folder, and run: python cli_data_entry.py

If your system uses Python 3, run: python3 cli_data_entry.py

## How to Use the Script

When the script runs:

it first displays example video game data in a formatted table

it then asks the user to enter a new game

the user types in:

game title

release year

genre

platform

the script shows the entered data back to the user

the user confirms whether the data is correct by typing y or n

if the user types n, the script asks them to re-enter that entry

if the user types y, the entry is saved in memory

the script asks whether the user wants to add another entry

when the user finishes, all confirmed entries are saved to game_data.json

the script prints the full file path so the user can find the saved file

## Example Interaction
Please enter a new game entry.
Enter the game title: Hollow Knight
Enter the release year: 2017
Enter the genre: Metroidvania
Enter the platform: PC

You entered the following data:
Title: Hollow Knight
Release Year: 2017
Genre: Metroidvania
Platform: PC

Is this information correct? (y/n): y
Do you want to add another entry? (y/n): n

## Output
After the script finishes, it creates a file named: game_data.json

The data is saved in JSON format. A sample output might look like this:

[
    {
        "title": "Hollow Knight",
        "release_year": "2017",
        "genre": "Metroidvania",
        "platform": "PC"
    }
]

Why I Chose JSON

I chose JSON because it is:

easy to read

easy to write in Python

structured and organized

useful for future data analysis or reuse

Skills Used

This project uses several Python concepts:

importing libraries

using third-party packages

creating functions

using loops

using conditionals

collecting user input

storing data in dictionaries and lists

writing data to a JSON file

working with file paths

Reflection

This project helped me understand how command-line applications can be used for manual data curation. It also showed how user input, loops, and file writing can work together in a simple data collection workflow. Using Rich made the application easier to read and more visually organized in the terminal.

Author

Raymond Lu

Course

IS 310 – Computing in the Humanities