"""
567. Permutation in String
link: https://leetcode.com/problems/permutation-in-string/
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Time: O(26*n) = O(n)
        Space: O(26) = O(1)
        Technique: Fixed-size sliding window
        """

        len_s1, len_s2 = len(s1), len(s2)

        if len_s1 > len_s2:
            return False

        s1_count, s2_count = [0] * 26, [0] * 26

        for c1, c2 in zip(s1, s2[:len_s1]):  # Building up the window
            s1_count[ord(c1) - ord("a")] += 1
            s2_count[ord(c2) - ord("a")] += 1

        if s1_count == s2_count:  # initial window matches?
            return True

        # Slide the window across s2
        for i in range(len_s1, len_s2):
            s2_count[ord(s2[i]) - ord("a")] += 1  # adding a char in window
            s2_count[ord(s2[i - len_s1]) - ord("a")] -= 1  # Remove leftmost char

            if s1_count == s2_count:  # O(26) check, which is O(1)
                return True

        return False
