"""
169. Majority Element
link: https://leetcode.com/problems/majority-element/
"""


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        """
        Time: O(N)
        Space: O(1)
        Algorithm:
            - Boyer-Moore Majority Vote Algorithm
            - This algorithm finds the majority element, which appears more than ⌊n/2⌋ times.
        Note:
            - If the problem didn't guarantee a majority element, we would need a second pass to verify the candidate.

        Other Approaches:
            - Counting:
                - Use a hash map (or `Counter` from `collections`) to count occurrences of each element.
                - Time: O(N), Space: O(N).

            - Sorting:
                - Sort the array and return the middle element.
                - Time: O(N log N), Space: Depends on sorting algorithm.

            - Divide and Conquer:
                - Divide the array into two halves and recursively find the majority element in each half.
                - Merge the results from the two halves to determine the majority element.
                - Time: O(N log N), Space: O(log N) due to recursion.
        """

        candidate, count = None, 0

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate
