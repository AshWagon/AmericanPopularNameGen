import os
import sys
import random

# Detects if the program is running as an EXE
if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.dirname(os.path.abspath(__file__))

first_name_folder = os.path.join(base_path, 'popularNamesByYear')
surname_file = os.path.join(base_path, 'surnames', 'surnames.txt')

# Load lastnames
try:
    with open(surname_file, 'r', encoding='utf-8') as f:
        surnames = [line.strip() for line in f if line.strip()]
except FileNotFoundError:
    print("Surname doesn't exist! Is your file corrupted?")
    sys.exit(1)

if not surnames:
    print("Surnames is empty!")
    sys.exit(1)

def format_surname(surname):
    parts = surname.lower().split(' ')
    return ' '.join(part.capitalize() for part in parts)

print("=== American Names Generator made by AshWagon of the Collections of OCs Discord Server ===")
print("Type exit at any point to quit the program.\n")

while True:
    # Ask for the gender
    while True:
        gender = input("Enter gender (MUST BE male/female): ").strip().lower()
        if gender == "exit":
            print("Bye!")
            sys.exit(0)
        if gender in ("male", "female"):
            break
        print("Gender is invalid. (No, this ain't a political statement.)")

    # Ask for the year
    while True:
        year = input("Enter year (1995-2024): ").strip()
        if year.lower() == "exit":
            print("Bye!")
            sys.exit(0)
        first_name_file = os.path.join(first_name_folder, f"{year}_{gender}.txt")
        if os.path.isfile(first_name_file):
            break
        print(f"No data for {gender} names in {year} The range is 1995-2024.")

    # Load first names
    with open(first_name_file, 'r', encoding='utf-8') as f:
        first_names = [line.strip() for line in f if line.strip()]

    if not first_names:
        print(f"Error: {first_name_file} is empty.")
        continue

    # Generate a random full name
    first_name = random.choice(first_names)
    surname = format_surname(random.choice(surnames))
    full_name = f"{first_name} {surname}"

    print(f"Your random name is...: {full_name} congrats on the baby!\n")
