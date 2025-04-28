"""
128. Longest Consecutive Sequence
link: https://leetcode.com/problems/longest-consecutive-sequence/description/
"""


class Solution:
    """
    Time: O(n)
    Space: O(n)

    Other ways:
        - Brute Force:
            * Create hashSet and then iterate for each element to find the next number
            * Time: O(n^2) Space: O(n)

        - Sorting:
            * Create hashSet and sort
            * Time: O(n log n) Space: O(n)
    """

    def longestConsecutive(self, nums: list[int]) -> int:
        max_sequence = 0
        hash_set = set(nums)

        for item in hash_set:
            if (item - 1) in hash_set:  # Not the beginning of a sequence
                continue

            current_max = 1
            while item + 1 in hash_set:
                current_max += 1
                item += 1

            max_sequence = max(current_max, max_sequence)

        return max_sequence
