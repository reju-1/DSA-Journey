"""
392. Is Subsequence
link: https://leetcode.com/problems/is-subsequence/
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """Single pointer"""

        cursor = 0
        for c in t:
            if cursor == len(s):
                return True

            if c == s[cursor]:
                cursor += 1

        return cursor == len(s)

    def isSubsequence(self, s: str, t: str) -> bool:
        """Two pointer"""
        sp, tp = 0, 0

        while sp < len(s) and tp < len(t):
            if s[sp] == t[tp]:
                sp += 1
            tp += 1

        return sp == len(s)

    def isSubsequence(self, s: str, t: str) -> bool:
        """with linier recursion."""

        def helper(sp: int, tp: int):
            if sp == len(s):
                return True
            if tp == len(t):
                return False

            if s[sp] == t[tp]:
                return helper(sp + 1, tp + 1)
            else:
                return helper(sp, tp + 1)

        return helper(sp=0, tp=0)
