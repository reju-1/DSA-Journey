"""
150. Evaluate Reverse Polish Notation
link: https://leetcode.com/problems/evaluate-reverse-polish-notation/

Types of Mathematical Notations:
    - Infix:   The operator is placed between operands. Example: (a + b)
    - Prefix:  Also known as Polish notation, where the operator precedes the operands. Example: (+ a b)
    - Postfix: Also known as Reverse Polish notation, where the operator follows the operands. Example: (a b +)
"""


class Solution:
    """
    Time: O(n)
    Space: O(n)
    """

    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for token in tokens:
            if token in "+-*/":
                a = stack.pop()
                b = stack.pop()

                result = 0
                match token:
                    case "+":
                        result = b + a
                    case "-":
                        result = b - a
                    case "*":
                        result = b * a
                    case "/":
                        result = b / a
                stack.append(int(result))

            else:
                stack.append(int(token))

        return stack[0]
