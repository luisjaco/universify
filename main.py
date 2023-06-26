from data_tools.school_search import school_search
from data_tools.genre_heap import edit_heap, get_top_three
from data_tools.spotify import spotify_sequence
import json
from time import sleep

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
    print("""* DUE TO MY SPOTIFY APPLICATION ONLY BEING DEVELOPMENTAL, I HAVE TO MANUALLY ENTER ANYONE WHO USES THIS APPLICATION TO ADD DATA.
* IF YOU ARE SOMEONE WHO WOULD LIKE TO USE THIS APPLICATION YOU CAN CONTACT ME AT: LUISJACOO04@GMAIL.COM

* YOU MAY ALSO TRY ANYWAYS, AS IT SOMETIMES WORKS WITHOUT BEING PUT IN.
""")
    sleep(.5)
    while True:
        choice = input("""What would you like to do?
0 - Update data
1 - View existing data
2 - Learn more
3 - Quit program
""")
        if choice == '0':
            update_data()
            break
        elif choice == '1':
            view_data()
            break
        elif choice == '2':
            learn_more()
            break
        elif choice == '3':
            print("\nThank you for using Universify. Have a great day! :)\n")
            quit()
        else:
            print("\nInvalid response found, please try again...\n")
            continue
    
# For the 'Update data' option. Lets user update the school-genre data.
def update_data():
    # Setting up values and data.
    grade_category, top_genres, data = None, None, None
    # Loading the data from our current data file.
    with open('data_files/school_genre_data.json') as jsonfile:
        data = json.load(jsonfile)
    # Finds a school who's data will be updated.
    print("\nFirst you must select the school which you'd like to update data for.")
    sleep(.5)
    try:
        school_id = school_search(data)
    except ValueError:
        quit()

    sleep(.5)
    print("\nYou have selected {} as your school.".format(data['schools'][school_id]['name']))

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
            except ValueError:
                quit()    
            
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
    
# For the 'Learn more' option. Teaches how to use this program and it's purpose.
def learn_more():
    sleep(.5)
    print()
    while True:
        choice = input("""What would you like to learn more about?
0 - Viewing data
1 - Searching for school
2 - Adding data
3 - Authenticating Spotify account
4 - Genre score
""")
        sleep(.5)
        if choice == '0':
            print("""
                            ************       VIEWING DATA       ************                              

To view data, the user must first select a school using the school search. After the user has found a school,
the program will look through it's current data to find the top genres of the selected school. If no genres
were found, the program will display that nothing was found, and inform the user to add genre data to the
school. If one or more genres were found, the program will display them along with their genre scores. The 
program will then prompt the user if they would like to see in-depth data. 
""")
            break
        elif choice == '1':
            print("""
                        ************    SEACRING FOR SCHOOL    ************

This is a sequence used for both viewing and adding data. It will first ask the user whether they would like 
to search for schools with states or zip code. Once the user has picked an option they will be asked to input
the respective field. If no results were found, the user will have the choice to either exit the program or 
search again. If valid results were found, the program will list all valid schools which match the field. 
The user must then input their school of choice, search again, or quit.
""")
            break
        elif choice == '2':
            print("""
                        ************      ADDING DATA      ************

To add data, the user must first select a school using the school search. After selecting a school, the user 
must authenticate their Spotify account with the spotify sequence. The program will then check the users top
genres. As the Spotify API does not allow a direct method to view a users top genres, we must calculate it manually.
Top genres are calculated by looking at a users top artists, and the genres which those artists fall in. If no 
genres were found, the program will inform the user that they have no top genres. If one or more genres are found,
the user will be prompted if they would like to add their genre data to their selected school. If the user consents 
to having their data used, the data will be added to the selected schools data.
""")
            break
        elif choice == '3':
            print("""
                        ************AUTHENTICATING SPOTIFY ACCOUNT************

For user authentication through the Spotify API, the user must first input their username. This username can be found
by taking the following path on the Spotify app: settings->account->username. Or on Spotify Desktop: 
profile(top right)->account->username. After the username is given, the program will open Spotify authentication on the 
users browser. The user must then authenticate their account through the Spotify website, copy the redirect link once it's finished,
then paste the link back into the program. If everything is valid, the authentication is successful. If the authentication goes wrong, 
the user will be prompted if they would like to try again.
""")
            break
        elif choice == '4':
            print("""
                        ************      GENRE SCORE      ************

The genre score is the point system this program uses to determine a specific genres popularity. Genre score is added when a 
user adds their genre data to a school. The following system is used for determining how much genre score is added:
#1 Genre: 2000
#2 Genre: 1500
#3 Genre: 1000
This genre score is also added to the in-depth scores when score is added. If a user is a sophomore and adds their genre data,
both the current score and sophomore score go up by the same amount.
""")
            break
        else:
            print("\nInvalid response found, please try again...\n")
            continue
    # Prompts the user if they'd like to continue learning.
    sleep(2)
    while True:
        choice = input("""What would you like to do?
0 - Learn more
1 - Start Universify again
2 - Quit
""")
        if choice == '0':
            learn_more()
        elif choice == '1':
            universify()
        elif choice == '2':
            print("\nThank you for using Universify. Have a great day! :)\n")
            quit()
        else:
            print("\nInvalid response found, please try again...\n")
            continue

