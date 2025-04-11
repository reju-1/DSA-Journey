"""
78. Subsets
link: https://leetcode.com/problems/subsets/
"""


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        """
        Time: O(n * 2^n)
        Space: O(n) for recursion stack. O(2^n) for result.
        """
        result = []

        def dfs(idx: int, subset: list):
            if idx == len(nums):
                result.append(subset[:])
                return

            dfs(idx + 1, subset)  # Don't take current number
            dfs(idx + 1, subset + [nums[idx]])  # Take current number

        dfs(0, [])
        return result
