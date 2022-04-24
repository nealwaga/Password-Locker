from ast import Delete


class Credential:
    credentials_list = []
    
    def __init__(self,username,serviceprovider,userpassword):
        
        self.username = username
        self.serviceprovider= serviceprovider
        self.userpassword= userpassword
        
        
    
    # savecredential
    def save_credential(self):
        
        Credential.credentials_list.append(self)
        
    # Delete credentials
    
    def delete_credential(self):
        Credential.credentials_list.remove(self)
        
        # finding a credential
    @classmethod   
    def find_credential(cls,serviceprovider):
        for credential in cls.credentials_list:
            if credential.serviceprovider == serviceprovider:
                return credential
            
            # check if it exist
    @classmethod
    def credential_exist(cls,serviceprovider):
        for credential in cls.credentials_list:
            if credential.serviceprovider == serviceprovider:
                return True
        return False
    
    @classmethod
    def display_credential(cls):
        return cls.credentials_list  