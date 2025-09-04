# Dictionaries to store users and albums
all_users = {}
all_albums = {}


def add_album(name, artist, genre, tracks):
    """
    Add a new album to all_albums.

    Args:
        name (str): Album name
        artist (str): Artist name
        genre (str): Album genre
        tracks (int): Number of tracks
    """
    if name not in all_albums:
        all_albums[name] = {'artist': artist, 'genre': genre, 'tracks': tracks}
        print(f"Album '{name}' added.")
    else:
        print(f"Album '{name}' already exists.")


def add_user(username, age, city, albums=None):
    """
    Add a new user with initial purchased albums.

    Args:
        username (str): Username
        age (int): Age of the user
        city (str): City of residence
        albums (list of tuples): List of (album_name, quantity)
    """
    if albums is None:
        albums = []
    if username not in all_users:
        all_users[username] = {'age': age, 'city': city, 'albums': albums.copy()}
        print(f"User '{username}' added.")
    else:
        print(f"User '{username}' already exists.")


def purchase_album(username, album_name, quantity=1):
    """
    Record a purchase of an album by a user.

    Args:
        username (str): Username
        album_name (str): Album to purchase
        quantity (int): Number of copies bought
    """
    if username not in all_users:
        print(f"User '{username}' does not exist.")
        return
    if album_name not in all_albums:
        print(f"Album '{album_name}' does not exist.")
        return

    # Check if user already has this album
    user_albums = all_users[username]['albums']
    for i, (name, qty) in enumerate(user_albums):
        if name == album_name:
            user_albums[i] = (name, qty + quantity)
            print(f"User '{username}' purchased {quantity} more of '{album_name}'.")
            return

    # New album purchase
    user_albums.append((album_name, quantity))
    print(f"User '{username}' purchased '{album_name}' ({quantity} copies).")
