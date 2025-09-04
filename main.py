from music_data import add_user, add_album, all_users, all_albums
from queries import (
    query_user_artist, query_user_genre,
    query_age_artist, query_age_genre,
    query_city_artist, query_city_genre
)

def print_menu():
    print("\n=== Music Recommender Menu ===")
    print("1. Add a new user")
    print("2. Add a new album")
    print("3. Query by user & artist")
    print("4. Query by user & genre")
    print("5. Query by age & artist")
    print("6. Query by age & genre")
    print("7. Query by city & artist")
    print("8. Query by city & genre")
    print("9. Show all users")
    print("10. Show all albums")
    print("0. Exit")

def main():
    while True:
        print_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            username = input("Username: ")
            age = int(input("Age: "))
            city = input("City: ")
            albums_input = input("Enter purchased albums (comma separated, e.g., album1:2,album2:1): ")
            albums = []
            if albums_input:
                for item in albums_input.split(","):
                    name, count = item.split(":")
                    albums.append((name.strip(), int(count)))
            add_user(username, age, city, albums, all_users)

        elif choice == "2":
            album_name = input("Album name: ")
            artist = input("Artist: ")
            genre = input("Genre: ")
            tracks = int(input("Number of tracks: "))
            add_album(album_name, artist, genre, tracks, all_albums)

        elif choice == "3":
            username = input("Username: ")
            artist = input("Artist: ")
            result = query_user_artist(username, artist, all_users, all_albums)
            print(f"{username} purchased {result} tracks by {artist}.")

        elif choice == "4":
            username = input("Username: ")
            genre = input("Genre: ")
            result = query_user_genre(username, genre, all_users, all_albums)
            print(f"{username} purchased {result} tracks in genre {genre}.")

        elif choice == "5":
            age = int(input("Age: "))
            artist = input("Artist: ")
            result = query_age_artist(age, artist, all_users, all_albums)
            print(f"Users aged {age} purchased {result} tracks by {artist}.")

        elif choice == "6":
            age = int(input("Age: "))
            genre = input("Genre: ")
            result = query_age_genre(age, genre, all_users, all_albums)
            print(f"Users aged {age} purchased {result} tracks in genre {genre}.")

        elif choice == "7":
            city = input("City: ")
            artist = input("Artist: ")
            result = query_city_artist(city, artist, all_users, all_albums)
            print(f"Users in {city} purchased {result} tracks by {artist}.")

        elif choice == "8":
            city = input("City: ")
            genre = input("Genre: ")
            result = query_city_genre(city, genre, all_users, all_albums)
            print(f"Users in {city} purchased {result} tracks in genre {genre}.")

        elif choice == "9":
            print("\n--- All Users ---")
            for u, info in all_users.items():
                print(f"{u}: Age {info['age']}, City {info['city']}, Albums {info['albums']}")

        elif choice == "10":
            print("\n--- All Albums ---")
            for a, info in all_albums.items():
                print(f"{a}: Artist {info['artist']}, Genre {info['genre']}, Tracks {info['tracks']}")

        elif choice == "0":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
