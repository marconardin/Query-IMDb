from sys import argv, exit
from cs50 import SQL

import pdb

def main(argv):
    if len(argv) != 2:
        print("Usage: python roster.py hogwarts_house")
        exit(1)

    hog_house = argv[1]

    # import database
    db = SQL("sqlite:///students.db")

    house_order = \
    db.execute(f"""SELECT first, middle, last, birth
                   FROM students
                   WHERE house LIKE "{hog_house}"
                   ORDER BY last, first
                """)

    for person in house_order:
        print_string = ' '.join((person['first'],
                                 person['last'] + ',',
                                 'born',
                                 str(person['birth'])
                                ))
        if person['middle'] != 'None':
            print_string = print_string.split()
            print_string.insert(1, person['middle'])
            print_string = ' '.join(print_string)
        print(print_string)


main(argv)