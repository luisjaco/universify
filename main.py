from data_tools.school_search import school_search
from data_tools.genre_heap import edit_heap, get_top_three
from data_tools.spotify import spotify_sequence
import json
from time import sleep

# USER ID: q818wih5cs74e1c0zi50c5kv0

def universify():
    print("""
  ___    _,---.   .--.-./`),---.  ,---.  .-''-. .-------.      .-'''-..-./`) ________   ____     __  
.'   |  | |    \  |  \ .-.'|   /  |   |.'_ _   \|  _ _   \    / _     \ .-.'|        |  \   \   /  / 
|   .|  | |  ,  \ |  / `-' |  |   |  ./ ( ` )   | ( ' )  |   (`' )/`--/ `-' |   .----'   \  _. /  /  
|'  '_  | |  |\_ \|  |`-'`"|  | _ |  . (_ o _)  |(_ o _) /  (_ o _).   `-'`"|  _|____     _( )_ ./'   
'   ( \.-.|  _( )_\  |.---.|  _( )_  |  (_,_)___| (_,_).' __ (_,_). '. .---.|_( )_   | __(_ o _)'    
| (`. _` /| (_ o _)  ||   |\ (_ o._) '  \   .---|  |\ \  |  .---.  \  :|   |(_ o._)__||  |(_,_)'     
| (_ (_) _|  (_,_)\  ||   | \ (_,_) / \  `-'    |  | \ `'   |    `-'  ||   ||(_,_)    |  \_'  /      
 \ /  . \ |  |    |  ||   |  \     /   \       /|  |  \    / \       / |   ||   |      \     /       
  ``-'`-'''--'    '--''---'   `---`     `'-..-' ''-'   `'-'   `-...-'  '---''---'       `..-'

Welcome to Universify, a program by Luis Jaco""")
    print("This program is intended to store, view and update data relating to colleges and their top music genres.\n")
    sleep(.5)
    while True:
        choice = input("""What would you like to do?
0 - Learn more
1 - Update data
2 - View existing data
3 - Quit program
""")
        if choice == '0':
            learn_more()
            break
        elif choice == '1':
            update_data()
            break
        elif choice == '2':
            view_data()
            break
        elif choice == '3':
            print("\nThank you for using Universify. Have a great day! :)\n")
            quit()
        else:
            print("\nInvalid response found, please try again...\n")
            continue
    
# For updating the school-genre data.
def update_data():
    # Setting up values and data.
    grade_category, top_genres, data = None, None, None
    # Loading the data from our current data file.
    with open('data_files/school_genre_data.json') as jsonfile:
        data = json.load(jsonfile)
    # Finds a school who's data will be updated.
    print("\nFirst you must selected the school which you'd like to update data for.")
    sleep(.5)
    school_id = school_search(data)
    sleep(.5)
    print("\nYou have selected {} as your school. Now enter the following:".format(data['schools'][school_id]['name']))

    # Grabs grade level for in-depth data.
    while True:
        choice = input("""
Please input your grade level:
0 - Freshman
1 - Sophomore
2 - Junior
3 - Senior
4 - Graduate
5 - Unknown
""")
        if choice == '0':
            grade_category = 'freshman_score'
            break
        elif choice == '1':
            grade_category = 'sophomore_score'
            break
        elif choice == '2':
            grade_category = 'junior_score'
            break
        elif choice == '3':
            grade_category = 'senior_score'
            break
        elif choice == '4':
            grade_category = 'graduate_score'
            break
        elif choice == '5':
            grade_category = 'unknown_score'
            break
        else:
            print("\nInvalid response found, please try again...\n")
            continue
    sleep(.5)

    # Gets user permission to have access to spotify data    
    print("\nNext, we will have to access your Spotify data. If you do not agree to this, you may exit the program.\n")
    while True:
        choice = input("""What would you like to do?
0 - Access Spotify data
1 - Quit
""")
        if choice == '0':
            # Initiates spotipy authorization.
            try:
                top_genres = spotify_sequence()
                break
            except:
                print("\n************     AN ERROR OCCURED    ************\n")
                print("Something went wrong with finding your account, please try again.\n")
                continue
            
        elif choice == '1':
            quit()
        else:
            print("\nInvalid response found, please try again...\n")
            continue

    # Checks if no genres were recieved. If genres are found, data is added to the current school after the user consents.
    if top_genres[0] is None:
        print("As there are no genres found, we cannot add non-existing data to our list.")
        end_prompt()
    else:
        while True:
            choice = input("""What would you like to do?
0 - Add genre data
1 - Don't add genre data
""")
            if choice == '0':
                # Adds data to the existing data, creates a new file & moves old files to a seperate folder
                print("We will now add these genres to the existing data for " + data['schools'][school_id]['name'] + "...")
                increment = 2000
                # Adding data to existing dictionary
                for genre in top_genres:
                    element = {
                        'genre' : genre,
                        "score" : increment,
                        "freshman_score" : 0,
                        "sophomore_score" : 0,
                        "junior_score" : 0,
                        "senior_score" : 0,
                        "graduate_score" : 0,
                        "unknown_score" : 0
                    }
                    element[grade_category] += increment
                    increment -=500
                    edit_heap(data['schools'][school_id], element)
                # Adds the new data to the existing json file
                with open("data_files/school_genre_data.json", 'w') as datafile:
                        json.dump(data, datafile, indent=4)
                sleep(.5)
                print("\nSuccessfully added data!\n")
                break
            elif choice == '1':
                print()
                break
            else:
                print("\nInvalid response found, please try again...\n")
                continue
    end_prompt()
    

def learn_more():
    pass

def view_data():
    pass

def load_data():
    with open('data_files/school_genre_data.json') as jsonfile:
        data = json.load(jsonfile)
    return data

def end_prompt():
    while True:
        choice = input("""What would you like to do?
0 - Start Universify again
1 - Quit
""")
        if choice == '0':
            universify()
            break
        elif choice == '1':
            print("\nThank you for using Universify. Have a great day! :)\n")
            quit()
        else:
            print("\nInvalid response found, please try again...\n")
            continue

universify()