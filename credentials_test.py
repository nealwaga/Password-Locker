import unittest
from credentials import Credential

class TestCredentials(unittest.TestCase):
    def setUp(self):
        self.new_credential = Credential("Neal","Reddit","waganealScrumhalf9.")
    
    def test_init(self):
        self.assertEqual(self.new_credential.username,"Neal")
        self.assertEqual(self.new_credential.serviceprovider,"Reddit")
        self.assertEqual(self.new_credential.userpassword,"waganealScrumhalf9.")
        
    
    # credential save
    def test_save_credential(self):
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credentials_list),1)
        
        # multiple credentials
        
    def test_save_multiple_credentials(self):
        self.new_credential.save_credential()
        test_credential = Credential("Test","Social Network","Password","Number",)
        test_credential.save_credential()
        self.assertEqual(len(Credential.credentials_list))
        
    def tearDown(self):
        Credential.credentials_list = []
        
        
    def test_save_multiple_credentials(self):
        self.new_credential.save_credential()
        test_credential = Credential("Test","Social Network","Password","Number",)
        test_credential.save_credential()
        self.assertEqual(len(Credential.credentials_list),2)
        
            
        
    def test_delete_credential(self):
        self.new_credential.save_credential()
        test_credential = Credential("Test","Social Network","Password","Number",)
        test_credential.save_credential()
        
        self.new_credential.delete_credential()
        self.assertEqual(len(Credential.credentials_list),1)
        
        # find credential
        
    def test_find_credential(self):
        self.new_credential.save_credential()
        test_credential = Credential("Test","Social Network","Password",)
        test_credential.save_credential()
        
        found_credential = Credential.find_credential("userp")
        
        self.assertEqual(found_credential.userpassword,test_credential.userpassword)
        
        # credential exist
        
    def test_credential_exist(self):
        self.new_credential.save_credential()
        test_credential = Credential("Test","Social Network","Password")
        test_credential.save_credential()
        
        credential_exist = Credential.credential_exist("userp")
        self.assertTrue(credential_exist)
        
    def test_display_credentials(self):
        self.assertEqual(Credential.display_credential(),Credential.credentials_list)       
        
    
if __name__ == '__main__':
    unittest.main()
