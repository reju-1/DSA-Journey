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
            # Remove characters from the left until the duplicate is removed
            while char in hash_set:
                hash_set.remove(s[left])
                left += 1

            hash_set.add(char)
            # count = max(count, len(hash_set))
            count = max(count, right - left + 1)

        return count

    def lengthOfLongestSubstring(self, s: str) -> int:

        hash_map = {}  # {char: index}
        left = count = 0

        for right, char in enumerate(s):
            # If char is in the map and within the current window
            if char in hash_map and hash_map[char] >= left:
                left = hash_map[char] + 1  # left = prev_occurrence + 1

            window = right - left + 1
            count = max(count, window)
            hash_map[char] = right  # Update last seen index

        return count
