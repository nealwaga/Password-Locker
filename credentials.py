from ast import Delete

class Credentials:
    credentials_list = []

    def __init__(self, user_name, social_networking_service, user_password):
        self.user_name = user_name
        self.social_networking_service = social_networking_service
        self.user_password = user_password

#saving credentials
    def save_credentials (self):
        Credentials.credentials_list.append (self)

#deleting credentials
    def delete_credentials (self):
        Credentials.credentials_list.remove (self)

#finding credentials
    @classmethod
    def find_credentials (cls, social_networking_service):
        for credential in cls.credentials_list:
            if credential.social_networking_service == social_networking_service:
                return True

        return False 

#displaying credentials
    @classmethod
    def display_credentials (cls):
        return cls.credentials_list                             