"""
724. Find Pivot Index
link: https://leetcode.com/problems/find-pivot-index/
"""


class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        """
        Time: O(n)
        Space: O(1)
        """
        left_sum, right_sum = 0, sum(nums)

        for i, curr in enumerate(nums):
            right_sum -= curr

            if right_sum == left_sum:
                return i
            left_sum += curr

        return -1

    def pivotIndexV2(self, nums: list[int]) -> int:
        """
        Time: O(n)
        Space: O(1)
        """
        left_sum, total = 0, sum(nums)

        for i, curr in enumerate(nums):
            if left_sum == total - left_sum - curr:
                return i
            left_sum += curr

        return -1
