"""
875. Koko Eating Bananas
link: https://leetcode.com/problems/koko-eating-bananas/
"""

import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        """
        Time: O(N log N)
        Space: O(1)
        """
        answer = 0
        l, r = 1, max(piles)

        while l <= r:
            mid = (l + r) // 2
            if self.canComplete(piles, speed=mid, hours=h):
                answer = mid  # Probable min speed
                r = mid - 1
            else:
                l = mid + 1

        return answer  # or `return l`

    def canComplete(self, piles: list[int], speed: int, hours: int) -> bool:
        total_hours = 0
        for pile in piles:
            h = math.ceil(pile / speed)
            total_hours += h

        return total_hours <= hours
