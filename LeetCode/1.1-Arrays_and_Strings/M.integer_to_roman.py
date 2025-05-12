"""
12. Integer to Roman
link: https://leetcode.com/problems/integer-to-roman/
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        """
        Time: O(N)
        Space: O(1)

        Approach:
            - Use a greedy strategy with a predefined number-symbol mapping in descending order.
            - Append symbols while reducing the number until it becomes 0.
        """
        number_map = [
            ("I", 1),
            ("IV", 4),
            ("V", 5),
            ("IX", 9),
            ("X", 10),
            ("XL", 40),
            ("L", 50),
            ("XC", 90),
            ("C", 100),
            ("CD", 400),
            ("D", 500),
            ("CM", 900),
            ("M", 1000),
        ]
        expression = ""

        for symbol, value in reversed(number_map):
            if num // value:  # Not equal zero
                times = num // value
                expression += times * symbol
                num = num % value

        return expression
