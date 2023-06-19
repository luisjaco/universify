# This file is for functions relating to searching through the json data to find a vaild school.
import json

def school_search(data=None):
    print("\n************      SCHOOL SEARCH      ************\n")

    # If no valid data is given, data will be taken from the following file
    if data is None:
        with open('data_files/school_genre_data.json') as jsonfile:
            data = json.load(jsonfile)
    
    # Asking the user how they would like to search for a school. The function will loop until a valid key is found.
    term, key = None, None
    while True:
        choice = input("""How would you like to search for a school?
0 - State
1 - ZIP Code
""")
        if choice == '0':
            term = input("Which state are you searching?: ").upper()
            key = 'state'
            break
        elif choice == '1':
            term = input("What is the zip code you're searching with?: ")
            key = 'zip'
            if not term.isnumeric():
                print("\nNon-valid zip found, please try again...\n")
                continue
            else:
                break
        else:
            print("\nNon-valid key found, please try again...\n")
            continue
        
    # Searches for school in data file, prints all found schools
    # We keep track of the found ids, and if anything was found in general.
    found = False
    found_ids = set()
    print("\n************    COMMENCING SEARCH    ************\n")
    for item in data['schools']:
        # Prints out all found data
        if item[key] == term and not found:
            found = True
            print("Here are the results:")
            print("{}. {}".format(item['id'], item['name']))
            found_ids.add(item['id'])
        elif item[key] == term:
            print("{}. {}".format(item['id'], item['name']))
            found_ids.add(item['id'])
    if not found:
        # If nothing is found, the user will decide whether or not they want to try again.
        print("There were no results; double check if the fields were correct or try searching with a different method.")
        return restart(data)
    else:
        while True:
            # Asks user for which college (out of shown colleges) they would like to pick
            choice = input("Which college would you like to look up? (if school not found enter N): ").upper()
            if choice == 'N':
                return restart(data)
            elif choice.isnumeric() and int(choice) in found_ids:
                # Displays the chosen colleges information
                selected_data = data['schools'][int(choice)]
                print("""
    Here is your selected schools data:
    Name:       {}
    Zip:        {}
    State:      {}
    Website:    {}
                """.format(selected_data['name'], selected_data['zip'], selected_data['state'], selected_data['website']))
                prompt = input("""What would you like to do?
0 - Select school
1 - Search again
2 - Quit program
""")
                if prompt == '0':
                    return int(choice)
                elif prompt == '1':
                    return school_search(data)
                else:
                    quit()
            else:
                print("\nNon-valid response found, please try again...\n")

# Handles whether the user wants to try searching again or quit the program.
def restart(data):
    prompt = input("""
What would you like to do?
0 - Search again
1 - Quit program
""")
    if prompt == '0':
        return school_search(data)
    else:
        quit()
