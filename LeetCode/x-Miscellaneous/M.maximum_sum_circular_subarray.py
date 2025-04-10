"""
918. Maximum Sum Circular SubArray
link: https://leetcode.com/problems/maximum-sum-circular-subarray/
"""


class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        """
        Time: O(N)
        Space: O(1)
        Remarks:
            - Modified Kadane's Algorithm
        """

        max_sum, min_sum = float("-inf"), float("inf")
        total, curr_max, curr_min = 0, 0, 0

        for num in nums:
            curr_max += num
            curr_min += num
            total += num

            max_sum = max(max_sum, curr_max)
            min_sum = min(min_sum, curr_min)

            if curr_max < 0:
                curr_max = 0
            if curr_min > 0:
                curr_min = 0

        if max_sum < 0:  #  when all elements are negative
            return max_sum

        # ======================== Circular Sum Case ========================
        # Example: [10, -5, -5, 30]
        # total = 30, min_sum = -10 (negative subarray is [-5, -5])
        # circular_sum = total - min_sum = 30 - (-10) = 40
        #
        # The negative subarray is included when we calculate the total sum.
        # When we subtract the negative part (min_sum), it effectively adds that part back,
        # so the negative subarray sum becomes zero, maximizing the circular subarray sum.

        return max(max_sum, total - min_sum)

    #
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        """Concise solution"""

        total = sum(nums)
        global_max = global_min = nums[0]
        curr_max, curr_min = 0, 0

        for n in nums:
            curr_max = max(curr_max + n, n)
            global_max = max(curr_max, global_max)

            curr_min = min(curr_min + n, n)
            global_min = min(curr_min, global_min)

        if global_max < 0:
            return global_max

        return max(global_max, total - global_min)
