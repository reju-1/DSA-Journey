class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        Time: O(n*log(n) + n^2) = O(n^2)
        Space: O(1)
        """

        nums.sort()
        answer = []

        for i, current in enumerate(nums):
            if current > 0:  # Optimization
                break

            if i > 0 and current == nums[i - 1]:  # Current and previous value same ?
                continue

            low, high = i + 1, len(nums) - 1

            while low < high:
                sum3 = current + nums[low] + nums[high]

                if sum3 == 0:
                    answer.append([current, nums[low], nums[high]])
                    low += 1
                    high -= 1

                    # Escaping duplicates
                    while low < high and nums[low] == nums[low - 1]:
                        low += 1
                    while low < high and nums[high] == nums[high + 1]:
                        high -= 1

                elif sum3 < 0:
                    low += 1
                else:
                    high -= 1

        return answer
