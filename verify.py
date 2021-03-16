import json # import json module

# This function will iterate through the data
# and check that all the keys exists in each mushroom entry
def verifyData():
    # Create the list of each required entry
    required_keys = ['name_lat', 'color', 'hymenium', 'hymenium_attachment',
        'cap', 'stipe', 'ecology', 'edible', 'division', 'class', 'order', 'family',
        'genus', 'spore_print']

    # Enter the json data correctly with some weird keyword
    with open('data.json') as json_file:
        data = json.load(json_file)
        i = 0
        for p in data['mushrooms']: # Loop through each mushroom
            for entry in required_keys: # Loop through and check each entry
                if entry not in p:
                    raise ValueError(entry + ' missing from entry with index ' + str(i))
            # If we got to here we check the spore_print
            if 'color' not in p['spore_print'] or 'literal' not in p['spore_print']:
                raise ValueError('spore_print key incorrect in entry with name ' + p['name_lat'])
            i += 1 # Increment the counter
    
    print("SUCESSFULLY VERIFIED THE DATASET AND IT HAS ALL THE REQUIRED KEYS")

verifyData()