"""
27. Remove Element
link: https://leetcode.com/problems/remove-element/
"""


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        """
        Time: O(N)
        Space: O(1)
        Approach:
            - Find the last element that is not `val`.
            - Traverse backward; for each `val` found, swap it with the current end element.
            - Decrement the end pointer after each swap.
        """
        end = len(nums) - 1
        while end >= 0 and nums[end] == val:
            end -= 1

        i = end
        while i >= 0:
            if nums[i] == val:
                nums[i] = nums[end]
                end -= 1
            i -= 1

        return end + 1

    def removeElementV2(self, nums: list[int], val: int) -> int:
        """
        Remarks:
            - A leetCode user solution
            - Traverse the array and overwrite each `non-val` element to the front in-place.
        """
        i = 0
        for n in nums:
            if n != val:
                nums[i] = n
                i += 1

        return i

    def removeElementV3(self, nums: list[int], val: int) -> int:
        """
        Remarks:
            - Two pointers technique
            - Do not increment `left` until a non-`val` is confirmed.
        """

        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[left] == val:
                nums[left] = nums[right]
                right -= 1
            else:
                left += 1

        return left
