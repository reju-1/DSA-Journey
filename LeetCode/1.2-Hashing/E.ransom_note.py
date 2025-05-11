"""
383. Ransom Note
link: https://leetcode.com/problems/ransom-note/
"""

from collections import Counter


class Solution:
    def canConstructV1(self, ransomNote: str, magazine: str) -> bool:
        """
        Time: O(N + M)
        Space: O(1), because the character set is limited to 26 lowercase English letters.
        Remarks:
            - 2-counter solution
        """
        c1 = Counter(ransomNote)
        c2 = Counter(magazine)
        # return c1 & c2 == c1  # Minimum counts of common elements(c1 & c2) is Equals to c1

        for key, val in c1.items():
            if c2.get(key, 0) < val:
                return False

        return True

    def canConstructV2(self, ransomNote: str, magazine: str) -> bool:
        """
        Time: O(N + M)
        Space: O(1)
        Remarks:
            - 1-counter solution
        """
        frequency = Counter(magazine)

        for char in ransomNote:
            if frequency[char] == 0:  # Note: Missing keys return 0 in Counter
                return False
            frequency[char] -= 1

        return True

    def canConstructV3(self, ransomNote: str, magazine: str) -> bool:
        """
        Time: O(N + M)
        Space: O(1)
        Remarks:
            - Using Array
        """
        freq = [0] * 26
        for char in magazine:
            freq[ord(char) - ord("a")] += 1

        for char in ransomNote:
            index = ord(char) - ord("a")
            freq[index] -= 1
            if freq[index] < 0:
                return False

        return True
