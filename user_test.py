import unittest

from user import User

class TestUser (unittest.TestCase):
    def setUp(self):
        self.new_user = User ("Neal", "waganealScrumhalf9")

    def test_init (self):
        self.assertEqual (self.new_user.user_name, "Neal")
        self.assertEqual (self.new_user.user_password, "waganealScrumhalf9")

if __name__ == '__main__':
    unittest.main ()          