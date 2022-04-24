import unittest
from user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User("Elijah","euregfj")
        
    def test_init(self):
        self.assertEqual(self.new_user.username,"Elijah")
        self.assertEqual(self.new_user.userpassword,"euregfj")
    
if __name__ == '__main__':
    unittest.main()   