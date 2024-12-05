import json
import time
from hashAndTrie import Trie
from hashAndTrie import HashMap


def loadDataset():
    # initialize the Trie
    trie = Trie()

    # initialize the Hashmap
    hashmap = HashMap()

    dataFile = 'data/meta_Appliances.jsonl'

    data = []  # info from data file gets stored in this array

    with open(dataFile, 'r') as file:  # help with loading items from https://amazon-reviews-2023.github.io/
        for line in file:
            item = json.loads(line)  # get json object on each line
            title = item.get('title', None)  # get title and features from data file
            features = item.get('details', None)

            if title:
                titleForTrie = trie.preprocess_title(title)
                titleForHash = hashmap.preprocess_title(title)
                # if title exists, append to the data array
                infoItem = {'title': title,
                            'features': features if features else "No features information"
                            }
                data.append(infoItem)
                trie.insert(titleForTrie, infoItem)
                hashmap.insert(titleForHash, features)
    return trie, hashmap, data


def compareTime(userInputList):
    totalTrieTime = 0
    totalHashTime = 0

    for title in userInputList:
        isTitle = '' # initializes title

        print(f"Searching for {title}")

        # timing for hash
        startTime = time.perf_counter()
        hashKeyFound = returnedHashMap.findKey(title)
        timeforHash = time.perf_counter() - startTime

        # Displays time of hash differently depending if title was found
        if hashKeyFound:
            print(f"Time taken for hashmap search: {1000000 * timeforHash:.2f} microseconds")
        else:
            print(f"'{title}' not found through hashmap. Search time: {1000000 * timeforHash:.2f}")

        totalHashTime += timeforHash

        # timing for trie
        start = time.perf_counter()
        trieKeyFound = returnedTrie.search(title)
        timeforTrie = time.perf_counter() - start

        # Displays time of trie different depending on if title was found
        if trieKeyFound:
            # Since the trie searches based on letters not exact matches, ask user if title correct
            print(f"Found: '{trieKeyFound[0]['title']}', is this your title?")
            isTitle = input("Input Y or N: ").lower()

            # Different output based on accuracy of title found
            if (isTitle == 'y'):
                print(f"Time taken for trie search: {1000000 * timeforTrie:.2f} microseconds\n")
            elif (isTitle == 'n'):
                print(f"'{title}' not found through trie. Search time: {1000000 * timeforTrie:.2f}\n")

        else:
            print(f"'{title}' and no relevant titles found through trie. Search time: {1000000 * timeforTrie:.2f}")
        totalTrieTime += timeforTrie

    # Get averages to display
    averageTrieTime = totalTrieTime / len(userInputList)
    averageHashTime = totalHashTime / len(userInputList)

    return averageTrieTime, averageHashTime, isTitle # is title is returned to use for accuracy


def compareAccuracy(userInputList, isTitleCorrect):
    hashAccuracyCount = 0
    trieAccuracyCount = 0
    lengthUserInputList = len(userInputList)

    # Checks trie and hashmap if keys exist
    for i in range(lengthUserInputList):
        # Increments counter for accuracy if key in hashmap
        hashKeyFound = returnedHashMap.findKey(userInputList[i])
        if hashKeyFound == True:
            hashAccuracyCount += 1
        else:
            hashAccuracyCount += 0

        # Increments counter for accuracy if key in trie AND if the title is what the users looking for
        trieKeyFound = returnedTrie.search(userInputList[i])
        if trieKeyFound and isTitleCorrect == 'y':
            trieAccuracyCount += 1
        else:
            trieAccuracyCount += 0

    # Calculates the accuracy based on the number of titles and how many are correct for each
    accuracyHash = (hashAccuracyCount / len(userInputList)) * 100
    accuracyTrie = (trieAccuracyCount / len(userInputList)) * 100

    return accuracyHash, accuracyTrie


def addTitle(titleInput, listOfTitles):
    listOfTitles.append(titleInput)
    return listOfTitles


def main():
    # Variables used in other functions
    global returnedTrie
    global returnedHashMap
    global dataLoaded

    listOfTitles = []

    print("---------------------------------------")
    print("Welcome to the Appliance Searcher 3000!")
    print("---------------------------------------")

    # Gets input from user to store in list of titles
    print("Please enter the title(s) of appliances you want to search for: ")
    print("Type 'done' when you are finished inserting titles.")

    userInput = input("Title: ")

    # Gets however many titles user wants
    while (userInput != 'done'):
        # makes sure input isn't empty
        if (userInput != ''):
            listOfTitles = addTitle(userInput, listOfTitles)
        else:
            print("No input, please try again.")

        userInput = input("Title: ")

    print("Loading...")

    # Get values and call return functions
    returnedTrie, returnedHashMap, dataLoaded = loadDataset()
    avgTrieTime, avgHashTime, isTitleCorrect = compareTime(listOfTitles)
    accuracyOfHash, accuracyOfTrie = compareAccuracy(listOfTitles, isTitleCorrect)

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
        print(
            f"The average time for finding the key with the trie structure is {1000000 * avgTrieTime:.2f} microseconds")

    # If accuracy of hash or accuracy of trie exist, display the percentage. If not, title not found
    if (accuracyOfHash or accuracyOfTrie):
        print(
            f"\nThe accuracy in finding the searched keys for hashmap is {accuracyOfHash:.2f}%, and for trie is {accuracyOfTrie:.2f}%")
    else:
        print("\nNo accuracy can be calculated because no titles were found.")


if __name__ == "__main__":
    main()

    ## list below is for running and testing

    # HANSGO Egg Holder for Refrigerator
    # Whirlpool W10918546 Igniter