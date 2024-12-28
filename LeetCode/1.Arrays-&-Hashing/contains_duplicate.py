"""
217. Contains Duplicate
link: https://leetcode.com/problems/contains-duplicate/description/
"""


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # Version2:
        # unique_elements =  set(nums)
        # return  len(unique_elements) != len(nums)

        uniq_elements = set()

        for n in nums:
            if n in uniq_elements:
                return True
            uniq_elements.add(n)

        return False
