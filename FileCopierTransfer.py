import shutil
import os

source = 'C:/Users/Jared/Desktop/Editor/'

destination = 'C:/Users/Jared/Desktop/Finalized/'
files = os.listdir(source)

for i in files:
    shutil.copy(source+i, destination)
    os.stat(path)
    
    
   
  
