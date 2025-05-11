"""
290. Word Pattern
link: https://leetcode.com/problems/word-pattern/
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        Time: O(N)
        Space: O(N)
        Remarks:
            - Bidirectional character-to-word mapping using 2 HashMaps.
            - Similar to LC 205: Isomorphic Strings(must see this).
        """
        words = s.split(" ")
        charToWord = {}
        wordToChar = {}

        if len(pattern) != len(words):
            return False

        for c, w in zip(pattern, words):
            if c in charToWord and charToWord[c] != w:
                return False
            if w in wordToChar and wordToChar[w] != c:
                return False
            charToWord[c] = w
            wordToChar[w] = c

        return True
