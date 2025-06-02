"""
77. Combinations
link: https://leetcode.com/problems/combinations/
"""


class Solution:
    def combineV1(self, n: int, k: int) -> list[list[int]]:
        """
        Time: O(k * C(n, k))
            - There are C(n, k) combinations each takes O(k) time to copying
        Space:
            - O(k) for recursion call stack
            - O(k * C(n, k)) for storing result
        Remarks:
            - Concise, N-branch, functional recursive backtracking.
        """

        def dfs(start: int, path: list[int]) -> list[list[int]]:
            if len(path) == k:
                return [path[:]]

            result = []
            for i in range(start, n + 1):
                result += dfs(i + 1, path + [i])

            return result

        return dfs(1, [])

    #
    def combineV2(self, n: int, k: int) -> list[list[int]]:
        """
        Time and Space: Same as previous
        Remarks:
            - Optimized, Memory-friendly
        """
        result = []
        path = []

        def dfs(start: int):
            if len(path) == k:
                result.append(path[:])
                return

            for i in range(start, n + 1):
                path.append(i)
                dfs(i + 1)
                path.pop()

        dfs(1)
        return result

    #
    def combineV3(self, n: int, k: int) -> list[list[int]]:
        """
        Time: O(k* C(n, k))
        Space: O(n) for recursion call stack
        Remarks:
            - 2-branch recursive backtracking (include/exclude).
        """
        result = []
        path = []

        def dfs(i: int):
            if len(path) == k:
                result.append(path[:])
                return
            if i > n:
                return

            path.append(i)
            dfs(i + 1)  # Include
            path.pop()
            dfs(i + 1)  # Exclude

        dfs(1)
        return result
