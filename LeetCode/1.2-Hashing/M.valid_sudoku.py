"""
36. Valid Sudoku
link: https://leetcode.com/problems/valid-sudoku/description/
"""


class Solution:
    """
    Time O(n^2)
    Space O(1)
    """

    def isValidSudoku(self, board: list[list[str]]) -> bool:

        # step1: row & column validation
        for i in range(9):
            row_frequency = [0] * 10
            col_frequency = [0] * 10

            for j in range(9):
                # Row check
                if board[i][j].isdigit():
                    num = int(board[i][j])
                    if row_frequency[num] == 1:
                        return False
                    row_frequency[num] = 1

                # Col check
                if board[j][i].isdigit():
                    num = int(board[j][i])
                    if col_frequency[num] == 1:
                        return False
                    col_frequency[num] = 1

        # Step:2 for each 3x3 Grid validation
        for row_start in range(0, 9, 3):  #  [0, 3, 6]
            for col_start in range(0, 9, 3):  # [0, 3, 6]

                # 3x3 grid
                grid_frequency = [0] * 10
                for r in range(row_start, row_start + 3):
                    for c in range(col_start, col_start + 3):

                        if board[r][c].isdigit():
                            num = int(board[r][c])
                            if grid_frequency[num] == 1:
                                return False
                            grid_frequency[num] = 1

        return True
