"""
211. Design Add and Search Words Data Structure
link: https://leetcode.com/problems/design-add-and-search-words-data-structure/
"""


class WordDictionary:
    """
    Space Complexity: O(T), where T is the total number of characters stored in the Trie.
    """

    def __init__(self):
        self.trie = {}
        self.END = "*"  # Marker to denote the end of a word

    def addWord(self, word: str) -> None:
        """
        Complexity:
            Time: O(N), where N is the length of the word.
        """
        curr_node = self.trie
        for c in word:
            if c not in curr_node:
                curr_node[c] = {}
            curr_node = curr_node[c]

        curr_node[self.END] = {}  # Add end-of-word marker

    #
    def search(self, word: str) -> bool:
        """
        Time: O(26^N), where N is the length of the word,
              but practically O(N) since at most two '.' are allowed (per problem constraints).
        """

        def dfs(index: int, node: dict) -> bool:
            curr_node = node

            for i in range(index, len(word)):
                char = word[i]

                if char == ".":
                    # Explore all possible children
                    for child in curr_node.values():
                        if dfs(i + 1, child):
                            return True
                    # No match found
                    return False
                else:
                    if char not in curr_node:
                        return False
                    curr_node = curr_node[char]

            # Check for end-of-word marker
            return self.END in curr_node

        return dfs(0, self.trie)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
