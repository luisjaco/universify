# This file is for making a json file using the existing school data csv file.
import json, csv

data = {"schools" : []}
# Opening the csv file.
with open('data_files/school_all_data.csv') as csvfile:
    # Creates new dictionaries for each school, with the following keys:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data['schools'].append({
            "id" : int(row['id'])-1,
            "name" : row['name'],
            "state" : row['state'],
            "zip" : row['zip'],
            "website" : row['website'],
            "genre_heap" : [None],
            "genre_positions" : {}
        })
# Creating the json file.
with open("data_files/school_genre_data.json", 'w') as jsonfile:
    json.dump(data, jsonfile, indent=4)
