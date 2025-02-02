"""
739. Daily Temperatures
link: https://leetcode.com/problems/daily-temperatures/

Type:
    - Monotonic Stack: a Stack maintaining elements in either increasing or decreasing order.
    - similar to 'Next Greater Element I'
"""


class Solution:
    """
    Time: O(n)
    Space: O(n)
    """

    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        result = [0] * len(temperatures)
        stack = []  # (Temp, index) Note: We can solve it only storing the index

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stk_t, stk_i = stack.pop()
                result[stk_i] = i - stk_i
            stack.append((temp, i))

        return result

    """
    Iteration from reverse direction
    Time: O(n)
    Space: O(n)
    """

    def dailyTemperaturesV2(self, temperatures: list[int]) -> list[int]:
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
