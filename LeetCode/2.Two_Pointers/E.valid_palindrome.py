class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Two pointer solution.
        Time O(n)
        Space O(1)
        """

        s = "".join(s.split(" ")).lower()
        left, right = 0, len(s) - 1

        while left < right:

            if not s[left].isalnum():
                left += 1
                continue

            if not s[right].isalnum():
                right -= 1
                continue

            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True

    def other_solution(self, s: str) -> bool:

        s = list(filter(str.isalnum, s.lower()))
        # s = [c for c in s.lower() if c.isalnum()]
        return s == s[::-1]
