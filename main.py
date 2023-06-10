from school_search import search
import json

with open('data_files/us_schools.json') as jsonfile:
    data = json.load(jsonfile)

search(data)