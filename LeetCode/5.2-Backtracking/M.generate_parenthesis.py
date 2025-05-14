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

    def generateParenthesisV2(self, n: int) -> list[str]:
        """
        Time & Space: same as previous! O(Cn), where Cn is the nth Catalan number
        Remarks:
            - DFS + Shared global object
        Approach:
            - Add an open parenthesis if open_count < n.
            - Add a close parenthesis if close_count < open_count.
            - When open_count == close_count == n, add the current path to the result.
        """
        path = []
        result = []

        def generate(open_count: int, close_count: int):
            # if n == open_count == close_count:
            if len(path) == 2 * n:
                result.append("".join(path))
                return

            if open_count < n:
                path.append("(")
                generate(open_count + 1, close_count)
                path.pop()  # clean up

            if close_count < open_count:
                path.append(")")
                generate(open_count, close_count + 1)
                path.pop()  # clean up

        generate(0, 0)
        return result
