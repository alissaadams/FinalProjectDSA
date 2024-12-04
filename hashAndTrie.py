import string

class keyValPair:
    def __init__(self, key=-1, val=-1):
        self.key = key
        self.val = val

class HashMap:
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.size = 0
        # initialize the storage structure(buckets) of the hash table
        self.buckets = []
        for _ in range(capacity):
            self.buckets.append(None)

    def preprocess_title(self, title):
        if not isinstance(title, str):
            title = str(title)
        return title.strip().lower()
    # define a hash function that maps keys to index positions in the hash table
    def hash(self, key):
        key = self.preprocess_title(key)
        # return an index to find the buckets(
        return hash(key) % self.capacity

    # going to handle collisions through open addressing, probably just linear probe.
    def insert(self, key, val):
        key = self.preprocess_title(key)
        # Check if the load factor exceeds the threshold
        if self.size / self.capacity > 0.75:
            # if does, resize the capacity
            self.resize()
        index = self.hash(key)

        for _ in range(self.capacity):
            if self.buckets[index] is None or self.buckets[index].key == key:
                self.buckets[index] = keyValPair(key, val)
                self.size += 1
                return
            index = (index + 1) % self.capacity

    def resize(self):
        # If it is already expanding, return
        if hasattr(self, '_resizing') and self._resizing:
            return
        self._resizing = True

        current_buckets = self.buckets
        self.capacity *= 2
        # reset the current element count for all key pairs will reinsert during capacity expansion
        self.size = 0
        self.buckets = []
        for _ in range(self.capacity):
            self.buckets.append(None)
        # key pairs reinsert
        for new_bucket in current_buckets:
            if new_bucket != None:
                self.insert(new_bucket.key, new_bucket.val)

    def findKey(self, key):
        key = self.preprocess_title(key)
        # calculates the hash value of the key and maps it to the bucket index
        index = self.hash(key)
        for _ in range(self.capacity):
            # if the buckets are empty, the key does not exist
            if self.buckets[index] is None:
                return False
            if self.buckets[index].key == key:
                return True
            # move to the next buckets use linearly detects
            index = (index + 1) % self.capacity
        return False


    #
    # load_factor = 0.75
    # def __init__(self):
    #     self.capacity = 10
    #     self.size = 0
    #     self.hashmap = [KeyValPair() for _ in range(self.capacity)]
    #
    # def hash(self, key):
    #     return key % self.capacity
    #
    # # going to handle collisions through open addressing, probably just linear probe.
    # def insert(self, key: int, value: string):
    #     hashed_key = self.hash(key)
    #     bucket = self.hashmap[hashed_key]
    #     #unfinished
    #
    # def get(self,key):
    #

    #don't need a remove function




class TrieNode:
    def __init__(self):
        self.children = {}
        self.node_info = []
        self.word_completed = False

    def end_word(self):
        self.word_completed = True

    def not_end_word(self):
        self.word_completed = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Standardize the title string.
    def preprocess_title(self, title):
        return title.strip().lower()

    def insert(self, title, title_info):
        title = self.preprocess_title(title)
        node = self.root

        # traverse each character in the title
        for char in title:
            # check if the character not exists in the current node's children
            if char not in node.children:
                # create a new child node for this character
                node.children[char] = TrieNode()
            node = node.children[char]
            
        if title_info not in node.node_info:
            # add the information of the title
            node.node_info.append(title_info)
        # mark the current node as the end of the word to indicate this path has a complete word
        node.end_word()

    # Search for a title in the Trie.
    def search(self, title):
        title = self.preprocess_title(title)
        exactly_search = self.exactlysearch(title)
        # Try if it is exactly match
        if exactly_search:
            return exactly_search
        # if not, try the prefix way
        prefix_search = self.startswith(title)
        if prefix_search:
            return prefix_search
        # if not find, return false
        return False

    # use for exactly matches search
    def exactlysearch(self, title):
        title = self.preprocess_title(title)
        node = self.root

        # traverse each character in the title string
        for char in title:
            if char in node.children:
                node = node.children[char]

            # if the character not exits in the node of children indicates the title not exits
            else:
                return False

        # check if the current node is the last character of a completed word
        if node.word_completed:
            return node.node_info
        else:
            return False

    # use for prefix matches search
    def startswith(self, prefix):
        prefix = self.preprocess_title(prefix)
        node = self.root
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                # Prefix not found
                return []
        # The prefix path exists, gather all relevant title information starting from this node
        return self.all_title_info(node)

    def all_title_info(self, node):
        # use to store all title information
        results = []
        if node.word_completed:
            results.extend(node.node_info)

        # traversal all child nodes of the current node
        for childnode in node.children.values():
            results.extend(self.all_title_info(childnode))
        # Return the results list containing all title information
        return results
