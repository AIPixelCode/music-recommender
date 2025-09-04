import unittest
import sys
import os

# Add the parent directory to the path to import modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from music_data import add_user, add_album, all_users, all_albums


class TestMusicData(unittest.TestCase):

    def setUp(self):
        # Clear previous data before each test
        all_users.clear()
        all_albums.clear()

    def test_add_album(self):
        # Test adding a new album
        add_album("Test Album", "Test Artist", "Rock", 10)
        self.assertIn("Test Album", all_albums)
        self.assertEqual(all_albums["Test Album"]["artist"], "Test Artist")

    def test_add_user(self):
        # Test adding a new user with albums
        add_user("test_user", 25, "Tehran", [("Album1", 2)])
        self.assertIn("test_user", all_users)
        self.assertEqual(all_users["test_user"]["age"], 25)

    def test_add_duplicate_user(self):
        # Test that duplicate users are not added
        add_user("test_user", 25, "Tehran")
        # Should not add duplicate user
        add_user("test_user", 30, "Shiraz")
        self.assertEqual(all_users["test_user"]["age"], 25)  # Age should not change


if __name__ == '__main__':
    unittest.main()