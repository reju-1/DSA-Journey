"""
303. Range Sum Query - Immutable
link: https://leetcode.com/problems/range-sum-query-immutable/
"""


class NumArray:
    def __init__(self, nums: list[int]):
        self._prefix_sum = []
        s = 0
        for n in nums:
            s += n
            self._prefix_sum.append(s)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self._prefix_sum[right]

        return self._prefix_sum[right] - self._prefix_sum[left - 1]


"""
class NumArray:
    def __init__(self, nums: list[int]):
        self._prefix_sum = [0]

        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i - 1]

        self._prefix_sum.extend(nums)

    def sumRange(self, left: int, right: int) -> int:
        return self._prefix_sum[right + 1] - self._prefix_sum[left]
"""
