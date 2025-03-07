"""
287. Find the Duplicate Number

Possible Approaches:
    1. Brute Force (Nested Loops)
        - Compare every element with every other element.
        - Time Complexity: O(n^2)
        - Space Complexity: O(1)

    2. Sorting Approach
        - Sort the array and check consecutive elements for duplicates.
        - Time Complexity: O(n log n)
        - Space Complexity: O(1) (if sorting in-place)

    3. Binary Search on Range
        - Use binary search on [1, n] and count elements ≤ mid.
        - Time Complexity: O(n log n)
        - Space Complexity: O(1)

    4. Bit Manipulation
        - Time Complexity: O(32*n)
        - Space Complexity: O(1)

    5. Hashing (Set Approach)
        - Use a hash set to track seen numbers.
        - Time Complexity: O(n)
        - Space Complexity: O(n)

    6. Array Modification (Negative Marking)
        - Modify the array by negating visited indices.
        - Time Complexity: O(n)
        - Space Complexity: O(1) (but modifies input)

    7. Floyd's Tortoise and Hare (Cycle Detection)
        - Treat numbers as pointers and detect a cycle.
        - Time Complexity: O(n)
        - Space Complexity: O(1)


Links:
    - https://leetcode.com/problems/find-the-duplicate-number/

    - https://www.youtube.com/watch?v=wjYnzkAhcNk
    - https://www.youtube.com/watch?v=_n5MR8IxR6c
    - https://www.youtube.com/watch?v=49HrEGt6D2s
"""


class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        fast, slow = 0, 0

        # Finding cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break

        # Finding intersection point
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
