"""
42. Trapping Rain Water
link: https://leetcode.com/problems/trapping-rain-water/
"""


class Solution:
    def trap(self, height: list[int]) -> int:
        """
        Monotonic Stack solution
        Time: O(n)
        Space: O(n)
        """

        result = 0
        n = len(height)

        leftMax = [0] * n
        rightMax = [0] * n

        leftMax[0] = height[0]
        rightMax[-1] = height[-1]

        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])
            rightMax[-i - 1] = max(rightMax[-i], height[-i - 1])

        for i in range(n):
            # Think why the volume is always positive
            volume = min(leftMax[i], rightMax[i]) - height[i]
            result += volume
            # print(f"{leftMax[i] = } { rightMax[i]= } {height[i] = } -----> {volume = }")

        return result


Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
