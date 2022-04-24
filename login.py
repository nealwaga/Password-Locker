from user import User
import run
from random import randint
from password import create_password

def register ():
    print ("Register")
    print ("-"*30)
    user_name = input ("Enter your username:  ")
    user_password = input ("Enter your password:  ")
    confirm_password = input ("Kindly confirm your password:  ")

#validating
    if user_password == confirm_password:
        user = User (user_name, user_password)
        user.save_user
        print (f"Welcome {user_name}. You have now successfully registered.")
        print ("Now, proceed to login")

    else:
        repeat = input ("There was an unfortunate error. Try again? Y/N")
        if repeat == "Y":
            print (register())
        else:
            print (exit())

#logging in
def logging_in ():
    print ("Log-in")
    print ("-"*30)
    user_name = input ("Enter your username:  ")
    user_password = input ("Enter your password:  ")

    user = User (user_name, user_password)
    if user is None:
        print ("Please key in a valid username and password")
    else:
        user.login
        print (f"Welcome {user_name}, you have now successfully logged in.")
        print ("\n")
        print ("-"*30)
        print ("What would you like to do?")
        while True:
            print ("Use the short codes: cc-Create a new password, dc-Display password, fc-Find a specific password, ss-Delete your credentials, ex-Exit")
            print ("-"*30)
            user_answer = input ("Your answer:  ")
            if user_answer == "cc":
                choose = input ("Would you like a custom password or a generated password? : C = Custom password and G = Generated password: C/G")
                if choose == "C":

                    print ("-"*30)
                    print ("Your social networking service? e.g. Instagram, Twitter")
                    snservice = input ()

                    print ("Your username? ")
                    usname = input ()

                    print ("Your password? ")
                    uspassword = input ()

                    run.save_credentials (run.create_credentials (usname, snservice, uspassword))
                    print ("\n")
                    print (f"Your new {snservice} credentials have been created and saved:")
                    print (f"Name: {usname}")
                    print (f"Password: {uspassword}")
                    print ("\n")

                else:
                    print ("-"*30)
                    print ("Social Networking Service e.g. Instagram, Twitter")
                    snservice = input ()

                    print ("Your username")
                    usname = input ()

                    uspassword = create_password ()
                    print ("-"*30)
                    run.save_credentials (run.create_credentials (usname, snservice, uspassword))
                    print ("-"*30)
                    print (f"Your new {snservice} credentials have been csuccessfully created and saved.")
                    print (f"Name: {usname}")
                    print (f"Password: {uspassword}")
                    print ("\n")
                    print ("-"*30)

            elif user_answer == "dc":
                if run.display_credentials ():
                    print ("Here is a lis of your passwords:")
                    print ("\n")

                    for credential in run.display_credentials ():
                        print (f"{credential.user_name} {credential.social_networking_service} {credential.user_password}")
                        print ("\n")
                else:
                    print ("\n")
                    print ("Sorry. Unfortunately you do not have any saved passwords.")
                    print ("\n")

            elif user_answer == "dd":
                print("Please enter the account you want to delete:" )
                deleteAccount = input()
                #  if deleteAccount == :
                #      deleteAccount = run.del_credential(deleteAccount)
                print(f"{deleteAccount} account successfuly deleted")
                #  else:
                #      print("you have no account to delete")
                
            elif user_answer == "ex":
                            print("Bye...")
                            break
            else:
                            print("I did not get that. Please use the short codes")                  