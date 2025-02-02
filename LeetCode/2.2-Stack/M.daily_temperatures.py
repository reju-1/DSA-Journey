"""
739. Daily Temperatures
link: https://leetcode.com/problems/daily-temperatures/
"""


class Solution:
    """
    Iteration from reverse direction
    Time: O(n)
    Space: O(n)
    """

    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        results = [0] * len(temperatures)
        stack = []  # (Temperature, index)

        for i, t in enumerate(temperatures[::-1]):

            while stack and stack[-1][0] <= t:
                stack.pop()

            if not stack:  # stack is empty
                stack.append((t, i))
                continue

            results[i] = i - stack[-1][1]
            stack.append((t, i))

        return results[::-1]
