import csv, os
from (~project name).models import (~class here)

# Change this first os call after this file is moved to proper place
os.chdir('../')

# Set directory to where this csv file will go
path = os.getcwd() + '/Banks/{}'
try:
    os.chdir(path.format(bank))
except NameError: # If there is no 'bank' variable
    print("Name of bank isn't given. Try again")
except FileNotFoundError:
    # Adds underscore for banks with more than one word
    new_dir = bank.replace(' ', '_')
    os.mkdir('Banks/' + new_dir)
    os.chdir(path.format(new_dir))

# Getting contents of csv file, line by line
with open(csv_file) as csvfile:
    reader = csv.DictReader(csvfile)

    # Adding content from each line into the database
    for row in reader:
        p = (~class)(~attributes on class)
        p.save()
