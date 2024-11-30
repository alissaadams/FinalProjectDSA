import json

class HashMap:
    hashMap = {}

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

    def insert(self, title, title_info):
        node = self.root

        # traverse each character in the title
        for char in title:
            # check if the character exists in the current node's children
            if char in node.children:
                node = node.children[char]
            # if not exits, create a new child node for this character
            else:
                node.children[char] = TrieNode()

        # mark the current node as the end of the word to indicate this path has a complete word
        node.end_word()
        # add the information of the title
        node.node_info.append(title_info)

    def search(self, title):
        node = self.root

        # traverse each character in the title string
        for char in title:
            if char in node.children:
                node = node.children[char]

            # if the character not exits in the node of children indicates the title not exits
            else:
                return []

        # check if the current node is the last character of a completed word
        if node.word_completed:
            return node.node_info
        else:
            return []


    def startswith(self, prefix):
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
