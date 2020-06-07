import shutil
import os

source = 'C:/Users/Jared/Desktop/Folder A/'

destination = 'C:/Users/Jared/Desktop/Folder B/'
files = os.listdir(source)

for i in files:
    shutil.move(source+i, destination)
