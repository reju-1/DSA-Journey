"""
680. Valid Palindrome II
link: https://leetcode.com/problems/valid-palindrome-ii/
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        Time: O(N)
        Space: O(N)
        Remarks:
            - Recursive two-pinter
        """

        def helper(l: int, r: int, count: int):
            if count > 1:
                return False
            if l > r:
                return True

            if s[l] == s[r]:
                return helper(l + 1, r - 1, count)
            else:
                return helper(l + 1, r, count + 1) or helper(l, r - 1, count + 1)

        return helper(0, len(s) - 1, 0)

    def validPalindrome(self, s: str) -> bool:
        """
        Time: O(N)
        Space: O(1)
        Approach:
            - Recursive two-pointer technique.
            - When a mismatch is found, try skipping either the left or right character.
            - Allow at most one character to be removed.

        Think:
            - Valid Palindrome III
        """

        def helper(l: int, r: int, popped: int):
            if popped > 1:
                return False

            while l < r:
                if s[l] != s[r]:  # When left and right Characters are not match
                    return helper(l + 1, r, popped + 1) or helper(l, r - 1, popped + 1)
                l += 1
                r -= 1

            return True

        return helper(0, len(s) - 1, 0)

    #
    def validPalindrome(self, s: str) -> bool:
        """
        Time: O(N)
        Space: O(1)
        Remarks:
            - Iterative Two-pointer technique
        """

        def isPalindrome(string: str) -> bool:
            return string == string[::-1]

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                # string: ...xxy...
                # exclude left : ..._xy...
                # exclude right: ...xx_...
                return isPalindrome(s[l:r]) or isPalindrome(s[l + 1 : r + 1])
            l += 1
            r -= 1

        return True
