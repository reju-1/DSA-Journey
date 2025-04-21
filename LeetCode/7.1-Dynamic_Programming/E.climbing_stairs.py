"""
70. Climbing Stairs
link: https://leetcode.com/problems/climbing-stairs/description/
"""


class Solution:
    """
    Top dow solution
    Time: O(n)
    Space: O(n)
    """

    cache = {}

    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        if n < 0:
            return 0
        # if n <= 0:
        #     return n == 0

        if n in self.cache:
            return self.cache[n]

        one_way = self.climbStairs(n - 1)
        another_way = self.climbStairs(n - 2)

        total_ways = one_way + another_way
        self.cache[n] = total_ways

        return total_ways

    """There exist O(log n ) time and O(1) space solution solution"""
