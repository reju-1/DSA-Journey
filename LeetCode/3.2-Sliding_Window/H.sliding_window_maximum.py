"""
239. Sliding Window Maximum
link: https://leetcode.com/problems/sliding-window-maximum/
"""

import heapq
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        """
        Time: O(N*logK)
        Space: O(K)
        Remarks:
            - Heap + HashMap(window)  approach
            - Heap and Hashmap store up to K elements

        Note:
            - A brute-force solution would slide the window and scans all K elements each time.
              This takes O(K) per window and O(N - K + 1) windows.
              Total time complexity: O(N * K).
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

    #
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        """
        Time: O(N)
        Space: O(K)
        Remarks:
            - Monotonic Decreasing Queue approach.
        """

        answer = []
        dq = deque()  # Stores the index

        # Initialize the first window
        for i in range(k):
            # Remove elements smaller than the current one
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)

        # First max
        answer.append(nums[dq[0]])

        # Slide the window
        for i in range(k, len(nums)):
            # Remove indices out of the current window
            if dq and dq[0] < i - k + 1:
                dq.popleft()

            # Remove elements smaller than the current one
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)
            answer.append(nums[dq[0]])

        return answer
