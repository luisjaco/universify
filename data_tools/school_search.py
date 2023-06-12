
def search(data):
    print("\nWELCOME TO LUIS' COLLEGE FINDER!\n")
    key, term = None, None
    while True:
        key = input("Would you like to search for colleges using zip or state? (zip/state): ")

        if key == 'state':
            term = input("Which state are you searching with?: ")
            break
        elif key == 'zip':
            term = input("What is the zip code you're searching with?: ")
            break
        else:
            print("\nERROR\nNon-valid key found, please try again...\n")
            continue

    print("Commencing search...")
    found = False
    for item in data['schools']:
        if item[key] == term and not found:
            found = True
            print("Here are the results:")
            print("{}. {}".format(item['id'], item['name']))
        elif item[key] == term:
            print("{}. {}".format(item['id'], item['name']))
    if not found:
        print("\nThere were no results; double check if the fields were correct or try searching with a different method")
        return restart(data)
    else:
        while True:
            choice = input("Which college would you like to look up? (if school not found enter N): ")
            if choice == 'N':
                return restart(data)
            elif choice.isnumeric():
                selected_data = data['schools'][int(choice)]
                print("""
                Here is your selected schools data:
                Name:       {}
                Zip:        {}
                State:      {}
                Website:    {}
                """.format(selected_data['name'], selected_data['zip'], selected_data['state'], selected_data['website']))
                return restart(data)
            else:
                print("\nERROR\nNon-valid response found, please try again...\n")
        
def restart(data):
    choice = input("\nWould you like to do another search? (y/n): ")
    if choice == 'y':
        return search(data)
    else:
        return goodbye()
    
def goodbye():
    print("THANK YOU FOR USING LUIS' COLLEGE FINDER")
