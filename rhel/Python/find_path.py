import os
from fnmatch import fnmatch

dir_path = ''
print (dir_path)

file_pattern = ".txt"
file_count = 0

for path, subdirs, files in os.walk(dir_path):
    for file in files:
        if file.endswith(file_pattern):
        #if fnmatch(file, file_pattern):
            print os.path.join(file)