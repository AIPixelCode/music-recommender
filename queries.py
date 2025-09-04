# Module to query users and albums

def query_user_artist(username, artist, all_users, all_albums):
    """Count tracks purchased by a user for a specific artist."""
    if username not in all_users:
        return 0
    return sum(
        all_albums[album]['tracks'] * qty
        for album, qty in all_users[username]['albums']
        if all_albums[album]['artist'] == artist
    )


def query_user_genre(username, genre, all_users, all_albums):
    """Count tracks purchased by a user for a specific genre."""
    if username not in all_users:
        return 0
    return sum(
        all_albums[album]['tracks'] * qty
        for album, qty in all_users[username]['albums']
        if all_albums[album]['genre'] == genre
    )


def query_age_artist(age, artist, all_users, all_albums):
    """Count tracks purchased by all users of a certain age for a specific artist."""
    return sum(
        query_user_artist(u, artist, all_users, all_albums)
        for u, info in all_users.items() if info['age'] == age
    )


def query_age_genre(age, genre, all_users, all_albums):
    """Count tracks purchased by all users of a certain age for a specific genre."""
    return sum(
        query_user_genre(u, genre, all_users, all_albums)
        for u, info in all_users.items() if info['age'] == age
    )


def query_city_artist(city, artist, all_users, all_albums):
    """Count tracks purchased by all users in a city for a specific artist."""
    return sum(
        query_user_artist(u, artist, all_users, all_albums)
        for u, info in all_users.items() if info['city'] == city
    )


def query_city_genre(city, genre, all_users, all_albums):
    """Count tracks purchased by all users in a city for a specific genre."""
    return sum(
        query_user_genre(u, genre, all_users, all_albums)
        for u, info in all_users.items() if info['city'] == city
    )
