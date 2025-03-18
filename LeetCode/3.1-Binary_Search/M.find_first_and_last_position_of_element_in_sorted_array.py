"""
34. Find First and Last Position of Element in Sorted Array
link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
"""


class Solution:
    def helper(self, nums: list[int], key: int, l: int, r: int):
        if l > r:
            return float("inf"), -float("inf")

        mid = (l + r) // 2
        if nums[mid] == key:
            f1, l1 = self.helper(nums, key, mid + 1, r)
            f2, l2 = self.helper(nums, key, l, mid - 1)
            return min(f1, f2, mid), max(l1, l2, mid)

        if nums[mid] > key:
            return self.helper(nums, key, l, mid - 1)
        else:
            return self.helper(nums, key, mid + 1, r)

    def searchRange(self, nums: list[int], target: int) -> list[int]:
        """
        Time: O(log n)
        Space: O(lon n)
        Note:
            if all the elements are same then the time ans space will be O(n)
        """
        result = self.helper(nums, target, 0, len(nums) - 1)
        return result if result[0] != float("inf") else [-1, -1]


Solution().searchRange([0, 1, 3, 3, 3, 4], 10)
