"""
1219. Path with Maximum Gold
link: https://leetcode.com/problems/path-with-maximum-gold/
"""


class Solution:
    def getMaximumGold(self, grid: list[list[int]]) -> int:
        """
        Time: O(rows * cols * 3^(rows * cols)), as each cell can explore up to 3 directions (excluding the visited one).
        Space: O(rows * cols) due to the recursion call stack.
        Remarks:
            - Slightly modified version of "79. Word Search"
        """

        rows, cols = len(grid), len(grid[0])

        def dfs(collected: int, x: int, y: int):
            if not (0 <= x < rows) or not (0 <= y < cols):  # Out of bounds
                return collected
            if grid[x][y] == 0 or grid[x][y] == -1:  # Non-gold or Visited check
                return collected

            gold = grid[x][y]
            collected += gold
            grid[x][y] = -1  # Marking as visited
            max_collected = max(
                dfs(collected, x + 1, y),
                dfs(collected, x - 1, y),
                dfs(collected, x, y + 1),
                dfs(collected, x, y - 1),
            )
            grid[x][y] = gold  # UnMarking
            return max_collected

        maxGold = 0
        for i in range(rows):
            for j in range(cols):
                maxGold = max(maxGold, dfs(0, i, j))

        return maxGold

    #
    def getMaximumGoldV2(self, grid: list[list[int]]) -> int:
        """
        Remarks:
            - Complexity remains same
            - Non-parameterized concise version
        """
        rows, cols = len(grid), len(grid[0])

        def dfs(x: int, y: int):
            if not (0 <= x < rows) or not (0 <= y < cols) or grid[x][y] <= 0:
                return 0

            cur_gold = grid[x][y]
            grid[x][y] = -1  # Marking as visited

            max_collected = max(
                dfs(x + 1, y),
                dfs(x - 1, y),
                dfs(x, y + 1),
                dfs(x, y - 1),
            )
            grid[x][y] = cur_gold  # UnMarking
            return cur_gold + max_collected

        maxGold = 0
        for i in range(rows):
            for j in range(cols):
                maxGold = max(maxGold, dfs(i, j))

        return maxGold
