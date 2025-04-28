"""
224. Basic Calculator
link: https://leetcode.com/problems/basic-calculator/

Notes:
    - Direct evaluation of infix notation (e.g., `1 + 2 * 3`) is not possible due to operator precedence.
    - Typically, we convert infix expressions into postfix or prefix notation for evaluation.
    - However, in this problem, only `+`, `-`, and parentheses `()` are present.
      Since there are no precedence-based operators (`*`, `/`), we can evaluate the expression directly without conversion.
"""


class Solution:
    def calculate(self, s: str) -> int:
        """
        Time: O(N)
        Space: O(N) [worst-case, deeply nested parentheses like (1+(1+(1)+1)+1) ]
        Credit:
            - https://www.youtube.com/watch?v=3AEKyHx3tzU

        """
        result = 0
        number = 0
        sign = 1
        stack = []

        for char in s:
            if char.isdigit():
                # Build the number (multi-digit)
                number = number * 10 + int(char)

            elif char == "+" or char == "-":
                # Apply the previous number and update the sign
                result += number * sign
                number = 0
                sign = 1 if char == "+" else -1

            elif char == "(":
                # Push the current result and sign onto the stack
                stack.append(result)
                stack.append(sign)
                # Reset for the new subexpression
                number = 0
                result = 0
                sign = 1

            elif char == ")":
                # Finalize the current subexpression (<---this--->)
                result += number * sign
                number = 0

                # Pop the sign and previous result
                prev_sign = stack.pop()
                prev_result = stack.pop()

                # prev + prev_sign * (current)
                result = prev_result + prev_sign * result

        result += number * sign  # Add any remaining number
        return result
