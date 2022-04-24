import unittest
from user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User("Neal","waganealScrumhalf9.")
        
    def test_init(self):
        self.assertEqual(self.new_user.username,"Neal")
        self.assertEqual(self.new_user.userpassword,"waganealSCrumhalf9.")
    
if __name__ == '__main__':
    unittest.main()   