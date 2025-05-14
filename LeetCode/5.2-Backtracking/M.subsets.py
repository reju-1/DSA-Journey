"""
78. Subsets
link: https://leetcode.com/problems/subsets/
"""


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        """
        Time: O(n * 2^n)
        Space: O(n) for recursion stack. O(2^n) for result.
        Remarks:
            - Parameterized recursive backtracking approach.
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

    def subsetsV2(self, nums: list[int]) -> list[list[int]]:
        """
        Time & Space: Same as previous.
        Remarks:
            - Uses a single shared list + DFS.
        """
        result = []
        curr_subset = []

        def dfs(index: int):
            if index == len(nums):
                result.append(curr_subset[:])
                return

            curr_subset.append(nums[index])  # Include the current value
            dfs(index + 1)
            curr_subset.pop()  # Exclude the current value
            dfs(index + 1)

        dfs(0)
        return result
