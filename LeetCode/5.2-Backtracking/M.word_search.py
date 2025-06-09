"""
79. Word Search
link: https://leetcode.com/problems/word-search/
"""

from collections import Counter


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        """
        Complexity:
            Time: O(n * m * 3^l)
                - n = no. of rows,   m = no. of columns,   l = length of the word
                - 3^l instead of 4^l because we avoid revisiting the previous cell.
            Space: O(l)
                - due to the recursion stack, where l is the length of the word.

        Remarks:
            - We avoid using a separate visited set to save space.
              Instead, we temporarily mark visited cells in the board with a special character (e.g., '#') and revert the change after the recursive call.
              This avoids additional space usage and does not permanently modify the input board.
        """
        # -------------- Follow-up Optimization -------------
        # 1. Prune: Skip DFS if board doesn't have enough letters
        c1 = Counter(c for row in board for c in row)
        c2 = Counter(word)
        if c1 & c2 != c2:
            return False  # Insufficient letters in board

        # 2. Heuristic (optional): Start DFS from the rarest character positions
        # (Not implemented here, but can help reduce branching in large boards)
        # ---------------------------------------------------
        rows, cols = len(board), len(board[0])

        def dfs(i: int, x: int, y: int) -> bool:
            if i == len(word):
                return True

            if not (0 <= x < rows) or not (0 <= y < cols):  # Out of bound check
                return False
            if board[x][y] != word[i] or board[x][y] == "#":  # Mismatch or visited
                return False

            board[x][y] = "#"  # Marking as Visited
            # Explore all four directions
            result = (
                dfs(i + 1, x, y + 1)
                or dfs(i + 1, x, y - 1)
                or dfs(i + 1, x + 1, y)
                or dfs(i + 1, x - 1, y)
            )
            board[x][y] = word[i]  # Undo the visit marking
            return result

        # Try to start from each cell
        for i in range(rows):
            for j in range(cols):
                if dfs(0, i, j):
                    return True

        return False
