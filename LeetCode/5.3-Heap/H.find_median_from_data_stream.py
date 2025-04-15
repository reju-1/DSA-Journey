"""
295. Find Median from Data Stream
link: https://leetcode.com/problems/find-median-from-data-stream/
"""

import heapq


class MedianFinder:
    """
    The median is the middle value in a sorted dataset.
    Example:
        - [1, <2>, 3]     --> median: 2
        - [1, 2, | 3, 4]  --> median: (2 + 3) / 2 = 2.5

    Approach:
        - Two-heap solution:
            - maxHeap: stores the smaller half of the numbers
            - minHeap: stores the larger half of the numbers
        - If both heaps are equal in size (even count), the median is the average of their tops.
        - Otherwise, the median is the top of the heap with more elements.
    """

    def __init__(self):
        self.minHeap = []  # stores the larger half
        self.maxHeap = []  # stores the smaller half

    def addNum(self, num: int) -> None:
        # If minHeap is not empty and num is greater than or equal to its top, push to minHeap
        if self.minHeap and num >= self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -num)

        # Rebalance the heaps if size difference exceeds 1
        if len(self.minHeap) > len(self.maxHeap) + 1:
            n = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -n)
        if len(self.maxHeap) > len(self.minHeap) + 1:
            n = -1 * heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, n)

    #
    def findMedian(self) -> float:
        # Return the top of the larger heap if sizes are unequal
        if len(self.maxHeap) < len(self.minHeap):
            return self.minHeap[0]
        elif len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        else:
            # If sizes are equal, return average of the two tops
            return (-self.maxHeap[0] + self.minHeap[0]) / 2
