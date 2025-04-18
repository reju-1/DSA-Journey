"""
219. Contains Duplicate II
link: https://leetcode.com/problems/contains-duplicate-ii/
"""


class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        """
        Time: O(N)
        Space: O(N)
        Remarks:
            - Hashmap approach
        """
        hashMap = {}  # num : index

        for i, n in enumerate(nums):
            if n in hashMap and i - hashMap[n] <= k:
                return True
            hashMap[n] = i

        return False

    #
    def containsNearbyDuplicateV2(self, nums: list[int], k: int) -> bool:
        """
        Time: O(N)
        Space: O(K)
        Remarks:
            - Fixed size sliding window approach
        """
        window = set()
        for i, n in enumerate(nums):
            if n in window:
                return True

            window.add(n)
            if len(window) > k:
                window.remove(nums[i - k])

        return False
