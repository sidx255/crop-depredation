import os
  
  
# Directory to be scanned
path = '/home/pi'
  
# Scan the directiory and get
# an iterator of os.DirEntry objets
# corresponding to entries in it 
# using os.scandir() method
obj = os.scandir()
  
# List all files and diretories 
# in the specified path
print("Files and Directories in '% s':" % path)
for entry in obj :
    if entry.is_dir() or entry.is_file():
        print(entry.name)
  
  
# entry.is_file() will check
# if entry is a file or not and
# entry.is_dir() method will
# check if entry is a
# directory or not. 
  
  
# To Close the iterator and
# free acquired resources
# use scandir.close() method
obj.close()
