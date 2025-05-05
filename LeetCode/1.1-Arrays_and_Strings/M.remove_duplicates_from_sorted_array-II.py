"""
80. Remove Duplicates from Sorted Array II
link: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
"""


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        """
        Time: O(N)
        Space: O(1)
        Approach:
            - Count occurrences of the current candidate.
            - Use a write pointer to overwrite duplicates.
        """
        candidate = nums[0]
        write = count = 1

        for val in nums[1:]:
            if val != candidate:
                # New value encountered, reset candidate and count
                candidate = val
                count = 1
                nums[write] = val
                write += 1

            elif count < 2:
                # Allow at most two occurrences of the same value
                count += 1
                nums[write] = val
                write += 1

        return write

    def removeDuplicates(self, nums: list[int]) -> int:
        """
        Time: O(N)
        Space: O(1)

        Approach:
            - Sorted array, duplicates are adjacent; keep first two by default.
            - For each subsequent number, if it differs from the number at index i-2,
              it means the current number hasn't appeared more than twice yet — so we keep it.
            - Place valid elements at index `i` and increment `i`.
        """
        i = 2  # Index where the next valid element should be placed
        for n in nums[2:]:
            if n != nums[i - 2]:
                nums[i] = n
                i += 1

        return i
