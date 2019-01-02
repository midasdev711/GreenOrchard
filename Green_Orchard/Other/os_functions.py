import os

def move_files():
    # Move dependant on which bank, and name of file
    os.rename("/Downloads/{}.csv", "/Documents/Capstone/Bank_Files/{}/{}.csv")
