"""
58. Length of Last Word
link: https://leetcode.com/problems/length-of-last-word/
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        Time: O(N)
        Space: O(1)
        """
        length = 0
        start = len(s) - 1

        while s[start] == " ":  # Escape white spaces from end
            start -= 1

        for char in s[start::-1]:
            if char == " ":
                break
            length += 1

        return length

    def lengthOfLastWord(self, s: str) -> int:
        """
        Time: O(N)
        Space: O(1)
        Remarks:
            - Concise
            - A more concise version `s.split(" ")[-1]` but uses O(N) extra space.
        """
        length = 0

        for char in s[::-1]:
            if char == " " and length != 0:  # Termination condition
                break

            if char != " ":
                length += 1

        return length
