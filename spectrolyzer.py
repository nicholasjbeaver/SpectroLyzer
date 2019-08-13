import pandas as pd
import numpy as np
import os


# Search for csv files in data/
# make a list of files in data directory

filenames = []

for files in os.listdir('/Users/nick/Coding/SpectroLyzer/SpectroLyzer/data'):
  filenames.append(files)

print(filenames)

while True:
    chosenFile = input('choose a file from the list above (type response):   ')
    if chosenFile in filenames:
        print(chosenFile)
        break
    else:
        print('the selected file is not in the data directory, please try again')



# based on csv chosen, make a dataframe

df=pd.read_csv(chosenFile)

print(df)

# function to display table at maximum wavelength

# filter by sample if user chooses to

# ask user to insert a specific wavelength to look at (or no)

# ask user to insert a wavelength range to find a max (or no)

# display raw data if prompted
