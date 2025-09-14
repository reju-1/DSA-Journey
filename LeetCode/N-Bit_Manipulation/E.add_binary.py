"""
67. Add Binary
link: https://leetcode.com/problems/add-binary/
"""


class Solution:
    def addBinaryV1(self, a: str, b: str) -> str:
        """
        Time: O(N) where N = max(len(a), len(b))
        Space: O(N)
        Approach:
            - Simulate binary addition manually.
            - Process digits from right to left.
            - Keep track of carry and append bits to result.
        """
        result = ""
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0 or carry:
            dig_a = a[i] if i >= 0 else 0
            dig_b = b[j] if j >= 0 else 0
            i -= 1
            j -= 1

            curr_sum = int(dig_a) + int(dig_b) + carry
            bit = curr_sum % 2
            carry = curr_sum // 2
            result = str(bit) + result

    def addBinaryV2(self, a: str, b: str) -> str:
        """
        Time: O(A+B)
        Space: O(1)
        Approach:
            - Convert strings to integers.
            - Use bitwise operations (XOR for sum, AND+shift for carry).
            - Repeat until no carry remains.
            - Convert result back to binary string.

        Why this works:
            - XOR computes the sum without carry.
            - AND finds positions where carry is needed, shifted left.
            - Repeating this process simulates manual binary addition.
        """
        a, b = int(a, 2), int(b, 2)

        while b:
            without_carry = a ^ b
            carry = (a & b) << 1
            a, b = without_carry, carry

        return bin(a)[2:]
