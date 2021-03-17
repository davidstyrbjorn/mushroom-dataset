import json # import json module

# This function will iterate through the data
# and check that all the keys exists in each mushroom entry
def verifyData():
    # Create the list of each required entry
    required_keys = ['name_lat', 'color', 'hymenium', 'hymenium_attachment',
        'cap', 'stipe', 'ecology', 'edible', 'classification', 'spore_print']
    required_classification_keys = ['division', 'class', 'order', 'family', 'genus']

    # Enter the json data correctly with some weird keyword
    with open('data.json') as json_file:
        data = json.load(json_file)
        i = 0
        for p in data['mushrooms']: # Loop through each mushroom
            for entry in required_keys: # Loop through and check each entry
                if entry not in p:
                    return (entry + ' missing from entry with index ' + str(i))
            # If we got to here we check the spore print fields
            if 'color' not in p['spore_print'] or 'literal' not in p['spore_print']:
                return ('spore_print key incorrect in entry with name ' + p['name_lat'])
            # If we got to here we check the classification fields
            for entry in required_classification_keys:
                if entry not in p['classification']:
                    return (entry + ' missing from classification entry with name ' + p['name_lat'])
            i += 1 # Increment the counter
    
    return ("SUCESSFULLY VERIFIED THE DATASET AND IT HAS ALL THE REQUIRED KEYS")

print(verifyData())