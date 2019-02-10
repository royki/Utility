#### Admin/User/UserGroup

------------------------------------------------------------------
- `su -root`
    - /home

- Information of a Users
    - `/etc/passwd`
    - `user_name:password:user_ID:group_ID:comment:home_directory:shell_name`

- Information of a Password
    - `/etc/shadow` - store the password

- Information of a Group
    - `/etc/group`
    - `group_name:password:group_ID:list_of_users_in_the_group`

- Add a User
    - `useradd USER_NAME`
    - `useradd uoc`

- Delete a User
    - `userdel USER_NAME`
    - `userdel uoc`

- Add a Comment to User
    - usermod -c "Comment" USER_NAME`

- Add a Group
    - `groupadd -r GROUP_NAME`
    - `groupadd -r projectX`
    - `groupadd -r projectY`

- Add a User to a Group
    - `usermod -G GROUP_NAME USER_NAME`
    - `usermod -G projectX uoc`
    - `usermod -G projectX, projectY uoc`

- Give the root previlages to an existing user
    - `usermod -a -G sudo USER_NAME`

- File Permissions (Modes) 
    - Separate Permissions for : User, Group, Other
    - `ls -l` 
    - `-rwxr-xr--`

------------------------
- Only root & owner can change the mod
    - Changing File Permissions
    - `Symbolic Modes`
    - `chmod g+w filename`
    - `chmod ug=rw filename `

- Binary Number/Raw Modes
    - chmod 754 filename   
    - 754 ugo (user, group, other)
    - `-rwxr-xr--`
    - `111101100-`
 
 - Directory Modes
    - `rwx` --> full access
    - `r-x` -> limited access (enter & read)
    - `---` --> no access

- Normal User be a Admin of a Group
    - `gpasswd -A user_name project_name [-A -> admin for the group]`
    - `gpasswd -A uoc projectX`
    - for the user uoc to add a user in the group
        - `gpasswd -a uoc2 projectX` [`-a` --> add a member to a group]
    - for the user uoc to del a user from the group
        - `gpasswd -d uoc2 projectX` [`-d` to delete user from the group]


-------------------------------------------------------------------

#### Administration of FileSystems & Security

-------------------------------------------------------------------

##### Mount & Manage FileSystems (Partitions & Devices)
- Security 

----------------

- `mkfs` - build/create/formatting file system
- `fdisk` - create partition/ partition table manipulator 
- `fsck` - check/repair the file system

##### FileSystems
- Directory Structure `/etc` ; `/home`
- Low Level organization - `ext2Fs`, `ext3`, `ReiserFs`

- `which mkfs` --> `/sbin/mkfs`
- `which fdisk` --> `/sbin/fdisk` /??\ `/sbin/fsck`

##### `fdisk -l`
   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|
| Device  |Boot   |Start   |End   | Blocks  | Id  | System  |
| /dev/sda1  |*   |1   |6   |   |   | Linux  |
| /dev/sda2  |   | 7  |   |   |   | Linux   |
| /dev/sda3  |   | 458  |   |   |   | Linux Swap  |

----------------------------------------------

- fdisk /dev/sda
- Comman (m for help): m 

-----------------------------------------------

- `mount -t iso9660 /dev/cdrom /mnt/cdrom`

-------------

`df`
/dev/sda2
/dev/sda1
------------------
df -h
du -h 
----------------------
du --max-depth=1 -h 
----------------------
/bin - executable command :: executable command of the system  -- cd, more, less, cat, ls, vi, copy
/boot - boot the system, Linux kernel 
/home - user home directory
/dev - holds one file for every device of the system
/etc - system configuration file  
/lib - shared program library -- common code
/mnt - mount removable media -- cdrom, floppy
/opt - optional software 
/proc - information of process of the system
/root - root user's home directory
/tmp - temporary storage
/var - variable data -- log file, user's mail directory that change every time
/sbin - system administration utility   
/usr - user process' resources
/usr/bin - clear, C compiler 
/usr/etc - particular function of C 
/usr/sbin - system administration utility for specific user administration - useradd usedel

----------------------------------------------------------------
Accounts & Password
- Remove dormant accounts -- account that no longer usage 
- Remove unnecessary program -- 
- User's Permission - umask values in - /etc/profile
---------------
umask -S 
u=rwx,g=rx,0=rx

----------
set uid permissions 
ls -l /usr/bin/passwd
-rwsr-xr-x.
s - set UID permission

------------------------------
Networking Overview

-Hardware - routers, wires, -> Ethernet[10baset, 100baset], Switch[hub, routers]
-Packets[header] - information transfer among the computers
-Protocols - govern the rule how the packets transmit through the network
[TCP,IP,UDP] - Application, Transport, Internet, Network Interface
(Application, Transport) -> TCP/UDP; (Internet, Network Interface)->IP
-Addressing - origin and destination address ->Port, HW address, (IP address, hostnames) -> DNS


To setup a name server -> cat /etc/resolv.conf
----------------------
ifconfig eth0/eth1/lo up ip_address netmask netmask_address
route add default gw gateway_address

point-to-point protocol (ppp) -> /usr/share/doc/ppp-2.4.5/scripts
------------------
connect to remote desktop
telnet computer_name -> no encription, plain text

----------------------
ftp.google.com
ftp
gftp -> UI
-----------------
Firewalls - block access to any services

inetd -> TCP Wrappers - block access to specific services -- /etc/hosts.allow
 							     /etc/hosts.deny
Xinetd -> extended version of inetd 

-----------------------------
X windows

X server

Window Manager

Desktop Environment - KDE, GNOME, CDE, KWM, SawFish

---------------------
Runlevels /etc/inittab

0 --- off
1,s --- single-user mode
2 --- multi-user, without networking
3 --- multi-user, with networking
4 --- varies
5 --- X Windows
6 --- Shutdown, reboot

Config Files
-user --- dot files [.bashrc;.profile ](user's home directory)
-system --- /etc

-----
Environment Variables -> env

----------
Configuring Printers and Services for file sharing
------------

NFS - Network File Sharing
user -> lpr(line printer) -> lpd(line printer daemon)-> print queue -> printer
print queue - postscript / [now Driver - GhostScripts -> PC to Printer connection]

lpq - printout
lprm 

print queue -> /var/spool/lpd
config -> /etc/princtcap

Alternative Printing System -> BSD, LPRng, CUPS

Windows
Samba -smb -> server message block
CIFS

Linux 
NFS - Network File Sharing
cat /etc/fstab

----------------------------
smbclient path -U user_name

Alternative way
---------------
smbmount //path destination_folder_name stored_folder_name
smbumount stored_folder_name

NFS - Network File Sharing
--------------------------
mount machine_name:path_of_dir_name_to_share

---
Back-Ups
-------
1. Full - everything
2. Incremental - everything since last incremental
3. Diffrential - everything since last full backup

*tar - tape archive (tarball)
*tar --create --verbose --same-permissions --file file_name directory_to_store
*tar cvpf file_name directory_to_store

--diff or --compare -> d

incremental / differential - backup --> --newer 
------
*tar cvpf file_name --newer 20May15 directory_to_store
---
*tar --extract --verbose --same-permissions --file file_name directory_to_store
*tar xvpf file_name directory_to_store
-----------------
Listing a tar
tar tvpf or tar --List --verbose --same-permission --file

-------------------
Swap Space vs Main Memory(RAM)

* To create an empty swap file 
dd if=/dev/zero of=/swapfile bs=1024 count=262154
dd -> convert one file to another, change the size etc
if -> input file
of -> output file
bs -> block size
* To active the swapfile
mkswap /swapfile
swapon /swapfile
* To deactive the swapfile
swapoff /swapfile
----------------------

*All partition size of the HDD in Terminal -> lsblk -o NAME,SIZE

*Kernel Version -> uname -r / cat /proc/version

*Distributin Version -> lsb_release -asr

--------------------------------------------
Troubleshooting in Linux System
--------------------------------------------
Hardware
OS (kernel) kernel version_x.y.z [y-> enve = stable / odd = unstable]
Application Software 
Configuration
User

/etc/syslog.conf
***dmesg - information of system hardware and software
***route
***du / df
***fsck
***top
*** /etc/init.d/ -> all the scripts to start, stop, restart of the system

---------------
Useful commands
---------------
*find / -name file_namenn
*find . -mmin -50 	
*grep network boot.log
*tail file_name/ tail -f filename [-f -> follow file]
*tail -f /var/log/messages

-----------------
Examine log files
-----------------
*tail -f /var/log/messages

-----------------
Boot Problems
-----------------
LILO error code
*To boot without LILO
*LOADIN -> Needs: DOS boot floopy, copy of LOADIN.EXE & copy of kernel (vmlixuz)
1] Boot DOS
2] Loadin vmlinuz root=/dev/sda1

-----------------
Common Problems
-----------------
su -> switch user
-----
umount /mnt/cdrom
umount: /mnt/cdrom: device is busy
lsof | grep cdrom

-------------------
dig www.google.com
-------------------
cat /etc/resolv.conf 
nameserver 16.110.135.52


--------------------------
Kernel Modules -> Controlled by /etc/modules.conf
insmod -> insert module/installed module
modprobe -> 
lsmod  -> list information of modules
-f -> force installation, binary exe files
-K -> auto clean flag 
-p -> test run for modules

modules.dep -> modules dependencies

/dev - directory holds one entry for each device for the system
/dev/fdx - floppy
/dev/hdxy - IDE hard disk
/dev/sdxy - SCSI disk
/dev/usb/x - usb devices

EIDE/IDE - Enhanced Integrated Device Electronics
ATA - Advanced Technology Attachement
Linux supports 2 IDE controllers
Each controller supports 2 devices
Maximum 4 IDE devices

hdparm -t /dev/hda
Internal vs External Transfer Rates
--------------------------------------
SCSI - Small Computer Systems Interface
Compared to IDE - more performance, expensive, 
more device/controller 7 for standard SCSI, 15 for wide SCSI, 
Allow concurrent communication
Must terminate chains !!!

Hard Drive ------- SCSI Interface

IEEE 1394 (Firewire) - addon currently
--------------------------------------
--------------------------------------
Pre Installation Issues
fdisk, disk drvid
Kickstart
RAID - Redundant array of Independent Disk
















