import json
import time
from hashAndTrie import Trie
from hashAndTrie import HashMap

def loadDataset():
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
                    HashMap.insert(title, features)
    return trie, data


def compare():
    userInput = input("Please insert title of appliance: \n")
    print("Searching...")
    trieCompare, dataLoaded = loadDataset()

    # timing for hash
    startTime = time.time()
    hashRes = HashMap.findKey(userInput)
    if hashRes == True:
        timeHash = time.time() - startTime
    else:
        print("Title not found through hashmap")

    # timing for trie
    start = time.time()
    trieCompare.search(userInput.lower())
    timeTrie = time.time() - start

    if hashRes == True:
        print(f"Time taken for hashmap search: {timeHash:.10f} seconds")
    print(f"Time taken for trie search: {timeTrie:.10f} seconds")

if __name__ == "__main__":
    compare()


# print(data[0]) # shows data format when put in array (just for example)
# print(data[4])
# print(data[8])
#
#
# # test for the Trie
# title = "ROVSUN Ice Maker Machine Countertop"
# results_title = trie.search(title.lower())
# print(f"Search results for title '{title}':", results_title, end='')
#
# prefix = "Whirlpool"
# results_prefix = trie.startswith(prefix.lower())
# print(f"Search results for prefix '{prefix}':", results_prefix, end='')
#
# nonetitle = "none"
# results_nonetitle = trie.search(nonetitle.lower())
# print(f"Search results for title '{nonetitle}':", results_nonetitle)
#
# print(f"Total items loaded: {len(data)}", end='')
