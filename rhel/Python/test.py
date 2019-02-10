import os
import glob
import shutil

filenames = os.listdir("Path_of_the_directory")
types = ('*.txt', '*.html', '*.css') # glob not working, need to fix


filelist = [ f for f in os.listdir(".") if f.endswith(".txt") ]
for f in filelist:
	print(f)
	os.remove(f)

for filename in filenames:
	if filename.startswith("TEST-"):
		print(filename)
		os.remove(filename)

for filename in filenames:
	if filename.endswith(".css"):
		print(filename)
		os.remove(filename)

for filename in filenames:
	if filename.endswith(".html"):
		print(filename)
		os.remove(filename)

if os.path.exists("d:\Userfiles\kroy\Desktop\Scripts"):
	# remove if exists
	shutil.rmtree(path)
	remove_folder(test)