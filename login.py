from user import User
import run
from random import randint
from password import generate_password

def register():
    print("REGISTER")
    print("-"*30)
    username = input("enter username:  ")
    userpassword = input("enter register password:  ")
    compassword=input("confirm password:   ")
    #  validation
    if userpassword == compassword:
        user = User(username,userpassword)
        user.save_user
        print(f"Welcome {username}!you are now registered")
        print("Lets Login")
        
    else:
       repeat= input("Something has gone wrong. Try again. y/n")
       if repeat == "y":
           print(register())
       else:
           print(exit())
           
        #    login
        
def Login():
     print("LOGIN")
     print("-"*30)
     username = input("Enter username: ")
     userpassword = input("enter login password:  ")
     
     user = User(username,userpassword)
     if user is None:
         print("please enter a valid name and password")
     else:
         user.login
         print(f"Welcome {username}!you are logged in")
         print("\n")
         print("-"*30)
         print('What would you like to do?')
         while True:
            print("use this short codes : cc-create a new password , dc-display passwords for different userservice,fc-find a specific password,dd-delete,ex -exit" )
            print("-"*50)
            useranswer = input("answer: ")
            if useranswer == "cc":
                            choose= input("would you like a custom password or generated password?: c = custom and g = generated password: c/g?")
                            if  choose == "c":
                                    
                                    print("*"*60)
                                    print("service provider eg twitter")
                                    sprovider= input()
                                    
                            
                                    print("User Name")
                                    usname= input()
                            
                                                        
                                    print("password")
                                    uspassword= input()
                                    
                                    run.save_credentials(run.create_credentials(usname,sprovider,uspassword))
                                    print("\n")
                                    print(f"New {sprovider} credentials created and saved:")
                                    print(f"Name:{usname}")
                                    print(f"password:{uspassword}")
                                    print("\n")
                                    # print(run.display_credentials())
                            else:
                                print("*"*60)
                                print("service provider eg twitter")
                                sprovider= input()
                                    
                            
                                print("User Name")
                                usname= input()
                            
                                                        
                            
                                uspassword=generate_password()
                                print("*"*60)
                                run.save_credentials(run.create_credentials(usname,sprovider,uspassword))
                                print("\n")
                                print(f"New {sprovider} credentials created and saved:")
                                print(f"Name:{usname}")
                                print(f"password:{uspassword}")
                                print("\n")
                                print("*"*60)
            elif useranswer == "dc":
                if run.display_credentials():
                    print("Here is a list of your saved passwords")
                    print("\n")
                    
                    for credential in run.display_credentials():
                        print(f"{credential.username} {credential.serviceprovider} ......{credential.userpassword}")
                    print('\n')
                else:
                    print('\n')
                    print("Sorry!you do not have any saved passwords")
                    print('\n')
                    
            elif useranswer == "dd":
                print("Enter the account you want to delete:" )
                deleteAccount = input()
                #  if deleteAccount == :
                #      deleteAccount = run.del_credential(deleteAccount)
                print(f"{deleteAccount} account successfuly deleted")
                #  else:
                #      print("you have no account to delete")
                
            elif useranswer == "ex":
                            print("Bye .......")
                            break
            else:
                            print("I really didn't get that. Please use the short codes") 