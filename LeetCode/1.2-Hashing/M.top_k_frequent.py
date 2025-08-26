"""
347. Top K Frequent Elements
link: https://leetcode.com/problems/top-k-frequent-elements/description/
"""

import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """
        Time O(n)
        Space O(n)

        Related to Bucket sort or Counting Sort.

        Other possible ways:
            - Counter(nums).most_common(k)
            - by Sorting n*lgo(n)
        """
        counter = Counter(nums)

        buckets = [[] for _ in range(len(nums) + 1)]

        for number, frequency in counter.items():
            buckets[frequency].append(number)

        results = []
        for bucket in buckets[::-1]:
            for num in bucket:
                results.append(num)
                k -= 1

                if k == 0:
                    return results

    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """
        Time: O(n log k)
        Space: O(n)
        Remarks:
            - Heap solution
        """
        min_heap = []
        counter = {}

        # Calculating frequency
        for n in nums:
            counter[n] = counter.get(n, 0) + 1

        # Maintain top K frequency window via Heap
        for item, frequency in counter.items():
            heapq.heappush(min_heap, (frequency, item))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return [item for frequency, item in min_heap]
