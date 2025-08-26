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
        Remarks:
            - Related to Bucket sort or Counting Sort.
            - Create buckets where index = frequency, value = list of numbers.
            - Iterate buckets from high frequency to low to collect top K elements.

        Other possible ways:
            - Counter(nums).most_common(k)
            - by Sorting n*lgo(n)
        """
        results = []
        counter = Counter(nums)

        max_frequency = max(counter.values())
        buckets = [[] for _ in range(max_frequency + 1)]  # Bucket needed: max_freq + 1

        for number, frequency in counter.items():
            buckets[frequency].append(number)

        for bucket in reversed(buckets):
            for num in bucket:
                results.append(num)
                if len(results) == k:
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
