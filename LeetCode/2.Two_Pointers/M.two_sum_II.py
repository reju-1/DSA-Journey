"""
167. Two Sum II - Input Array Is Sorted
link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
"""


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        """
        Time: O(n)
        Space: O(1)

        Other solutions:
            - HashMap:
                * This problem is similar to Tow sum But required Extra O(N) space.
        """
        left, right = 0, len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                return [left + 1, right + 1]  # One index array
            elif current_sum > target:
                right -= 1
            else:
                left += 1
