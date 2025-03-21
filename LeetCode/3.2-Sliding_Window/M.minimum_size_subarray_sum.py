"""
209. Minimum Size Subarray Sum
link: https://leetcode.com/problems/minimum-size-subarray-sum/
"""


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        """
        Time: O(n)
        Space: O(1)
        Note:
            Minimum window sum >= target
        """

        l, curr_sum, window = 0, 0, float("inf")

        for r, val in enumerate(nums):
            curr_sum += val

            while curr_sum >= target:
                window = min(window, r - l + 1)
                curr_sum -= nums[l]
                l += 1

        return 0 if window == float("inf") else window
