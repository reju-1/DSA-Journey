"""
39. Combination Sum
link: https://leetcode.com/problems/combination-sum/
"""


class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        """
        Time: O(2^T/M) where T = target, M = minimal val. candidate
        Space: O(T/M)
        """
        results = []
        path = []

        def dfs(idx: int, total: int):
            if total == target:
                results.append(path[:])
                return
            if idx >= len(candidates) or total > target:
                return

            path.append(candidates[idx])
            dfs(idx, total + candidates[idx])  # Try current number
            path.pop()
            dfs(idx + 1, total)  # Skip current number

        dfs(0, 0)
        return results
