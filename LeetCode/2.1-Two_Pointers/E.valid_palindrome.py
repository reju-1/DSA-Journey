"""
125. Valid Palindrome
link: https://leetcode.com/problems/valid-palindrome/
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Two pointer solution.
        Time O(n)
        Space O(1)
        """

        s = "".join(s.split(" ")).lower()
        left, right = 0, len(s) - 1

        while left < right:

            if not s[left].isalnum():
                left += 1
                continue

            if not s[right].isalnum():
                right -= 1
                continue

            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True

    def isPalindromeV2(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1

        return True

    def isPalindromeV3(self, s: str) -> bool:

        s = list(filter(str.isalnum, s.lower()))
        # s = [c for c in s.lower() if c.isalnum()]
        return s == s[::-1]
