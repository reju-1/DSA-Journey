"""
3211. Generate Binary Strings Without Adjacent Zeros
link: https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/

Problem Generalization:
    - Generate all possible `N`-length binary strings (consisting of `0` and `1`) that don't have adjacent zeros.
"""


class Solution:
    """
    Time: O(Fib(n+2)) ≈ O(φⁿ) where φ=1.618 (golden ratio)
        - The recurrence relation is:
            F(n) = F(n-1) + F(n-2)
            - F(n-1): Count of valid (n-1)-length strings (can append '1' to any of them).
            - F(n-2): Count of valid (n-2)-length strings (can append '10' only if the last char was '1').
        - This matches the Fibonacci sequence, but with an offset:
            - Base cases:
                F(0) = 1 (empty string)
                F(1) = 2 ("0" or "1")
            - Thus, F(n) = Fib(n+2), where Fib(0)=0, Fib(1)=1, Fib(2)=1, etc.
        - The tight bound is O(Fib(n+2)), **not O(2^n)**, because branching is restricted.

    Space:
        - Recursion depth: O(n)
        - Output size: Fib(n+2) strings of length n
    """

    def validStringsV1(self, n: int) -> list[str]:
        def dfs(i: int, soFar) -> list[str]:
            if i == n:
                return [soFar]

            result = []
            result += dfs(i + 1, soFar + "1")

            # Add Zero if string is empty or last char is not zero
            if not soFar or soFar[-1] != "0":
                result += dfs(i + 1, soFar + "0")

            return result

        return dfs(0, "")

    def validStringsV2(self, n: int) -> list[str]:
        result = []
        path = []

        def dfs(prev):
            if len(path) == n:
                result.append("".join(path))
                return

            path.append("1")
            dfs(prev="1")
            path.pop()

            if prev != "0":
                path.append("0")
                dfs(prev="0")
                path.pop()

        dfs("")
        return result
