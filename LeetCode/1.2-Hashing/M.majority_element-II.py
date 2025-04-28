"""
229. Majority Element II
link: https://leetcode.com/problems/majority-element-ii/
"""


class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        """
        Time: O(N)
        Space: O(1)

        Approach:
            - Maintains at most two candidates. When a third unique element appears,
              the count of all current candidates is decreased by one. Candidates with zero count are removed.
              Finally, the remaining candidates are verified by counting their actual occurrences.

        Remarks:
            - Modified Boyer-Moore Voting Algorithm.
            - There can be at most two elements that appear more than ⌊n/3⌋ times.

        Other approaches:
            - Sorting + Counting: Time O(N log N), Space O(1) or O(N)
            - Hashmap + Counting: Time O(N), Space O(N)
        """
        answer = []
        hashMap = {}

        for n in nums:
            hashMap[n] = 1 + hashMap.get(n, 0)

            if len(hashMap) <= 2:
                continue

            # Reduce count for all elements
            toRemove = []
            for key in hashMap:
                hashMap[key] -= 1
                if hashMap[key] == 0:
                    toRemove.append(key)

            # Remove elements with 0 count
            for key in toRemove:
                hashMap.pop(key)

        # Verify candidates by actual count
        for key in hashMap:
            if nums.count(key) > len(nums) // 3:
                answer.append(key)

        return answer

    #
    def majorityElement(self, nums: list[int]) -> list[int]:
        """
        Remarks: Sorting + Counting
        """
        nums.sort()
        n = len(nums)
        threshold = n // 3
        result = []

        i = 0
        while i < n:
            count = 1
            while i + count < n and nums[i + count] == nums[i]:
                count += 1
            if count > threshold:
                result.append(nums[i])
            i += count  # Skip over this group

        return result
