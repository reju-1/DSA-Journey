"""
242. Valid Anagram
link: https://leetcode.com/problems/valid-anagram/description/
"""
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c1 = Counter(s)
        c2 = Counter(t)
        return c1 == c2
