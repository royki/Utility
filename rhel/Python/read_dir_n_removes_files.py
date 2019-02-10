import os
from fnmatch import fnmatch

dir_path = 'D:\API_Deploy'
print (dir_path)
file_pattern = "report"
file_count = 0


for path, subdirs, files in os.walk(dir_path):
    for file in files:  
        # if file.endswith(file_pattern):
        if file.startswith(file_pattern):  	
        #if fnmatch(file, file_pattern):
            print os.path.join(file)
            os.remove(os.path.join(path, file))
			
			
'''

def scandirs(path):
    for root, dirs, files in os.walk(path):
        for currentFile in files:
            print "processing file: " + currentFile
            exts = ('.log', '.rex')
            if any(currentFile.lower().endswith(ext) for ext in exts):
                os.remove(os.path.join(root, currentFile))


scandirs('D:/MSX_PDT/MSX_REGRESSION')

'''