import unittest

from user import User

class TestUser (unittest.TestCase):
    def setUp(self):
        self.new_user = User ("Neal", "waganealScrumhalf9")

    def test_init (self):
        self.assertEqual (self.new_user.)  