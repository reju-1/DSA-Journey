"""
977. Squares of a Sorted Array
Link: https://leetcode.com/problems/squares-of-a-sorted-array/
"""


class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        results = []
        left, right = 0, len(nums) - 1

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                results.append(nums[left] ** 2)
                left += 1
            else:
                results.append(nums[right] ** 2)
                right -= 1

        return results[::-1]

    def sortedSquares(self, nums: list[int]) -> list[int]:

        result = [0] * len(nums)
        left, right, index = 0, len(nums) - 1, len(nums) - 1

        while left <= right:

            if abs(nums[left]) > abs(nums[right]):
                result[index] = nums[left] ** 2
                left += 1
            else:
                result[index] = nums[right] ** 2
                right -= 1
            index -= 1

        return result

    def sortedSquares(self, nums: list[int]) -> list[int]:
        return sorted([x * x for x in nums])
