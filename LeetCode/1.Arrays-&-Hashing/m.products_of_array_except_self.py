"""
238. Product of Array Except Self
links: https://leetcode.com/problems/product-of-array-except-self/description/
"""


class Solution:
    """
    Complexity:
        - Time O(n)
        - Space O(n)
    """

    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix_arr = [1, nums[0]]
        postfix_arr = [nums[-1]]

        for prev_i, n in enumerate(nums[1:], start=1):
            prefix_arr.append(prefix_arr[prev_i] * n)

        for prev_i, n in enumerate(nums[-2::-1], start=0):
            postfix_arr.append(postfix_arr[prev_i] * n)

        postfix_arr = postfix_arr[::-1]
        postfix_arr.append(1)

        result = []
        for i in range(len(nums)):
            result.append(prefix_arr[i] * postfix_arr[i + 1])

        return result

    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """
        NeetCode solution
        Complexity:
            - Time O(n)
            - Space O(1)
        """

        result = [0] * len(nums)

        preFix = 1
        for i in range(len(nums)):
            result[i] = preFix
            preFix = preFix * nums[i]

        postFix = 1
        for i in range(len(nums) - 1, -1, -1):  # n down to 0
            result[i] *= postFix
            postFix *= nums[i]

        return result
