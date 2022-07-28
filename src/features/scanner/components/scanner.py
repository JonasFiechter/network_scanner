#  This app should to be a simple and lightweight tool to print on screen all the online machines 
# inside your network

# How to get the data from the system
from locale import locale_encoding_alias
import sys 
import subprocess
from tkinter.tix import Tree

command = ['ipconfig']

#  Instance of subprocess object
p = subprocess.Popen(command, stdout=subprocess.PIPE, text=True)
text = str(p.stdout.read())
retcode = p.wait()

print(text)