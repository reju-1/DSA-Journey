"""
78. Subsets
link: https://leetcode.com/problems/subsets/
"""


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        """
        Time: O(n * 2^n) — There are 2^n subsets, and each subset takes up to O(n) time to copy.
        Space:
            - O(n) for recursion stack.
            - O(n * 2^n) for output — 2^n subsets, each up to size n.
        Remarks:
            - 2 Branch recursion (include/exclude)
            - `Parameterized recursive` backtracking approach.
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
            - 2 Branch recursion (include/exclude)
            - Memory-friendly backtracking with a single mutable `list object`.
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

    def subsetsV3(self, nums: list[int]) -> list[list[int]]:
        """
        Time & Space: Same as previous.
        Remarks:
            - 2 Branch recursion (include/exclude)
            - purely `functional recursion` without globals. (No mutable state, No side effects)
        """

        def dfs(i: int, cur_set: list) -> list[list[int]]:
            if i == len(nums):
                return [cur_set[:]]

            # return dfs(i + 1, cur_set) + dfs(i + 1, cur_set + [nums[i]])  # CONCISE

            result = []
            result += dfs(i + 1, cur_set)  # No Take
            result += dfs(i + 1, cur_set + [nums[i]])  # Take
            return result

        return dfs(0, [])

    def subsetsV4(self, nums: list[int]) -> list[list[int]]:
        """
        Time & Space: Same as previous.
        Remarks:
            - N-branch recursive backtracking (for-loop).
            - Uses a shared (non-local) list to store result.
        """
        result = []

        def dfs(start: int, subset: list):
            result.append(subset[:])
            for i in range(start, len(nums)):
                dfs(i + 1, subset + [nums[i]])

        dfs(0, [])
        return result

    def subsetsV5(self, nums: list[int]) -> list[list[int]]:
        """
        Time & Space: Same as previous.
        Remarks:
            - N-branch recursive backtracking (for-loop).
            - Recursively constructs and aggregates subset results.
        """

        def dfs(start: int, subset: list) -> list[list]:
            result = [subset[:]]
            for i in range(start, len(nums)):  # No Out of bounds call due to range()
                result += dfs(i + 1, subset + [nums[i]])
            return result

        return dfs(0, [])
