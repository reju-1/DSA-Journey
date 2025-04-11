"""
208. Implement Trie (Prefix Tree)
link: https://leetcode.com/problems/implement-trie-prefix-tree/

Overview:
    A Trie, also known as a digital tree or prefix tree, is a specialized search tree data structure
    used to efficiently store and retrieve strings, especially useful for prefix-based lookups.

    The word "trie" comes from the middle of the word "retrieval." It is an "M-ary" tree where each node
    represents a character, and paths from the root to leaves represent words.

    Applications:
        - Autocomplete and search suggestions
        - Spell checking
        - Web search engines
        - Full text search
        - IP routing (e.g., longest prefix match)
        - Dictionary word validation
        - Genome sequencing (bio-informatics)

    Common Trie implementations:
        1. Array-based using fixed-size lists (efficient for small alphabets like a-z)
        2. HashMap-based using nested dictionaries (lightweight and Pythonic)
        3. Node-based using a TrieNode class with a dictionary or array of children
        4. Radix tree (also known as a compact prefix tree or compressed trie)

    This script includes both Node-based and HashMap-based implementations.

    Learn more: https://en.wikipedia.org/wiki/Trie
"""


# -----------------------------Node based Implementation-------------------------
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_word = False  # Indicates the end of a valid word


class Trie:
    def __init__(self):
        self.head = TrieNode()

    def insert(self, word: str) -> None:
        curr: TrieNode = self.head

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()  # Create a new node for the character
            curr = curr.children[char]  # Move to the child node for this character

        curr.end_word = True  # Mark the end of the word

    def search(self, word: str) -> bool:
        curr = self.head
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]  # Move to the next node

        return curr.end_word  # True only if it's a complete word

    def startsWith(self, prefix: str) -> bool:
        curr = self.head
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]  # Move to the next node

        return True  # All characters in prefix found, so it exists


# ---------------------------------HashMap Implementation--------------------------
END = "*"  # Marks as end of word


class Trie:
    def __init__(self):
        self.head = {}

    def insert(self, word: str) -> None:
        curr_node = self.head
        for char in word:
            if char not in curr_node:
                curr_node[char] = {}  # Create a new nested dictionary for the character
            curr_node = curr_node[char]

        curr_node[END] = END  # Mark the end of the word

    def search(self, word: str) -> bool:
        curr_node = self.head
        for char in word:
            if char not in curr_node:
                return False
            curr_node = curr_node[char]

        return END in curr_node

    def startsWith(self, prefix: str) -> bool:
        curr = self.head
        for char in prefix:
            if char not in curr:
                return False
            curr = curr[char]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
