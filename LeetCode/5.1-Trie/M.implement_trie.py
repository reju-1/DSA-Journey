"""
208. Implement Trie (Prefix Tree)
link: https://leetcode.com/problems/implement-trie-prefix-tree/
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
class Trie:
    def __init__(self):
        pass

    def insert(self, word: str) -> None:
        pass

    def search(self, word: str) -> bool:
        pass

    def startsWith(self, prefix: str) -> bool:
        pass


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
