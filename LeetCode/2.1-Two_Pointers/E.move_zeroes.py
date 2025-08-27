"""
283. Move Zeroes
link: https://leetcode.com/problems/move-zeroes/
"""


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Time: O(n)
        Space: O(1)
        """
        left = 0  # index where the next non-zero element should go

        for right in range(len(nums)):
            if nums[right] != 0:  # if non-zero, swap it into the left position
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
