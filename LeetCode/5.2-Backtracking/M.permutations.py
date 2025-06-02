"""
46. Permutations
link: https://leetcode.com/problems/permutations/
"""


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        """
        Time: O(n! * n^2)
            - n! permutations (DFS leaf nodes).
            - O(n) for copying each permutation (leaf nodes).
            - O(n^2) for `n not in path` Searching from root to each leaf node O(1 + 2 + ... + n-1) ≈ O(n^2)

        Space: O(n! * n)
            - O(n) for call stack and path
            - O(n! * n) for results storing
        """

        def dfs(path: list):
            if len(path) == len(nums):
                return [path[:]]

            result = []
            for n in nums:
                if n not in path:
                    path.append(n)
                    result += dfs(path)
                    path.pop()
            return result

        return dfs([])
