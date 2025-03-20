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

    def findPeakElement(self, nums: list[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1

        while l <= r:
            mid = (l + r) // 2
            mid_val = nums[mid]

            # -∞ [...] -∞
            left_vel = nums[mid - 1] if mid > 0 else float("-inf")
            right_val = nums[mid + 1] if mid < n - 1 else float("-inf")

            if left_vel < mid_val > right_val:  # Mid is peak
                return mid
            elif left_vel < mid_val < right_val:  # Increase sequence
                l = mid + 1
            else:  # Decreasing sequence
                r = mid - 1
