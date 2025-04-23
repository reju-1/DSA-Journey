"""
239. Sliding Window Maximum
link: https://leetcode.com/problems/sliding-window-maximum/
"""

import heapq


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        """
        Time: O(N*logK)
        Space: O(K)
        Remarks:
            - Heap + HashMap(window)  approach
            - Heap and Hashmap store up to K elements
        """

        window = {}
        result = []

        max_heap = [-x for x in nums[:k]]
        heapq.heapify(max_heap)
        result.append(-max_heap[0])

        for n in nums[:k]:
            window[n] = 1 + window.get(n, 0)

        for i, n in enumerate(nums[k:]):
            # Remove outgoing element from window
            out = nums[i]
            window[out] -= 1
            if window[out] == 0:
                del window[out]

            # Add new element to window and heap
            window[n] = 1 + window.get(n, 0)
            heapq.heappush(max_heap, -n)

            # Clean up outdated max elements
            while -max_heap[0] not in window:
                heapq.heappop(max_heap)

            result.append(-max_heap[0])

        return result
