"""
155. Min Stack
link: https://leetcode.com/problems/min-stack/
"""

from collections import deque


class MinStack:
    """
    Time: O(1) for all operations
    Space: O(n)

    Note:
        This is 2 stack approach but there exist more space efficient solution (One stack).
    """

    def __init__(self):
        # stack = [(value, min-at-this-level), (....), (...),]

        self.stack = deque()

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            return self.stack.append((val, val))

        min_val = min(val, self.getMin())
        self.stack.append((val, min_val))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
