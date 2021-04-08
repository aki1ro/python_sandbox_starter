#!/usr/bin/env python3

'''
You have a bad carriage return character at the end of the first line in your code as told by the following error message.

bash: ./mcb.py: /usr/bin/python3^M: bad interpreter: No such file or directory
The ^M is a carriage return character. If you see this, you're probably looking at a file that originated in the DOS/Windows world, where an end-of-line is marked by a carriage return/newline pair, whereas in the Unix world, end-of-line is marked by a single newline. source

To get rid of the error make a new mcb.py file. Open the default Text Editor app, copy the code from your question and paste it into Text Editor (gedit in Ubuntu 20.04), save the code as mcb.sh, and run the code again with the following commands:

chmod +x  mcb.sh
./mcb.sh

Or you can run dos2unix (filename)

dos2unix -c mac filename (converts dos/windows to unix files, c = conversion type.)
'''

import os
import subprocess as sp
import time as t 
import getpass as gp #used to ask for password input

def error(func):
   def wrap():
      try:
         func()
      except(KeyboardInterrupt):
         print("\nEXITING SCRIPT...")
   return wrap

@error
def user_available(u, p):
   users = str(sp.check_output('sudo getent "passwd" | awk -F: "{print $1}"', shell=True)).split()
   #For each record i.e line, the awk command splits the record delimited by whitespace character by default and stores it in the $n variables. If the line has 4 words, it will be stored in $1, $2, $3 and $4 respectively. Also, $0 represents the whole line. 
  
   if u in users:
      print(f"User {u} already in Database")
   else:
      print(f"User {u} is being added to Database")
      adduser(u,p)
   
@error   
def adduser(u,p):
   sp.run(['sudo', 'useradd', u])
   proc = sp.Popen(['passwd','--stdin', u], stdin=sp.PIPE) # sp.PIPE used to pipe stdin to communicate. 
   proc.communicate(input=p.encode()) #encode turns str into binary and comunicate is used for input
   print(f"User {u} Added Successfully")
   createshare(u)
@error   
def createshare(u):
   share = f"/mnt/NetworkShare/{u}"
   df = str(sp.check_output('df | grep "192.168.50.101/Net"', shell=True)).split()
   check_share = "b'//192.168.50.101/NetworkShare"
   
   if check_share in df:
         print("Network Share mounted!\n")
   else:
         print("Adding Network Share to /mnt/NetShare\n")
         sp.run(['sudo','mount', '-t', 'cifs', '-o', 'credentials=/etc/win-credentials', '//192.168.50.101/NetworkShare', '/mnt/NetworkShare'])
   sp.run(['mkdir', share])
   print("Adding Permission to Share\n")
   sp.run(['chmod','600', share])
   print("Successfully added Permissions\n")
   os.chdir(share)
   print("New User Share Location:", os.getcwd())
   copytxt(u)
   
@error
def copytxt(u):
   home = f"/home/{u}/Desktop"
   sp.run(["cp", "/mnt/NetworkShare/You've Made it.txt", home])
   print("text file copied")
@error
def isroot(r):
   if r == ("y" or "yes" or "Y" or "Yes"):
      x = input("Enter Username here: ")
      y = gp.getpass("Enter Password here: ")
      user_available(x, y)
   elif r == ("n" or "no" or "N" or "No"):
      print("Please Login as 'root'")

x = input("Are you root?(script will fail if not root) y/n: ")

isroot(x)

  
   


