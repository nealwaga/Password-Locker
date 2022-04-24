import random
import string

def generate_password( char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
    choose = print("What is your choice of password length?")
    answer = int(input("Length chosen: "))
    '''
    Function to generate an 8 character password for a credential
    '''
    gen_pass=''.join(random.choice(char) for _ in range(answer))
    return gen_pass