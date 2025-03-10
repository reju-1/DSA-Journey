"""
3. Longest Substring Without Repeating Characters
link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Time: O(n)
        Space: O(m) Where m is the total number of unique characters in the string.
        """

        hash_set = set()
        left = count = 0

        for right, char in enumerate(s):

            while char in hash_set:  # remove upto duplicate character
                hash_set.remove(s[left])
                left += 1

            hash_set.add(char)
            # count = max(count, len(hash_set))
            count = max(count, right - left + 1)

        return count
