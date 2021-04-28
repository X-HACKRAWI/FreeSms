#!/usr/bin/python3
import base64
import time
import os
import sys
try:
    import requests
    
except ImportError:
    print("Error to import 'requests' Library\ntodo : python3 -m pip install requests")
    exit()

banner ="""
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 ##::::'##:::::::::::'######::'##::::'##::'######::
. ##::'##:::::::::::'##... ##: ###::'###:'##... ##:
:. ##'##:::::::::::: ##:::..:: ####'####: ##:::..::
::. ###::::'#######:. ######:: ## ### ##:. ######::
:: ## ##:::........::..... ##: ##. #: ##::..... ##:
: ##:. ##:::::::::::'##::: ##: ##:.:: ##:'##::: ##:
 ##:::. ##::::::::::. ######:: ##:::: ##:. ######::
..:::::..::::::::::::......:::..:::::..:::......:::  
     WhatsApp>  X-HACKRAWI    +31 97005033396"             
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++  

  
    """
os.system('clear') 
print(banner)

p = input("Enter a phone number : > ")
m = input("Enter the text message : > ")
resp = requests.post('https://textbelt.com/text', {
        'phone': (p),
        'message': (m), 
        'key': 'textbelt',      
})

try:
    int(p) 
    print("\n\t\t[ + ] plase whate ..... ")
    time.sleep( 5 )
    print(resp.json())
    

except:
    print("\n\t[!] Error sending the message")
    print("\t[!] Please enter the number  \n ")






