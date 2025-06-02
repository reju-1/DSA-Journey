"""
216. Combination Sum III
link: https://leetcode.com/problems/combination-sum-iii/
"""


class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        """
        Time: O(C(9, k))  # number of combinations
        Space: O(k)       # depth of recursion stack (excluding result)
        """

        def dfs(start: int, total: int, path: list) -> list[list[int]]:
            if total == n and len(path) == k:
                return [path.copy()]

            result = []
            for i in range(start, 10):
                if total + i > n:
                    break  # or -> return result
                result += dfs(i + 1, total + i, path + [i])

            return result

        return dfs(1, 0, [])

    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        """
        Time: O(1) or O(2^9).
        Space: O(k)
        """

        def dfs(i: int, total: int, path: list) -> list[list]:
            if total == n and len(path) == k:
                return [path[:]]
            if i > 9 or len(path) > k or total > n:
                return []

            exclude = dfs(i + 1, total, path)
            include = dfs(i + 1, total + i, path + [i])

            return include + exclude

        return dfs(1, 0, [])
