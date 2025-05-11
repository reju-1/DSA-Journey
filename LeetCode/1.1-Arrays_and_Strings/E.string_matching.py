"""
28. Find the Index of the First Occurrence in a String
link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Time: O(N*M)
        Space: O(1)
        Remarks:
            - Naive approach
        """
        n, m = len(haystack), len(needle)

        if n < m:
            return -1

        for i in range(n - m + 1):
            # if haystack[i : i + m] == needle:
            #     return i

            j = 0
            while j < m and haystack[i + j] == needle[j]:
                j += 1
            if j == m:
                return i

        return -1
