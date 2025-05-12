"""
13. Roman to Integer
link: https://leetcode.com/problems/roman-to-integer/
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Time: O(N)
        Space: O(1)
        Remarks:
            - Subtractive notation is the key (e.g. IV = 4, IX = 9).
            - Subtract if current symbol is less than the next one.
        """

        total = 0
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        for i, ch in enumerate(s):
            if i + 1 < len(s) and roman[ch] < roman[s[i + 1]]:
                total -= roman[ch]
            else:
                total += roman[ch]

        return total
