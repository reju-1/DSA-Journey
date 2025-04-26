"""
228. Summary Ranges
link: https://leetcode.com/problems/summary-ranges/
"""


class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        """
        Time: O(N)
        Space: O(N)
        Note:
            - We do include the output space in space complexity.
        """
        answer = []
        i, n = 0, len(nums)

        while i < n:
            start = nums[i]
            while i + 1 < n and nums[i] + 1 == nums[i + 1]:
                i += 1
            end = nums[i]
            i += 1

            if start == end:
                answer.append(f"{start}")
            else:
                answer.append(f"{start}->{end}")

        return answer
