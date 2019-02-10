import os
from os import listdir

path =  "D:\API_Deploy\OPS\Application"
filenames = os.listdir(path)

filelist = [ f for f in os.listdir(path) if f.endswith(".txt") ]
for f in filelist:	
	os.remove(f)