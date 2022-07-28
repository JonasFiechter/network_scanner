#  This app should be a simple and lightweight tool to print on screen all the online machines 
# inside your network

# How to get the data from the system
import subprocess
import unicodedata

command = ['ipconfig']

class Scanner:
    def __init__(self):
        pass
    
    def get_str_from_cmd(self):
        p = subprocess.Popen(command, stdout=subprocess.PIPE, text=True)
        text = str(p.stdout.read())
        unicodedata.normalize(text, 'utf-8')
        return text
