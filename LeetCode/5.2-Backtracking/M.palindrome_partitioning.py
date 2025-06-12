"""
131. Palindrome Partitioning
link: https://leetcode.com/problems/palindrome-partitioning/
"""


class Solution:
    def partition(self, s: str) -> list[list[str]]:
        """
        Complexity:
            Time: O(n * 2^n)
                - There are up to 2^n possible partitions (when all characters are same).
                - Each partition takes up to O(n) time to copy into the result list.
            Space:
                - O(n) for the recursive call stack.
                - O(n * 2^n) for storing all possible partitions.

        Approach:
            - Use backtracking to explore all possible partitions.
            - For each starting index i, expand to all possible ending indices j where s[i..j] is a palindrome.
            - Recursively partition the remaining string s[j+1..n-1].
            - At i == len(s), add the current valid partition to the result.
        """
        result = []
        path = []

        def dfs(i: int):
            if i == len(s):
                result.append(path[:])
                return

            for j in range(i, len(s)):
                substring = s[i : j + 1]
                if substring == substring[::-1]:  # Check if palindrome
                    path.append(substring)
                    dfs(j + 1)
                    path.pop()

        dfs(0)
        return result
