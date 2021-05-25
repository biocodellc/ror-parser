import json
import itertools

from operator import itemgetter, attrgetter

# read ror file and produce a separate file for each country
with open('ror.json') as json_file:
    data = json.load(json_file)
    namesList = []

    for key in data:
        country = key['country']['country_name']
        country_lowercase = country.lower()
        
        values =  { "name": key["name"], "country": country_lowercase, "types":key['types'] }
        namesList.append(values)
    
    # sort by country
    namesList.sort(key=lambda content: content['country'])

    # then use groupby on country name
    groups = itertools.groupby(namesList, lambda content: content['country'])

    # loop and write country names to file
    for country, group in groups:        
        filename = f'{country}.json'
        filename = filename.replace(" ", "_")

        with open(filename, 'w') as outfile:                                
            count = 0
            outfile.write("[")
            for content in group:
                if (count > 0):
                    outfile.write(",")
                json.dump(content, outfile, indent=1)  
                count = count + 1             
            outfile.write("]")
                
