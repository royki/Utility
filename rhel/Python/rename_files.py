import os
from os import rename, listdir

path =  os.getcwd()
filenames = os.listdir(path)
prefix = "PDT_"
suffix = "_PDT"

for filename in filenames:
    if filename.startswith(prefix):
        rename(filename, filename.replace(prefix, "APP_"))



for filename in filenames:
    if filename.endswith(suffix):
        rename(filename, filename.replace(suffix, "_DEV"))
