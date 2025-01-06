"""
704. Binary Search
link: https://leetcode.com/problems/binary-search/description/
"""


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """"""
        l, r = 0, len(nums) - 1

        while l <= r:  # Note that "<="
            mid = (l + r) // 2

            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

        return -1
