"""
20. Valid Parentheses
link: https://leetcode.com/problems/valid-parentheses/description/
"""


class Solution:
    def isValid(self, s: str) -> bool:
        """
        Time O(n)
        Space O(n)
        """

        closing_pair = {
            ")": "(",
            "}": "{",
            "]": "[",
        }

        stack = []
        for c in s:
            if c in "({[":
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                if closing_pair[c] != stack.pop():
                    return False

        return len(stack) == 0
