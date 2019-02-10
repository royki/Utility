#### Search Command

- To find the most recently modified files, sorted in the reverse order of update time (i.e., the most recently updated files first):

    - `$ find /etc -type f -printf '%TY-%Tm-%Td %TT %p\n' | sort -r`

The above command sorts files in /etc (and all its subdirectories), in the reverse order of their update time, and prints out the sorted list, along with their location and update time. If you want to examine directories as well, you can omit "-type f" option in the command.

- To search for files in /target_directory and all its sub-directories, that have been modified in the last 60 minutes:
    
    - `$ find /target_directory -type f -mmin -60`

- To search for files in /target_directory and all its sub-directories, that have been modified in the last 2 days:

    - `$ find /target_directory -type f -mtime -2`

- To search for files in /target_directory and all its sub-directories no more than 3 levels deep, that have been modified in the last 2 days:

    - `$ find /target_directory -type f -mtime -2 -depth -3`

- You can also specify the range of update time. To search for files in /target_directory and all its sub-directories, that have been modified in the last 7 days, but not in the last 3 days:

    - `$ find /target_directory -type f -mtime -7 ! -mtime -3`

- To search for files in /target_directory (and all its sub-directories) that have been modified in the last 60 minutes, and print out their file attributes:

    - `$ find /target_directory -type f -mmin -60 -exec ls -al {} \;``

- Alternatively, you can use xargs command to achieve the same thing:

    - `$ find /target_directory -type f -mmin -60 | xargs ls -l`


- UserList

    - `cat /etc/passwd`
    - `more /etc/passwd`
    - `less /etc/passwd`
    - `awk -F':' '{print $1}' /etc/passwd`


** A Note About System and General Users- `grep "^UID_MIN" /etc/login.defs`


