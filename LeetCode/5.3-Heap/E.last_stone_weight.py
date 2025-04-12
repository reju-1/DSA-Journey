"""
1046. Last Stone Weight
link: https://leetcode.com/problems/last-stone-weight/
"""

import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        """
        Time: O(N*logN)
        Space: O(N)
        """

        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            y = heapq.heappop(max_heap)
            x = heapq.heappop(max_heap)
            if y != x:
                heapq.heappush(max_heap, y - x)

        return -max_heap[0] if max_heap else 0
