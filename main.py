import json
from hashAndTrie import Trie

# initialize the Trie
trie = Trie()

dataFile = 'data/meta_Appliances.jsonl'

data = [] # info from data file gets stored in this array, may change when hash and trie implemented ?

with open(dataFile, 'r') as file: # help with loading items from https://amazon-reviews-2023.github.io/
    for line in file:
            item = json.loads(line) # get json object on each line
            title = item.get('title', None) # get title and features from data file
            features = item.get('details', None)

            if title: # if title exists, append to the data array
                info_item = {'title': title,
                             'features': features if features else "No features information"
                             }
                data.append(info_item)
                trie.insert(title.lower(), info_item)

print(data[0]) # shows data format when put in array (just for example)
print(data[4])
print(data[8])


# test for the Trie
title = "ROVSUN Ice Maker Machine Countertop"
results_title = trie.search(title.lower())
print(f"Search results for title '{title}':", results_title, end='')

prefix = "Whirlpool"
results_prefix = trie.startswith(prefix.lower())
print(f"Search results for prefix '{prefix}':", results_prefix, end='')

nonetitle = "none"
results_nonetitle = trie.search(nonetitle.lower())
print(f"Search results for title '{nonetitle}':", results_nonetitle)

print(f"Total items loaded: {len(data)}", end='')