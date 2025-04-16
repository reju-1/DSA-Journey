"""
502. IPO
link: https://leetcode.com/problems/ipo/
"""

import heapq


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list, capital: list) -> int:
        """
        Time: O(N*logN + K*logN)
        Space: O(N)
        Remarks:
            - Sorting + Heap solution
        """

        projects = [(c, p) for (c, p) in zip(capital, profits)]
        projects.sort(key=lambda x: x[0])  # sorting base on capital
        i, n = 0, len(projects)

        maxProfit = []  # max-heap

        for _ in range(k):
            while i < n and projects[i][0] <= w:
                heapq.heappush(maxProfit, -projects[i][1])  # pushing profit
                i += 1

            if not maxProfit:  # heap is empty
                break
            w += -heapq.heappop(maxProfit)

        return w

    def findMaximizedCapital(self, k: int, w: int, profits: list, capital: list) -> int:
        """
        Time: O(N*logN)
        Space: O(N)
        Remarks:
            - Two Heap Approach
        """
        max_heap = []  # profit
        min_heap = [(c, p) for (c, p) in zip(capital, profits)]  # (capital, profit)
        heapq.heapify(min_heap)

        for _ in range(k):
            while min_heap and min_heap[0][0] <= w:
                _, p = heapq.heappop(min_heap)
                heapq.heappush(max_heap, -p)

            if not max_heap:
                break
            w += -heapq.heappop(max_heap)

        return w
