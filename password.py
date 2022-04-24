import random
import string

def create_password ( char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
    choose = print ("What password length would you prefer?")
    answer = int (input("length: "))
    '''
    Function to create a 7 character password for a credential
    '''

    create_pass = ''.join (random.choice(char) for _ in range (answer))
    return create_pass