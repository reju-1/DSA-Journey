"""
74. Search a 2D Matrix
link: https://leetcode.com/problems/search-a-2d-matrix/
"""


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """
        Time: O(log(m*n))
        Space: O(1)

        Note:
            Each row contains `cols` elements, so dividing `mid` by `cols` (`mid // cols`) gives the row index.
            The remainder of `mid` divided by `cols` (`mid % cols`) gives the column index.
        """

        rows = len(matrix)
        cols = len(matrix[0])

        left, right = 0, rows * cols - 1

        while left <= right:
            mid = (left + right) // 2
            i = mid // cols  # row index
            j = mid % cols  # column index

            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
