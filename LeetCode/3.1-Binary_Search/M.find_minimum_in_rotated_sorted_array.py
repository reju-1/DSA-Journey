"""
153. Find Minimum in Rotated Sorted Array
link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
"""


class Solution:
    def findMin(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:  # Run until left and right not become equal
            mid = (l + r) // 2

            # If mid element is greater than the rightmost element,
            # this means the smallest value is in the right half
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid  # mid could be the minimum value

        return nums[l]


Solution().findMin([10, 20, 0])
