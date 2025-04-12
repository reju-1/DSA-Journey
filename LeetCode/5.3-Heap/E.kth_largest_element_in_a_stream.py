"""
703. Kth Largest Element in a Stream
link: https://leetcode.com/problems/kth-largest-element-in-a-stream/
"""

import heapq


class KthLargest:
    """
    Time: O(M * logK),Where M is the number of calls made to add().
    Space: O(K)
    """

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.min_heap = []

        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        return self.min_heap[0]

    def addV2(self, val: int) -> int:
        if len(self.min_heap) < self.k or self.min_heap[0] < val:
            heapq.heappush(self.min_heap, val)
            if len(self.min_heap) > self.k:
                heapq.heappop(self.min_heap)

        return self.min_heap[0]
