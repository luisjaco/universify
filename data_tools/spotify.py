# This file uses spotipy to authenticate the user and then find the users top genres.
import os
import spotipy
from time import sleep

def spotify_sequence():
    print("\n************ENTERING SPOTIFY SEQUENCE************")
    print("""
We are going to access your Spotify data, first we will ask your username (can be found in Spotify settings).
We will then open a window in your browser to continue Spotify authentication. Once you authenticate your Spotify
account online, copy the link you are redirected to and paste it back into the program.
""")
    # Setting scope of the program for user authentication.
    scope = "user-top-read"
    
    while True:
        # Grabbing username to do all spotify api functions.

        username = input("Please input your spotify username: ")
        # Using spotipy to handle grabbing authentication.
        try:
            # This will prompt the user twice if it does not work the first time.
            token = spotipy.prompt_for_user_token(username, scope)
            # For this program, the user should have redo authentication each time they use the program, so I delete the cache if it exists.
            try:
                os.remove(f'.cache-{username}')
            except:
                pass
            break
        except:
            # Given an error occurs, the user has to keep trying until a valid token is recieved.
            print("\n************     AN ERROR OCCURED    ************\n")
            try:
                os.remove(f'.cache-{username}')
            except:
                pass
            while True:
                choice = input("""What would you like to do?
0 - Try again
1 - Quit
""")
                if choice == '0':
                    print()
                    break
                elif choice == '1':
                    print("\nThank you for using Universify. Have a great day! :)\n")
                    raise ValueError
                else:
                    print("\nInvalid response found, please try again...\n")
                    continue

    sp_obj = spotipy.Spotify(auth=token)
    # Catching user dashboard error (user was not manually input into the program by me.)
    try:
        name = sp_obj.current_user()['display_name']
    except:
        print("\nAn error occured with obtaining your data, the owner of this program must manually enter your account\ninto the spotify api for a user to be able to use their user data.")
        print("\nThank you for using Universify. Have a great day! :)\n")
        raise ValueError
    sleep(.5)
    print('\nWelcome ' + name.strip() + "! We are currently finding your top three genres based on your favorite artists...")

    # Displaying to the user what the calculated top genres are.
    top_three = get_top_three_genres_artists(sp_obj)
    if top_three[0] is None:
        print("There were no genres found. Please listen to some songs first!")
    else:
        valid_genres = [i for i in top_three if i is not None]
        print("Your favorite genres are: ",end='')
        for i in range(len(valid_genres)):
            if i == len(valid_genres)-1:
                print(valid_genres[i],end='.\n')
            elif i == len(valid_genres)-2:
                print(valid_genres[i], end=' and ')
            else:
                print(valid_genres[i],end=', ')
    print()

    return top_three

def get_top_three_genres_artists(sp_obj):
    # The Spotify API does not give a direct method of grabbing the top genres in a user, so we will use-
    # this method to calculate a users top genres using a users top artists.

    # Gets a users top 10 artists, or less, given there are less than 10.
    artist_data = sp_obj.current_user_top_artists(limit=10)

    # To hold genres and have an accurate list to calculate the top three genres, we will use a dictionary formatted like so:-
    # key: genre name, value: count of times seen
    genre_dict = {}
    for i in artist_data['items']:
        for j in i['genres']:
            if genre_dict.get(j) is not None:
                genre_dict[j] += 1
            else:
                genre_dict[j] = 1

    # We will hold the top three genres in a list. If there are not enough genres to have a top three, the missing spots will be None
    top_three = [None, None, None]
    index = 0

    # This will find the top three values by finding the max value in the dictionary, adding it to the list, then popping the genre from-
    # the genre_dict. In the case where there are multiple genres with the same count, max() picks the oldest genre.
    while genre_dict and index < 3:
        top_three[index] = max(genre_dict, key=genre_dict.get)
        genre_dict.pop(top_three[index])
        index += 1

    return top_three
