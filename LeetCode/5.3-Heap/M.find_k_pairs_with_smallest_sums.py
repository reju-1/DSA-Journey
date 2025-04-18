"""
373. Find K Pairs with Smallest Sums
link: https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
"""

import heapq


class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list]:
        """
        Time: O(K log K)
        Space: O(K)
        Remarks:
            - Min-heap to efficiently find pairs with smallest sums.
            - Explore next candidates by incrementing the nums2 index (greedy/BFS-like).
        """
        result = []
        minHeap = []  # (sum, index, index)

        # Initialize the heap with the first k elements of nums1 paired with nums2[0]
        for i in range(min(k, len(nums1))):
            heapq.heappush(minHeap, (nums1[i] + nums2[0], i, 0))

        while len(result) != k:
            _, i, j = heapq.heappop(minHeap)
            result.append((nums1[i], nums2[j]))

            # For each popped pair (i, j), push potential (i, j+1) to explore next nums2 element.
            if j + 1 < len(nums2):
                heapq.heappush(minHeap, (nums1[i] + nums2[j + 1], i, j + 1))

        return result
