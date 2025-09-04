import unittest
import sys
import os

# Add the parent directory to the path to import modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from music_data import add_user, add_album, all_users, all_albums
from queries import query_user_artist, query_user_genre


class TestQueries(unittest.TestCase):

    def setUp(self):
        # Clear previous data and set up test data
        all_users.clear()
        all_albums.clear()

        # Add test data
        add_album("Album1", "Artist1", "Rock", 5)
        add_album("Album2", "Artist1", "Pop", 3)
        add_album("Album3", "Artist2", "Jazz", 7)

        add_user("user1", 25, "Tehran", [("Album1", 2), ("Album2", 1)])
        add_user("user2", 30, "Shiraz", [("Album3", 1)])

    def test_query_user_artist(self):
        # Test query for tracks by a specific artist for a user
        result = query_user_artist("user1", "Artist1", all_users, all_albums)
        self.assertEqual(result, 2 * 5 + 1 * 3)  # (2 * 5) + (1 * 3)

    def test_query_user_genre(self):
        # Test query for tracks in a specific genre for a user
        result = query_user_genre("user1", "Rock", all_users, all_albums)
        self.assertEqual(result, 2 * 5)  # 2 * 5

    def test_query_nonexistent_user(self):
        # Test query for a user that doesn't exist
        result = query_user_artist("nonexistent", "Artist1", all_users, all_albums)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()