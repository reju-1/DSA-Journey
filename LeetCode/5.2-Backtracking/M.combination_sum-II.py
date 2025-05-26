"""
40. Combination Sum II
link: https://leetcode.com/problems/combination-sum-ii/
"""


class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        """
        Time: O(K * 2^N) — Up to 2^N subsets, each taking O(K) time to copy, where K is the average length of a combination.
        Space: O(N) call stack
        Remarks:
            - Same as Lc 39: Combination Sum
            - 2-branch recursive approach: `take` or `not take`
        Note:
            - When consider the value, take it, When it's time to not consider, skip all the duplicates.
            - Sorting makes duplicates adjacent
        """
        result = []
        path = []
        candidates.sort()

        def dfs(i: int, curr_total: int):
            if curr_total == target:
                result.append(path[:])
                return
            if i == len(candidates) or curr_total > target:
                return

            # Take the current value
            path.append(candidates[i])
            dfs(i + 1, curr_total + candidates[i])
            path.pop()

            # "not take" branch: Skip duplicates
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1  # Skipping
            dfs(i + 1, curr_total)

        dfs(0, 0)
        return result

    def combinationSum2V2(self, candidates: list[int], target: int) -> list[list[int]]:
        """
        Time & Space: Same as previous
        Remarks:
            - N-ary recursive backtracking approach.
            - Optimized compared to the previous version due to early branch pruning.
        """
        result = []
        path = []
        candidates.sort()

        def dfs(start: int, cur_sum: int):
            if cur_sum == target:
                result.append(path[:])
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue  # Skip duplicates at the same tree level

                if cur_sum + candidates[i] > target:
                    break  # Early pruning

                path.append(candidates[i])
                dfs(i + 1, cur_sum + candidates[i])
                path.pop()

        dfs(0, 0)
        return result
