"""
35. Search Insert Position
link: https://leetcode.com/problems/search-insert-position/
"""


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            # print(f"{l=} {r=} {mid=} {nums[mid]=}")
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        # print(f"{l=} {r=}")
        return l

    def searchInsert(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        if nums[mid] < target:
            return mid + 1
        else:
            return mid


Solution().searchInsert([2], 3)
