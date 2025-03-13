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

    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """
        Double Binary Search Technique:
            1. First, perform a binary search to find the correct row.
            2. Then, perform a binary search within that row to find the target.
        """

        rows, cols = len(matrix), len(matrix[0])
        top, bottom = 0, rows - 1

        while top <= bottom:
            mid = (top + bottom) // 2
            if matrix[mid][-1] < target:
                top = mid + 1
            elif matrix[mid][0] > target:
                bottom = mid - 1
            else:  # Found the possible row
                break

        if top > bottom:  # If top crosses bottom, the target is not in any row
            print(f"{top=} {bottom=}")
            return False

        row = (top + bottom) // 2
        l, r = 0, cols - 1

        while l <= r:
            m = (l + r) // 2
            if matrix[row][m] == target:
                return True
            elif matrix[row][m] > target:
                r = m - 1
            else:
                l = m + 1

        return False
