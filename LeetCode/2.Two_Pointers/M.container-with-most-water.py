"""
11. Container With Most Water
link: https://leetcode.com/problems/container-with-most-water/description/
"""


class Solution:
    def maxArea(self, height: list[int]) -> int:
        """
        Time: O(n)
        Space: O(1)
        """

        max_area = 0
        l, r = 0, len(height) - 1
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            max_area = max(area, max_area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area

    def OthersSolutions(self, height: list[int]) -> int:
        """
        Time complexity is same for both code. but runtime is faster.
        """
        if len(height) < 2:
            return 0

        left = 0
        right = len(height) - 1
        max_area = 0

        # Precompute maximum heights for optimization
        max_height = max(height)

        while left < right:
            # Early termination check
            # If remaining width * max possible height < max_area, we can't do better
            if (right - left) * max_height <= max_area:
                break

            # Calculate width and find limiting height
            width = right - left
            current_height = min(height[left], height[right])
            current_area = width * current_height

            # Update max_area if current_area is larger
            max_area = max(max_area, current_area)

            # Move pointers and skip similar heights
            if height[left] < height[right]:
                # Skip all shorter or equal heights from left
                while left < right and height[left] <= current_height:
                    left += 1
            else:
                # Skip all shorter or equal heights from right
                while left < right and height[right] <= current_height:
                    right -= 1

        return max_area
