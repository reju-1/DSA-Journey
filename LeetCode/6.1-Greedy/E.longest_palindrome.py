"""
409. Longest Palindrome
link: https://leetcode.com/problems/longest-palindrome/
"""


class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashSet = set()
        count = 0

        for char in s:
            if char in hashSet:
                count += 2  # encounter twice
                hashSet.remove(char)
            else:
                hashSet.add(char)

        if hashSet:  # Not empty means there exist odd number of char
            count += 1

        return count
