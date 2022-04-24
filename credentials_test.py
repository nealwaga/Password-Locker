import unittest
from credentials import Credentials

class TestCredentials (unittest.TestCredentials):
    def setUp (self):
        self.new_credential = Credentials ("Neal", "Reddit", "waganealScrumhalf")

    def test_init (self):
        self.assertEqual (self.new_credential.user_name, "Neal")
        self.assertEqual (self.new_credential.social_networking_service, "Reddit")
        self.assertEqual (self.new_credential.user_password, "waganealScrumhalf")

#saving credentials
    def test_save_credential (self):
        self.new_credential.save_credentials ()
        self.assertEqual (len(Credentials.credentials_list), 1)

#multiple credentials
    def test_save_multiple_credentials (self):
        self.new_credential.save_credentials ()
        test_credentials = Credentials ("Test", "Social", "Password")
        test_credentials.save_credentials ()
        self.assertEqual (len(Credentials.credentials_list))

    def tearDown (self):
        Credentials.credentials_list = []

    def test_save_multiple_credentials (self):
        self.new_credential.save_credentials ()
        test_credentials = Credentials ("Test", "Social", "Password")
        test_credentials.save_credentials ()
        self.assertEqual (len(Credentials.credentials_list), 2)

    def test_delete_credentials (self):
        self.new_credential.save_credentials ()
        test_credentials = Credentials ("Test", "Social", "Password")
        test_credentials.save_credentials ()
        self.assertEqual (len(Credentials.credentials_list), 1)

    def test_find_credentials (self):
        self.new_credential.save_credentials ()
        test_credentials = Credentials ("Test", "Social", "Password")
        test_credentials.save_credentials ()

        found_credentials = Credentials.find_credentials ("Test")

        self.assertEqual (found_credentials.user_password, test_credentials.user_password)

#credentials exists
    def test_credentials_exists (self):
        self.new_credential.save_credentials ()
        test_credentials = Credentials ("Test", "Social", "Password")
        test_credentials.save_credentials ()

        credentials_exists = Credentials.credentials_exists ("Test")
        self.assertTrue (credentials_exists)

    def test_display_credentials (self):
        self.assertEqual (Credentials.display_credentials(), Credentials.credentials_list)

if __name__ == '__main__':
    unittest.main ()
