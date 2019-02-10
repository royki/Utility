import errno
import os,time
from datetime import datetime

import shutil


def copy_and_overwrite(from_path, to_path):
    if os.path.exists(to_path):
        shutil.rmtree(to_path)
    shutil.copytree(from_path, to_path)

def fcount(path):
  count = 0
  for f in os.listdir(path):
    child = os.path.join(path, f)
    if os.path.isdir(child):
      #child_count = fcount(child, map)
      #count += child_count + 1 # unless include self
      count += 1
  #map[path] = count
  return count

def oldestpath(path):
  min = 0;
  deldir = ''
  for r,d,f in os.walk(path):
    for dir in d:
        a = os.stat(os.path.join(r,dir))
	temptime = datetime.strptime(time.ctime(a.st_ctime), "%a %b %d %H:%M:%S %Y")
	#print temptime
	if min == 0 or min > temptime:
		min = temptime
		deldir = dir

        #if now-numdays > timestamp:

  print deldir
  try:
    shutil.rmtree(os.path.join(path,deldir))
  except Exception,e:
    print e
    pass

path = "D:/"
if not os.path.exists(path):
  os.makedirs(path)
filecount =  fcount(path)
mydir = os.path.join(path, datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))

if(filecount > 6):
  oldestpath(path)

#try:
#  os.mkdir(mydir)
#except OSError as e:
#  if e.errno != errno.EEXIST:
#     raise  # This was not a "directory exist" error..


copy_and_overwrite(r'', mydir)










