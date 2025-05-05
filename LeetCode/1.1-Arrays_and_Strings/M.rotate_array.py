"""
189. Rotate Array
link: https://leetcode.com/problems/rotate-array/
"""


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Time: O(N)
        Space: O(1)

        Approach:
            - Reverse the entire array.
            - Reverse the first k elements.
            - Reverse the remaining n - k elements.
        Remarks:
            - https://www.youtube.com/watch?v=kE3aoZ1wsgA
        """

        n = len(nums)
        k = k % n  # case: k>=n

        def reverse(l: int, r: int):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
