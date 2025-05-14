"""
22. Generate Parentheses
link: https://leetcode.com/problems/generate-parentheses/
"""


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        """
        Complexity:
            links:
                - https://www.youtube.com/watch?v=TAuJV5eNKLM
                - https://en.wikipedia.org/wiki/Catalan_number#Applications_in_combinatorics
                - https://www.youtube.com/watch?v=FcHyVFRd2fY
                - https://www.youtube.com/watch?v=1ZAotQGnbi4

            Time: O(4^n / sqrt(n))
            Space:
                - O(n) for the recursion call stack
                - O(4^n / sqrt(n)) for storing the result list
        """
        result = []

        def dfs(s: str, open_count: int, close_count: int):
            if n == open_count == close_count:
                result.append(s)
                return

            if open_count < n:
                dfs(s + "(", open_count + 1, close_count)
            if close_count < open_count:
                dfs(s + ")", open_count, close_count + 1)

        dfs("", 0, 0)

        return result


# Todo: Learn the solution that solved with stack
