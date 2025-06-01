"""
136. Single Number
link: https://leetcode.com/problems/single-number/
"""


class Solution:
    def singleNumberV1(self, nums: list[int]) -> int:
        """
        Time: O(N)
        Space: O(N)
        Remarks:
            - Using set
        """
        hashSet = set()
        for n in nums:
            if n in hashSet:
                hashSet.remove(n)
            else:
                hashSet.add(n)

        return hashSet.pop()  # pop the single element

    #
    def singleNumberV2(self, nums: list[int]) -> int:
        """
        Time: O(N)
        Space: O(1)
        Remarks:
            - Bitwise XOR

        XOR Properties Used:
            1. a ^ a = 0       → a number XORed with itself cancels out.
            2. a ^ 0 = a       → a number XORed with 0 remains unchanged.
            3. Commutative     → a ^ b = b ^ a (order doesn't matter).
            4. Associative     → (a ^ b) ^ c = a ^ (b ^ c) (grouping doesn't matter).

        How It Works:
            - All duplicate numbers cancel each other due to a ^ a = 0.
            - Only the unique number remains after XORing the entire array.

        Example Simulation:
            nums = [4, 5, 7, 4, 7]  → Unique number is 5

            **Truth table**:
                +----------+
                |  4: 100  |
                |  5: 101  |
                |  7: 111  |
                |  4: 100  |
                |  7: 111  |
                +----------+
                |  5: 101  |
                +----------+
                Rules:
                    - 1^1 = 0
                    - 1^0 = 1
                    - 0^1 = 1
                    - 0^0 = 0
            *****Summary rule: Even number of 1's → 0, Odd number of 1's → 1*****

            **Code logic Step-by-step XOR**:
                result = 0        (000)
                result ^= 4       → 0 ^ 4 = 4       (000 ^ 100 = 100)
                result ^= 5       → 4 ^ 5 = 1       (100 ^ 101 = 001)
                result ^= 7       → 1 ^ 7 = 6       (001 ^ 111 = 110)
                result ^= 4       → 6 ^ 4 = 2       (110 ^ 100 = 010)
                result ^= 7       → 2 ^ 7 = 5       (010 ^ 111 = 101)

            Final result = 5 (binary: 101)
        """

        result = 0
        for n in nums:
            result = n ^ result

        return result


"""
XOR Tricks:
    1. Swap two variables without a temporary variable:
        a = a ^ b
        b = a ^ b  # (a ^ b) ^ b = a --> b ^ b = 0, a ^ 0 = a
        a = a ^ b  # (a ^ b) ^ a = b --> a ^ a = 0, b ^ 0 = b
    
    2. <Add>
"""
