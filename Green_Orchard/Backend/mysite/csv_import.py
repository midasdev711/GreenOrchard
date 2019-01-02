import csv, os
from pathlib import Path
from expenses.models import (~class here)


def upload_file():
    home = str(Path.home())

    # Change this first os call after this file is moved to proper place
    # os.chdir(home) #Obsolete if getting home directory

    # For first time use of app:
    if not os.path.isdir(home+'/.Green_Orchard_Banks/'):
        os.mkdir(home+'/.Green_Orchard_Banks/')

    # Set directory to where this csv file will go
    path = home + '/.Green_Orchard_Banks/{}'
    try:
        # note: 'bank' has to come from the file's properties,
        # from the 'where from' data
        x
        bank_dir = bank.replace(' ', '_')
        os.chdir(path.format(bank_dir))
    except NameError: # If there is no 'bank' variable
        print("Name of bank isn't given. Try again")
    except FileNotFoundError:
        # Adds underscore for banks with more than one word
        new_dir = bank.replace(' ', '_')
        os.mkdir('.Green_Orchard_Banks/' + new_dir)
        os.chdir(path.format(new_dir))

    # Getting contents of csv file, line by line
    with open(csv_file) as csvfile:
        reader = csv.DictReader(csvfile)

    # Adding content from each line into the database
    for row in reader:
        p = (~class)(~attributes on class)
