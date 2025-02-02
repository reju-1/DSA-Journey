"""
496. Next Greater Element I

Topic:
    - Monotonic decreasing Stack
    - Similar problem 'Daily Temperatures'

links:
    - lc: https://leetcode.com/problems/next-greater-element-i/
    - idea: https://www.youtube.com/watch?v=mJWQjJpEMa4
"""


class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack = []
        next_greater = {}

        for num in reversed(nums2):
            while stack and stack[-1] <= num:
                stack.pop()  # Remove smaller elements

            if not stack:  # Stack is empty
                next_greater[num] = -1
            else:
                next_greater[num] = stack[-1]

            stack.append(num)

        # Filtering
        return [next_greater[num] for num in nums1]
