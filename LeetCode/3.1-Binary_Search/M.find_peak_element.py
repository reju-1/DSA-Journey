"""
162. Find Peak Element
link: https://leetcode.com/problems/find-peak-element/
"""


class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1
        peak = 0  # track the index of peak element

        while l != r:  # or l<r
            mid = (l + r) // 2

            if nums[mid] < nums[mid + 1]:
                if nums[mid + 1] > nums[peak]:
                    peak = mid + 1
                l = mid + 1
            else:
                if nums[mid] > nums[peak]:
                    peak = mid
                r = mid

        return peak
