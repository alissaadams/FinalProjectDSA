import json
import time
from hashAndTrie import Trie
from hashAndTrie import HashMap

def loadDataset():
    # initialize the Trie
    trie = Trie()

    #initialize the Hashmap
    hashmap = HashMap()

    dataFile = 'data/meta_Appliances.jsonl'

    data = [] # info from data file gets stored in this array

    with open(dataFile, 'r') as file: # help with loading items from https://amazon-reviews-2023.github.io/
        for line in file:
                item = json.loads(line) # get json object on each line
                title = item.get('title', None) # get title and features from data file
                features = item.get('details', None)

                if title:
                    title_for_trie = trie.preprocess_title(title)
                    title_for_hash = hashmap.preprocess_title(title)
                    # if title exists, append to the data array
                    info_item = {'title': title,
                                 'features': features if features else "No features information"
                                 }
                    data.append(info_item)
                    trie.insert(title_for_trie, info_item)
                    hashmap.insert(title_for_hash, features)
    return trie, hashmap, data

def compareTime(userInput):
    totalTrieTime = 0
    totalHashTime = 0

    if not userInput:
        print("No input for comparison.")
        return 0, 0

    for title in userInput:
        print(f"Searching for {title}")

        # timing for hash
        startTime = time.perf_counter()
        keyFound = returnedHashMap.findKey(title)
        if keyFound:
            timeforHash = time.perf_counter() - startTime
            print(f"Time taken for hashmap search: {1000000 * timeforHash:.2f} microseconds")
        else:
            timeforHash = 0
            print(f"{title} not found through hashmap")
        totalHashTime += timeforHash

        # timing for trie
        processedTitle = returnedTrie.preprocess_title(title)
        start = time.perf_counter()
        trieKeyFound = returnedTrie.search(processedTitle)

        # Calculates time only if key is found
        if trieKeyFound:
            timeforTrie = time.perf_counter() - start
            print(f"Time taken for trie search: {1000000 * timeforTrie:.2f} microseconds\n")
        else:
            timeforTrie = 0
            print(f"{title} not found through trie\n")
        totalTrieTime += timeforTrie

    # Get averages
    averageTrieTime = totalTrieTime / len(userInput)
    averageHashTime = totalHashTime / len(userInput)

    return averageTrieTime, averageHashTime

def compareAccuracy(userInput):
    hashAccuracyCount = 0
    trieAccuracyCount = 0

    for i in range(len(userInput)):
        keyFound = returnedHashMap.findKey(userInput[i])
        if keyFound == True:
            hashAccuracyCount += 1
        else:
            hashAccuracyCount += 0

        trieKeyFound = returnedTrie.search(userInput[i])
        # print(f"Searching for {userInput[i]} in Trie. Found: {trieKeyFound}")

        if trieKeyFound:
            trieAccuracyCount += 1
        else:
            trieAccuracyCount += 0

    accuracyHash = (hashAccuracyCount / len(userInput)) * 100
    accuracyTrie = (trieAccuracyCount / len(userInput)) * 100

    return accuracyHash, accuracyTrie


def addTitle(titleInput, listOfTitles):
    listOfTitles.append(titleInput)
    return listOfTitles


if __name__ == "__main__":
    # Gets input from user to store in list of titles
    print("Welcome to Appliance Searcher 3000!")
    print("Please enter the title(s) of appliances you want to search for: ")
    print("Type 'done' when you are finished inserting titles.")
    userInput = input("Title: ")
    listOfTitles = []

    while (userInput != 'done'):
        listOfTitles = addTitle(userInput, listOfTitles)
        userInput = input("Title: ")

    print("Loading...") # prints after titles have been inserted

    # Get values and call return functions
    returnedTrie, returnedHashMap, dataLoaded = loadDataset() # outside the function so it only runs loadDataset one time
    avgTrieTime, avgHashTime = compareTime(listOfTitles)
    accuracyOfHash, accuracyOfTrie = compareAccuracy(listOfTitles)

    print("")
    # Checks if there is an average hash time to determine what to display
    if avgHashTime == 0:
        print("There is no average time for the Hashmap function because it "
              "could not find any of the inputted titles.")
    else:
        print(
            f"The average time for finding the key with the hash structure is {1000000 * avgHashTime:.2f} microseconds")

    # Checks if there is an average trie time to determine what to display
    if avgTrieTime == 0:
        print(f"There is no average time for the Trie function because it "
              "could not find any of the inputted titles.")
    else:
        print(f"The average time for finding the key with the trie structure is {1000000 * avgTrieTime:.2f} microseconds")

    # If accuracy of hash or accuracy of trie exist, display the percentage. If not, title not found
    if (accuracyOfHash or accuracyOfTrie):
        print(f"\nThe accuracy in finding the searched keys for hashmap is {accuracyOfHash:.2f}%, and for trie is {accuracyOfTrie:.2f}%")
    else:
        print("No accuracy can be calculated because no titles were found.")

    ## list below is for running and testing
    #
    #                   ["ROVSUN Ice Maker Machine Countertop, Make 44lbs Ice in 24 Hours, Compact & Portable Ice Maker with Ice Basket for Home, Office, Kitchen, Bar (Silver)", "HANSGO Egg Holder for Refrigerator",
    #                    "154567702 Dishwasher Lower Wash", "Whirlpool W10918546 Igniter",
    #                    "1841N030 - Brown Aftermarket Replacement Stove Range Oven Drip Bowl Pan"]
