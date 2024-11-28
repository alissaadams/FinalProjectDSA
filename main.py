import json
import hashAndTrie


dataFile = 'data/meta_Appliances.jsonl'

data = [] # info from data file gets stored in this array, may change when hash and trie implemented ?

with open(dataFile, 'r') as file: # help with loading items from https://amazon-reviews-2023.github.io/
    for line in file:
            item = json.loads(line) # get json object on each line
            title = item.get('title', None) # get title and features from data file
            features = item.get('details', None)

            if title: # if title exists, append to the data array
                    data.append({'title': title,
                                 'features': features if features else "No features information"})

print(data[0]) # shows data format when put in array (just for example)
print(data[4])