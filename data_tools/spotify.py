# This file is for spotipy functions.
import sys
import os
import json
from json.decoder import JSONDecodeError
import spotipy
import webbrowser
import spotipy.util as util

def spotify_sequence():
    print("\n************ENTERING SPOTIFY SEQUENCE************\n")

    # Setting scope of the program for user authentication.
    scope = "user-top-read"
    
    while True:
        # Grabbing username to do all spotify api functions.
        username = input("Please input your spotify username: ")
        # Using spotipy to handle grabbing authentication.
        try:
            # This will prompt the user twice if it does not work the first time.
            token = spotipy.prompt_for_user_token(username, scope)
            break
        except:
            # Given an error occurs, the user has to keep trying until a valid token is recieved.
            print("\n************     AN ERROR OCCURED    ************\n")
            print("Something went wrong with finding your account, please try again.\n")
            try:
                os.remove(f'.cache-{username}')
            except:
                pass

    sp_obj = spotipy.Spotify(auth=token)
    name = sp_obj.current_user()['display_name']
    print('Welcome ' + name.strip() + "! We are currently finding your top three genres based on your favorite artists...")

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
            
    # For this program, the user should have to input their username each time they use the program, so I delete the cache if it exists.
    try:
        os.remove(f'.cache-{username}')
    except:
        pass

    # Returns top three to where this was called
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


# USER ID: q818wih5cs74e1c0zi50c5kv0