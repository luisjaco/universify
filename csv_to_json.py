import json, csv

data = {"schools" : []}
with open('data_files/us_colleges_and_universities.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data['schools'].append({
            "id" : int(row['id'])-1,
            "name" : row['name'],
            "state" : row['state'],
            "zip" : row['zip'],
            "website" : row['website'],
            "genre list" : []
        })

with open("new-json-file.json", 'w') as jsonfile:
    json.dump(data, jsonfile, indent=4)