#!/usr/bin/env python
import threading
import string
import base64
import urllib.request
import urllib.parse
import os
import time
import sys
import random

try:
    import requests
except ImportError:
    print('Error !! : Some dependencies are not installed')
    print("Error to import 'requests' Library\ntodo : python3 -m pip install requests")
    exit()


def clr():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')

def banner():
    clr()
    logo = """                                                  
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 ##::::'##:::::::::::'######::'##::::'##::'######::
. ##::'##:::::::::::'##... ##: ###::'###:'##... ##:
:. ##'##:::::::::::: ##:::..:: ####'####: ##:::..::
::. ###::::'#######:. ######:: ## ### ##:. ######::
:: ## ##:::........::..... ##: ##. #: ##::..... ##:
: ##:. ##:::::::::::'##::: ##: ##:.:: ##:'##::: ##:
 ##:::. ##::::::::::. ######:: ##:::: ##:. ######::
..:::::..::::::::::::......:::..:::::..:::......:::  
     WhatsApp>  X-HACKRAWI    +31 97005033396"     version = V2       
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++  
                                         """
    print(logo)
    print("\n")
    

def Track() :
  TXTID = input("Enter Text ID of X-SMS \n\t -->>")
  os.system(f"curl https://textbelt.com/status/{TXTID}")
  input("\nPress Enter To Exit..")
  print("\nThanks For Using X-SMS..")
  print("\tWe Hope To See You Again\n Type bash Run.sh\n\tTo Run Again..")
  print("Thank you for Your Time...")
  exit()

clr()
banner()
   
while True:
	print("\033[0mThis Tool Is Used To Send Anonymous Messages")
	break
type = 0
try:
	if sys.argv[1] == "track":
		type = 1
except Exception:
	type = 0
if type == 1:
	print("Track The Anonymous Message You Sent Using This Tool.")
	print()
	Track()
elif type == 0:
	while True:
		print("Enter The Details Of The Person You Want To Send Anonymous Message")
		cc = input("\tEnter Country Code (Without +) : ")
		if '+' in cc:
		        tc = list(cc)
		        tc.remove('+')
		        cc = ''.join(tc)
		        cc = cc.strip()
		if len(cc) >= 4 or len(cc) < 1:
		        print('\n\nInvalid Country Code..\n\t\tCountry Codes Are Generally 1-3 digits...\n')
		        continue
		pn = input("Enter Phone Number : +" + cc + " ")
		if len(pn) <= 6:
		        print('\n\nInvalid Phone Number..\n')
		        continue
		numbe = cc + pn
		if not numbe.isdigit():
		            print('\n\nPhone Number Must Consist Of Numbers Only\n')
		            continue
		receiver = '+' + numbe
		text = input("Enter Message to send : ")
		
		resp = requests.post('https://textbelt.com/text',{
			'phone' : receiver,
			'message' : text ,
			'key' : 'textbelt'
		})
		
		print(resp.json())
		print("Thank you for Your Time...")
		break
		if '"success" : true ' in resp.text:
		    print("\033[92m Message Sent Succesfully \033[0m")
		    input('\n\t\tPress Enter To Exit...')
		    banner()
		    exit()
		if '"success" : false ' in resp.text:
		    print("\033[91m Error Occured")
		    print("\033[91m Failed to send SMS! ")
		    input('\n\t\tPress Enter To Exit...')
		    banner()
		    exit()
		exit() 
