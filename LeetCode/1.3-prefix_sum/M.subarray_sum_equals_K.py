"""
560. Sub-array Sum Equals K
link: https://leetcode.com/problems/subarray-sum-equals-k/

+---------------------------------------------------------------------------------------------------------------+
Sub-array:
    - A contiguous part of an array.
    - Properties:
        - Must be contiguous (continuous block of elements).
        - Order is preserved.
        - Length range: 1 to n.
        - Total possibilities: O(n^2).

Sub-String:
    - A contiguous part of a string.
    - Properties:
        - Similar to Sub-array

Sub-sequence:
    - A sequence derived by deleting some or no elements without changing the order.
    - Properties:
        - Can be contiguous or non-contiguous.
        - Order is preserved.
        - Length range: 0 to n.
        - Total possibilities: 2^n.

Sub-set:
    - A selection of elements from a set where order is irrelevant, and duplicates are not allowed.
    - Properties:
        - Can be seen as a combination.
        - Order does not matter.
        - Length range: 0 to n.
        - Total possibilities: 2^n.

Note: The key difference between `Subset` and `Subsequence` is `Order`.  
      - In a subsequence, order matters.  
      - In a subset, order does not matter.

+--------------------------------------------------------------------------------------------------------------+
"""


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        """
        Brute Force
        Time: O(n^2)
        Space: O(1)
        """

        count = 0
        for i in range(len(nums)):
            sum = 0

            for val in nums[i:]:
                sum += val
                if sum == k:
                    count += 1

        return count

    def subarraySum(self, nums: list[int], k: int) -> int:
        """
        Time: O(n)
        Space: O(n)

        Solution: https://www.youtube.com/watch?v=bqN9yB0vF08
        """

        prefix_sum = {0: 1}
        curr_sum, count = 0, 0

        for n in nums:
            curr_sum += n

            if curr_sum - k in prefix_sum:
                count += prefix_sum[curr_sum - k]

            # prefix_sum[curr_sum] = prefix_sum.get(curr_sum, 0) + 1 # concise
            if curr_sum in prefix_sum:
                prefix_sum[curr_sum] += 1
            else:
                prefix_sum[curr_sum] = 1

        return count
