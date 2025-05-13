"""
88. Merge Sorted Array
link: https://leetcode.com/problems/merge-sorted-array/
"""


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Time: O(n + m)
        Space: O(1)
        Remarks:
            - Two-pointer technique, starting from the end.
            - Don't return, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        write = n + m - 1

        while j >= 0:  # While nums2 has elements to merge
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[write] = nums1[i]
                i -= 1
            else:
                nums1[write] = nums2[j]
                j -= 1
            write -= 1
