"""
17. Letter Combinations of a Phone Number
link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        """
        Time:
            - O(n * 4^n), where n is the length of the input digits.
            - Each digit can map to at most 4 letters, resulting in up to 4^n combinations.
              Each combination is of length n, so appending it to the result takes O(n) time.
        Space:
            - O(n) for the recursion call stack.
            - O(4^n * n) for storing all combinations in the result list.
        """
        result = []
        if not digits:
            return result

        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(i: int, path: list):
            if len(path) == len(digits):
                result.append("".join(path))
                return

            for char in digitToChar[digits[i]]:
                path.append(char)
                dfs(i + 1, path)
                path.pop()

        dfs(0, [])
        return result

    def letterCombinationsV2(self, digits: str) -> list[str]:
        """
        Remarks: Iterative (BFS-like) approach. complex remains O(4^n * n)
        """
        if not digits:
            return []

        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        result = [""]

        for digit in digits:
            temp = []
            for cur_res in result:
                for char in digitToChar[digit]:
                    temp.append(cur_res + char)
            result = temp

        return result
