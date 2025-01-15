"""
198. House Robber
link: https://leetcode.com/problems/house-robber/description/
"""


class Solution:
    """
    Technique: Recursive top-down DP
    Time: O(n)
    Space: O(n)
    """

    def rob(self, nums: list[int]) -> int:
        cache = {}

        def helper(index: int):
            if index < 0:
                return 0

            if index in cache:
                return cache[index]

            # Exclude current house
            exclude = helper(index - 1)
            # Include current house
            include = nums[index] + helper(index - 2)

            cache[index] = max(include, exclude)

            return max(exclude, include)

        return helper(len(nums) - 1)


"""
There exist O(1) space complexity solution.
Bottom-Up (Optimized) DP / Sliding Window Approach which required O(1) space.
"""
