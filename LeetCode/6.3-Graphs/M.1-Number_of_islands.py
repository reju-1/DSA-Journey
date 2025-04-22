"""
200. Number of Islands
link: https://leetcode.com/problems/number-of-islands/
"""


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        """
        Time: O(N*M) where N = rows, M = columns.
        Space: O(N*M) for the visited matrix.

        Remarks:
            - Uses DFS to explore adjacent '1's (up/down/left/right).
            - Tracks visited cells to avoid cycles/recounting.
        """

        island = 0
        n, m = len(grid), len(grid[0])
        visited = [[False] * m for _ in range(n)]  # 2D

        def dfs(i, j):
            """Performs DFS to mark all connected '1's as visited from (i, j)."""

            if not (0 <= i < n and 0 <= j < m) or grid[i][j] == "0" or visited[i][j]:
                return

            visited[i][j] = True

            # Explore all four directions
            dfs(i, j + 1)
            dfs(i, j - 1)
            dfs(i + 1, j)
            dfs(i - 1, j)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and not visited[i][j]:
                    island += 1
                    dfs(i, j)

        return island


# ==========================Todo============================
# Approach	     	Core Idea
# DFS	        ✅	Recursively/iteratively explore
# BFS	        ✅	Queue-based layer-wise explore
# Union-Find	✅	Disjoint sets of connected lands
# Flood Fill	✅	Paint-like region marking
