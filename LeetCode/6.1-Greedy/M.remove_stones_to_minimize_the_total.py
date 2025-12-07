"""
1962. Remove Stones to Minimize the Total
link: https://leetcode.com/problems/remove-stones-to-minimize-the-total/
"""

import heapq


class Solution:
    def minStoneSum(self, piles: list[int], k: int) -> int:
        """
        Time: O(K*logN)
        Space: O(N)
        Remarks:
            - Required python version 3.14>=
        TODO:
            Try to solve the  **Digital Logarithm**  problem https://codeforces.com/problemset/problem/1728/C
            the solution like is : https://www.youtube.com/watch?v=7IyMK6TXxbQ
        """

        heapq.heapify_max(piles)
        for _ in range(k):
            item = heapq.heappop_max(piles)
            heapq.heappush_max(piles, item - item // 2)

        return sum(piles)
