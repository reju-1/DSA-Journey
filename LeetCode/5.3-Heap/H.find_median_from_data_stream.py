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


"""
***Follow-up***
How would you optimize it:

1. If all integer numbers from the stream are between 0 and 100:
    => Use a counting array (size 101). This allows O(1) insertion
       and O(101) time to find the median by scanning through the array.

2. If 99% of the numbers are between 0 and 100:

    => Hybrid approach 1 (three arrays):
        - Use three arrays:
            - low_array: for numbers < 0
            - count_array: for 0 <= num <= 100
            - high_array: for numbers > 100
        - Since low_array and high_array are small, sorting them is cheap.
        - To find the median:
            1. Use the total count to locate the median's index.
            2. If the median is within [0, 100], you can scan the count_array directly.
               - Simply subtract the size of low_array to adjust the index.
               - No need to sort or search low/high arrays in this case.
            3. If the median lies outside the count_array range, fall back to scanning
               low_array or high_array as needed.

    => Hybrid approach 2 (array + heaps):
        - num < 0         : use a maxHeap
        - 0 <= num <= 100 : use a counting array
        - num > 100       : use a minHeap
"""


class MedianFinder:
    """
    Remarks:
        - Hybrid approach 2
    """

    def __init__(self):
        self.count = [0] * 101  # For range [0, 100]
        self.lowHeap = []  # Max heap for < 0 (store as negative)
        self.highHeap = []  # Min heap for > 100
        self.total = 0

    def addNum(self, num: int) -> None:
        if 0 <= num <= 100:
            self.count[num] += 1
        elif num < 0:
            heapq.heappush(self.lowHeap, -num)
        else:  # num > 100
            heapq.heappush(self.highHeap, num)
        self.total += 1

    def findMedian(self) -> float:
        n = self.total
        mid1 = (n + 1) // 2
        mid2 = (n + 2) // 2

        def get_kth(k):
            # Check left heap (numbers < 0)
            if k <= len(self.lowHeap):
                return -heapq.nlargest(k, self.lowHeap)[-1]
            k -= len(self.lowHeap)

            # Check count[0–100]
            count_in_range = 0
            for i in range(101):
                count_in_range += self.count[i]
                if count_in_range >= k:
                    return i

            # Remaining in highHeap
            k -= count_in_range
            return heapq.nsmallest(k, self.highHeap)[-1]

        return (get_kth(mid1) + get_kth(mid2)) / 2
