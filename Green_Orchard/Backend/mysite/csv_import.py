import csv, os, shutil
from pathlib import Path
from expenses.models import (~class here)


def upload_files():
    home = Path.home()
    files_list = retrieve_files(home)
    move_files(home, files_list)

    database_list = read_files(home, files_list)
    add_to_database(database_list)

    return True


def retrieve_files(home):
    # Calls to downloads folder where csv file originally is
    path = Path(str(home)+'/Downloads/')
    # path = str(Path.home()) + '/Downloads'

    files_to_move = []

    # Temporary solution
    # Finds specific csv files based on bank
    bank_matches = {
        'Capital One': ['*transaction_download*'],
        'Wells Fargo': ['*CreditCard*', '*Checking*'],
        'Discover': ['*Discover*'],
    }

    # Loops through all banks indicated
    for bank in chosen_bank:
        # this loops through list values in dict
        for query in bank_matches[bank]:
            # this adds csv files to our list
            queried_files = [(bank.replace(' ', '_'), file.replace(path, '')) for file in path.glob(query)]
            files_to_move.extend(queried_files)

    # returns list of tuples to unpack in move_files
    return files_to_move # [(Wells Fargo, 'file.csv'), (Discover, 'file.csv')]


def move_files(home, files_list):
    path_from = str(home) + '/Downloads/'

    # For first time use of app:
    if not os.path.isdir(str(home)+'/.Green_Orchard_Banks/'):
        os.mkdir(str(home)+'/.Green_Orchard_Banks/')

    path_to = str(home) + '/.Green_Orchard_Banks/{}'

    for bank, file in files_list:
        bank_folder = path_to.format(bank)
        if not os.path.isdir(bank_folder):
            os.mkdir(bank_folder)

        # move files into appropriate folder
        shutil.move(path_from + file, bank_folder)


    # # Set directory to where this csv file will go
    # path = home + '/.Green_Orchard_Banks/{}'
    # try:
    #     # note: 'bank' has to come from the file's properties,
    #     # from the 'where from' data
    #     x
    #     bank_dir = bank.replace(' ', '_')
    #     os.chdir(path.format(bank_dir))
    # except NameError: # If there is no 'bank' variable
    #     print("Name of bank isn't given. Try again")
    # except FileNotFoundError:
    #     # Adds underscore for banks with more than one word
    #     new_dir = bank.replace(' ', '_')
    #     os.mkdir('.Green_Orchard_Banks/' + new_dir)
    #     os.chdir(path.format(new_dir))

def read_files(files_list):
    file_path = str(home) + '/.Green_Orchard_Banks/{}/{}'
    database_list = []
    for bank, file in files_list:
        # Getting contents of csv file, line by line
        with open(file_path.format(bank, file)) as csvfile:
            reader = csv.reader(csvfile, delimiter=',')

            # Get each line's content in variable to compare and add
            current_file_contents = [row for row in reader]

            # # Adding content from each line into the database
            # for row in reader:
            #     print(row)

        database_list.extend(check_for_duplicates(bank, current_file_contents))

    return database_list


def check_for_duplicates(bank, current_file_contents):
    # will compare current file with last added file

    # return list if file is the first file in folder
    # use something in python that tells length of folder contents
    
    # if both files have ~4 of the same expenses on the same days
    # ignore everything until there are unique entries
    pass

def add_to_database(database_list):
    # will use ORM queries to add to postgresql
    for expense in database_list:
        # will add each individual expense
        pass


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
