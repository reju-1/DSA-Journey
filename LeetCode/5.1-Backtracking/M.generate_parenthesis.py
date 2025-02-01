class Solution:
    """
    Time complexity: O(4^n / sqrt(n))

    Todo: Learn the solution that solved with stack
    """

    def generateParenthesis(self, n: int) -> list[str]:
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
