"""
33. Search in Rotated Sorted Array
https://leetcode.com/problems/search-in-rotated-sorted-array/
"""


class Solution:
    def _search(self, nums: list[int], target: int, l: int, r: int) -> int:

        if l > r:
            return -1

        mid = (l + r) // 2
        if nums[mid] == target:
            return mid

        if nums[l] <= nums[mid]:  # Left half is sorted

            # target is within sorted array ?
            if nums[l] <= target <= nums[mid]:
                return self._search(nums, target, l, mid - 1)
            else:  # Otherwise target must be in right half of array
                return self._search(nums, target, mid + 1, r)

        else:
            # right is sorted and target is within this half of array?
            if nums[mid] <= target <= nums[r]:
                return self._search(nums, target, mid + 1, r)
            else:  # Otherwise target must be in left half of array
                return self._search(nums, target, l, mid - 1)

    def search(self, nums: list[int], target: int) -> int:
        """
        The key idea is that in a rotated sorted array, at least one half (left or right) is always sorted.
        We use this property to decide which half to search in, narrowing down the search space efficiently.
        Time: O(log n)
        Space: O(log n) [Recursion Stack]
        """

        return self._search(nums, target, 0, len(nums) - 1)

    def search(self, nums: list[int], target: int) -> int:
        """
        Key idea is to identify the sorted half and then perform the check
        to determine which part should be eliminated.
        """

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid

            if nums[l] <= nums[mid]:  # left half is sorted
                if nums[l] <= target <= nums[mid]:  # Target lies in left half ?
                    r = mid - 1
                else:
                    l = mid + 1

            else:  # Right half is sorted
                if nums[mid] <= target <= nums[r]:  # Target lies in right half ?
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
