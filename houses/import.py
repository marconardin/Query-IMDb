import csv
from sys import argv, exit
from cs50 import SQL

import pdb

def main(argv):
    if len(argv) != 2:
        print("Usage: python import.py characters.csv")
        exit(1)

    csv_file = argv[1]

    # assume csv exists and has columns: name, house, and birth
    with open(csv_file, "r") as f:
        reader = csv.DictReader(f)
        characters = [line for line in reader]

    # import database
    db = SQL("sqlite:///students.db")

    for character in characters:
        names = character['name'].split()
        if len(names) == 3: # contains middle name
            first, middle, last = names
        else:
            first, last = names
            middle = None
        house = character['house']
        birth = character['birth']

        db.execute(f"""INSERT INTO students (first, middle, last, house, birth)
                    VALUES ('{first}', '{middle}', '{last}', '{house}', '{birth}');
                    """)


main(argv)