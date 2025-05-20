"""
39. Combination Sum
link: https://leetcode.com/problems/combination-sum/
"""


class Solution:
    def combinationSumV1(self, candidates: list[int], target: int) -> list[list[int]]:
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

    def combinationSumV2(self, candidates: list[int], target: int) -> list[list[int]]:
        """
        Time: O(N^(T/M +1))
             where N = Number of candidates T = target, M = minimal val. candidate
             At each step, try N choices, and recursion depth is up to T/M.
        Space: O(T/M) for recursion depth and current path storage.
        Remark:
            - Faster due to early pruning
        """
        results = []
        path = []
        candidates.sort()  # Sorting is O(N log N), negligible compared to O(N^(T/M + 1))

        def dfs(i: int, curr_sum: int):
            if curr_sum == target:
                results.append(path[:])
                return

            for j in range(i, len(candidates)):  # `range` safely handles i >= N case
                if curr_sum + candidates[j] > target:
                    return  # Use `continue` if not sorted
                path.append(candidates[j])
                dfs(j, curr_sum + candidates[j])
                path.pop()

        dfs(0, 0)
        return results
