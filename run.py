#!/usr/bin/env python3.8
from credentials import Credential
import login
 
#creating credentials
def create_credentials(usname,sprovider,uspassword):
        new_credential = Credential(usname,sprovider,uspassword)
        return new_credential

#saving credentials
def save_credentials(credential):
        credential.save_credential()
        
#deleting credentials
def del_credential(credential):
        credential.delete_contact()
        
def find_credential(serviceprovider):
        return Credential.find_credential(serviceprovider)

def check_exixting_credentials(serviceprovider):
        return Credential.credential_exist(serviceprovider)

def  display_credentials():
        return Credential.display_credential()

#main function
def main():
        print("Hello there. Welcome to my password locker and generator application,")
        ans=input("would you like to generate a password? (y for YES or n for NO):  ")
        if ans == "y":
                status = input("Are you a registered user of this application? (y for Yes or n for No)?")
                if status == "n":
                        login.register()
                        login.Login()
                else:
                        login.Login()
                       
                             
                                
if __name__ == '__main__':

     main()                        