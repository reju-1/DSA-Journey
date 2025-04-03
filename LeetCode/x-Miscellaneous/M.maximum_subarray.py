"""
53. Maximum Sub-array
link: https://leetcode.com/problems/maximum-subarray/
"""


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        """
        Time: O(n)
        Space: O(1)
        Remarks:
            - Kadane's Algorithm
        """
        max_sum = nums[0]
        curr_sum = 0

        for n in nums:
            curr_sum += n
            max_sum = max(curr_sum, max_sum)

            if curr_sum < 0:
                curr_sum = 0  # Start fresh if the group becomes toxic 😄

        return max_sum

    def maxSubArray(self, nums: list[int]) -> int:
        """
        Time: O(N)
        Space: O(log N)
        Remarks:
            - Divide and conquer approach
        """
        pass
