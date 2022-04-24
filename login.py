from user import User
import run
from random import randint
from password import generate_password

def register():
    print("REGISTER HERE")
    print("-"*50)
    username = input("Enter your username:  ")
    userpassword = input("Enter your register password:  ")
    compassword=input("Kindly confirm your password:  ")

#validation
    if userpassword == compassword:
        user = User(username,userpassword)
        user.save_user
        print(f"Welcome {username}. You are now a registered user.")
        print("Now proceed to log-in")
        
    else:
       repeat= input("There has been an error. Do you want to try again? (y for Yes or n for No)")
       if repeat == "y":
           print(register())
       else:
           print(exit())
           

#login   
def Login():
     print("LOG-IN HERE")
     print("-"*50)
     username = input("Enter your username: ")
     userpassword = input("Enter your log-in password:  ")
     
     user = User(username,userpassword)
     if user is None:
         print("Please enter a username and password of your choice.")
     else:
         user.login
         print(f"Welcome {username}. You are now successfully logged in.")
         print("\n")
         print("-"*50)
         print(f"{username}, what would you like to do next?")
         while True:
            print("Use the following short codes to make a decision: cc - create a new password , dc - display created password , fc - find a specific password , dd - delete existing password , ex - exit the application")
            print("-"*50)
            useranswer = input("Answer: ")
            if useranswer == "cc":
                            choose= input("Would you like to create your own custom password or would you prefer a password generated for you instead?: (c = custom password and g = generated password)")
                            if  choose == "c":
                                    
                                    print("*"*50)
                                    print("What is your social network provider? (.e.g Instagram, Twitter)")
                                    sprovider= input()
                                    
                            
                                    print("Your username:")
                                    usname= input()
                            
                                                        
                                    print("Your password:")
                                    uspassword= input()
                                    
                                    run.save_credentials(run.create_credentials(usname,sprovider,uspassword))
                                    print("\n")
                                    print(f"Great! Your new {sprovider} credentials have been successfully created and saved. Here they are:")
                                    print(f"Name: {usname}")
                                    print(f"Password: {uspassword}")
                                    print("\n")
                                    # print(run.display_credentials())
                            else:
                                print("*"*60)
                                print("What is your social network provider? (.e.g Instagram, Twitter)")
                                sprovider= input()
                                    
                            
                                print("Username:")
                                usname= input()
                            
                                                        
                            
                                uspassword=generate_password()
                                print("*"*60)
                                run.save_credentials(run.create_credentials(usname,sprovider,uspassword))
                                print("\n")
                                print(f"Great! Your new {sprovider} credentials have been successfully created and saved.")
                                print(f"Name: {usname}")
                                print(f"Password: {uspassword}")
                                print("\n")
                                print("*"*60)

            elif useranswer == "dc":
                if run.display_credentials():
                    print("Here are your saved passwords:")
                    print("\n")
                    
                    for credential in run.display_credentials():
                        print(f"{credential.username} {credential.serviceprovider} ......{credential.userpassword}")
                    print('\n')
                else:
                    print('\n')
                    print("Unfortunately, you do not have any saved passwords. You have to create one first.")
                    print('\n')
                    
            elif useranswer == "dd":
                print("Enter the account you would like to delete (Use your social network provider for this):")
                deleteAccount = input()
                #  if deleteAccount == :
                #      deleteAccount = run.del_credential(deleteAccount)
                print(f"{deleteAccount} account has been successfuly deleted")
                #  else:
                #      print("you have no account to delete")
                
            elif useranswer == "ex":
                            print("You are now out of the application. I hope it was a five star user experience for you.")
                            break
            else:
                            print("There has been an error. Please use the short codes correctly.") 