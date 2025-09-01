"""
31. Next Permutation
https://leetcode.com/problems/next-permutation/
"""


class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Time: O(N)
        Space: O(1)
        Remarks:
            - https://www.youtube.com/watch?v=zGQq3HGBTXg
        """

        N = len(nums)

        # find the pivot
        pivot = N - 2
        while pivot >= 0 and nums[pivot] >= nums[pivot + 1]:
            pivot -= 1

        if pivot < 0:  # maximum permutation
            nums.reverse()
            return

        # 2. find element just larger than nums[pivot] from the right and swap
        right = N - 1
        while nums[right] <= nums[pivot]:
            right -= 1
        nums[pivot], nums[right] = nums[right], nums[pivot]

        # reverse the rest
        nums[pivot + 1 :] = reversed(nums[pivot + 1 :])
