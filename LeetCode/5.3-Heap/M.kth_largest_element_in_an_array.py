"""
215. Kth Largest Element in an Array
link: https://leetcode.com/problems/kth-largest-element-in-an-array/
"""

import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        """
        Time: O(N*logN)
        Space: O(1) or O(N) based on sorting algo.
        Remarks:
            - Sorting
        """
        nums.sort()
        return nums[-k]

    #
    def findKthLargest(self, nums: list[int], k: int) -> int:
        """
        Time:O(N*logK)
        Space: O(K)
        Remarks:
            - Heap
        """
        min_heap = []
        for n in nums:
            heapq.heappush(min_heap, n)
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return min_heap[0]

    #
    def findKthLargest(self, nums: list[int], k: int) -> int:
        """
        Time: O(N) average case, O(N^2) worst case
        Space: O(1)
        Remarks:
            - Uses the Quick Select algorithm.
            - Quick Select is a selection algorithm to find the Kth element in an array.
              It is based on the partitioning logic of Quicksort, with an average time complexity of O(N).
              However, in the worst case — where the pivot is always the smallest or largest element —
              the partitions become highly unbalanced, resulting in O(N^2) time complexity.
              Randomized pivot selection helps avoid the worst-case scenario.

            - Best case: when the pivot splits the array evenly (partition size ≈ N/2)
                T(n) = n + n/2 + n/4 + ... + 1
                => T(n) = 2n
                => O(N)

            - Worst case: when the pivot is the smallest/largest, creating partitions of size 1 and (N-1)
                T(n) = n + (n-1) + (n-2) + ... + 1
                => T(n) = n*(n - 1)/2
                => O(N^2)

        Links:
            - https://www.youtube.com/watch?v=wiNfjkMDl3A
            - https://www.youtube.com/watch?v=XEmy13g1Qxc
        """
        kth_index = len(nums) - k

        def quick_select(start, end) -> int:
            i, pivot = start, nums[end]

            for j in range(start, end):
                if nums[j] <= pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            # swapping curr ith value with pivot
            nums[i], nums[end] = nums[end], nums[i]

            nonlocal kth_index
            if i < kth_index:
                return quick_select(i + 1, end)
            elif i > kth_index:
                return quick_select(start, i - 1)
            else:  # i == kth_index
                return nums[i]

        # calling quick-select with left and right boundary
        return quick_select(0, len(nums) - 1)
