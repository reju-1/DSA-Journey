"""
26. Remove Duplicates from Sorted Array
link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        """
        Time: O(N)
        Space: O(1)
        """
        i = 0
        for val in nums[1:]:
            if nums[i] != val:
                i += 1
                nums[i] = val

        return i + 1
