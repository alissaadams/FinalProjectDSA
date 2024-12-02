import json
import time
import random
from hashAndTrie import Trie
from hashAndTrie import HashMap


def loadDataset():
    # initialize the Trie
    trie = Trie()

    dataFile = 'data/meta_Appliances.jsonl'

    data = [] # info from data file gets stored in this array

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


def compareTime(userInput):
    print(f"Searching for {userInput}")

    # values are used in the accuracy function, they count how many times a search is successful
    hashAccuracyCount = 0
    trieAccuracyCount = 0
    timeHash = 0 # can't run without having this defined first

    # timing for hash
    startTime = time.perf_counter()
    keyFound = HashMap.findKey(userInput)
    if keyFound == True:
        timeHash = time.perf_counter() - startTime
        hashAccuracyCount += 1
        print(f"Time taken for hashmap search: {1000000 * timeHash:.10f} microseconds")
    else:
        print("Title not found through hashmap")

    # timing for trie
    start = time.perf_counter()
    returnedTrie.search(userInput.lower())
    timeTrie = time.perf_counter() - start
    print(f"Time taken for trie search: {1000000 * timeTrie:.10f} microseconds\n")
    trieAccuracyCount += 1

    return trieAccuracyCount, hashAccuracyCount, timeTrie, timeHash

def compareAccuracy():
    numCorrectHash = 0
    numCorrectTrie = 0

    # Fixed list to mix specific and shortened titles
    listForAccuracy = ["ROVSUN Ice Maker Machine Countertop", "HANSGO Egg Holder for Refrigerator",
                       "154567702 Dishwasher Lower Wash", "Whirlpool W10918546 Igniter",
                       "1841N030 - Brown Aftermarket Replacement Stove Range Oven Drip Bowl Pan"]


    for i in range(5):
        trieCount, hashCount, _, _ = compareTime(listForAccuracy[i])
        numCorrectTrie += trieCount
        numCorrectHash += hashCount

        accuracyHash = (numCorrectHash / 5) * 100
        accuracyTrie = (numCorrectTrie / 5) * 100

    print(f"The accuracy in finding the searched keys for hashmap is {accuracyHash}%, and for trie is {accuracyTrie}%")


def multipleIterations(dataLoaded): # function calls the compare time function for random values in the data set
    avgHashTime = 0
    avgTrieTime = 0

    for i in range(5):
        randomNum = random.randint(0, 99000)
        input = dataLoaded[randomNum]['title']
        _, _, trieTime, hashTime = compareTime(input) # using underscores because first two values are not needed in this function
        avgHashTime += hashTime
        avgTrieTime += trieTime

    avgHashTime = avgHashTime / 5
    avgTrieTime = avgTrieTime / 5

    print(f"The average time for finding the key with the hash structure is {1000000 * avgHashTime:.10f} microseconds, and with"
          f" the trie structure, it is {1000000 * avgTrieTime:.10f} microseconds")

if __name__ == "__main__":
    print("Selecting random titles from data to search for, please wait.")
    returnedTrie, dataLoaded = loadDataset()  # outside the function so it only runs loadDataset one time
    multipleIterations(dataLoaded)

    print("Now we'll determine accuracy for both hashmap and trie based on full "
          "titles from the data set and shortened versions: \n")
    compareAccuracy()