# For the 'View existing data' option. Allows the user to look at the top genres of a school.
def view_data():
    # Setting up data.
    data = None 
    # Loading the data from our current data file.
    with open('data_files/school_genre_data.json') as jsonfile:
        data = json.load(jsonfile)
    # Finds a school who's data will be updated.
    print("\nFirst you must select the school which you'd like to view the data for.")
    sleep(.5)
    school_id = school_search(data)
    sleep(.5)
    print("\nYou have selected {} as your school. We will now search for their top genres.".format(data['schools'][school_id]['name']))
    print("\n************    GETTING TOP GENRES    ************\n")
    sleep(.5)

    # Getting the top genres, displays top genres.
    print('Here are the results:')
    top = get_top_three(data['schools'][school_id]['genre_heap'])
    
    if top[0] is None:
        # Handling when there is no data currently
        print("\nUh oh! {} seems to not have any genre data. Please add some data and try again.\n".format(data['schools'][school_id]['name']))
        sleep(.5)
        end_prompt()
    else:
        num = 0
        for i in top:
            # If i is None, this part will be skipped
            if i:
                num+=1
                print(f"""
    {num}. {i['genre'].capitalize()}
    GENRE SCORE: {i['score']}""")
            else:
                pass
    print()
    sleep(.5)
    # Prompts the user if they'd like to see in depth data.
    while True:
        choice = input("""What would you like to do?
0 - View in-depth data
1 - Find a different school
2 - Start Universify again
3 - Quit
""")
        if choice == '0':
            # For finding in-depth data.
            while True:
                choice = input("\nEnter the number of the genre you would like to see in-depth data for: ")
                if choice.isnumeric():
                    index = int(choice)
                    if index <= num and index > 0:
                        genre = top[index-1]
                        print(f"""
Here is the in-depth data for {genre['genre']}...
                              
    FRESHMAN SCORE:     {genre['freshman_score']}
    SOPHOMORE SCORE:    {genre['sophomore_score']}
    JUNIOR SCORE:       {genre['junior_score']}
    SENIOR SCORE:       {genre['senior_score']}
    GRADUATE SCORE:     {genre['graduate_score']}
    UNKNOWN SCORE:      {genre['unknown_score']}
    TOTAL:              {genre['score']}
    """)
                        sleep(.5)
                        break
                    else:
                        print("\nInvalid response found, please try again...")
                        continue
                else:
                    print("\nInvalid response found, please try again...")
                    continue
            continue
        elif choice == '1':
            view_data()
        elif choice == '2':
            universify()
        elif choice == '3':
            print("\nThank you for using Universify. Have a great day! :)\n")
            quit()
        else:
            print("\nInvalid response found, please try again...\n")
            continue

# For looping the program or exiting.
def end_prompt():
    '''
    does something
    '''
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
