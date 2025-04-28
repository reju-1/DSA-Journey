"""
1. Two Sum
link: https://leetcode.com/problems/two-sum/description/
"""


class Solution:
    """
    solution: time & space O(n)

    Other approaches:
        - Bruit force (2 for loop )
        - Sort and then 2 pointer

    """

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        cache = {}  # Value -> index

        for index, number in enumerate(nums):
            diff = target - number

            if diff in cache:
                return [cache[diff], index]
            else:
                cache[number] = index
