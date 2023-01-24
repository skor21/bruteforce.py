# ztm_bruteforce.py
Simple python program to brute force metasploitable2 VM. 

This program is designed to perform a simple brute force using hydra on the metasploitable2 VM. 
The program was taken from ZTM Complete Ethical Hacking 2023 course. Some changes were made to the
original course program as I was unsuccessful getting it to work. This program was corrected using
chatgpt and has been tested to work on the metasploitable2 VM.


Line 2 - new line

from termcolor import colored #This will go under 'import requests'

line 10 - edit

print(colored(('Trying: ' + password), 'red))

line 16 - edit

print(colored(('[+] Found Username: ==> ' + username), 'green'))

line 17 - edit

print(colored(('[+] Password: ==>'+ password), 'green')) 
