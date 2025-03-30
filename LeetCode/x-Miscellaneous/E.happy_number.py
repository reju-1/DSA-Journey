"""
202. Happy Number
link: https://leetcode.com/problems/happy-number/
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        """
        Time: O(1)
        Space: O(1)
        Note:
            Floyd's Cycle Finding Algorithm, great for cycle detection in sequences, Array (Lc: 287) linked lists, and functional graphs.
        """

        slow, fast = n, self.get_next(n)
        while slow != 1:
            if fast == slow:
                return False

            slow = self.get_next(slow)
            fast = self.get_next(self.get_next(fast))

        return True

    def isHappy(self, n: int) -> bool:
        """
        Time: O(1)
        Space: O(1)

        Explanation:
            - The sum of the squares of digits will never exceed 3 digits.
            - Since the sequence is bounded to a small set of numbers, the number of iterations is constant.
            - This makes the algorithm O(1) in both time and space.

        Constraints:
            1 <= n <= 2^31 - 1
        """
        visited = set()

        while n != 1:
            n = self.get_next(n)
            if n in visited:
                return False
            visited.add(n)

        return True

    def get_next(self, n: int) -> int:
        """Returns sum of squares"""
        answer = 0
        while n != 0:
            last = n % 10
            n = n // 10
            answer += last**2
        return answer
