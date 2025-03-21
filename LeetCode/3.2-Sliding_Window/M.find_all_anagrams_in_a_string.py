"""
438. Find All Anagrams in a String
link: https://leetcode.com/problems/find-all-anagrams-in-a-string/
"""


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        """
        Time: O(n)
        Space: O(n)
        Note:
            - Similar to leetCode: "567. Permutation in String"
            - Fixed size sliding window problem
        """

        n1, n2 = len(s), len(p)
        if n2 > n1:
            return []

        answer = []
        count, window = [0] * 26, [0] * 26

        for i in range(n2):
            count[ord(p[i]) - ord("a")] += 1
            window[ord(s[i]) - ord("a")] += 1

        if count == window:
            answer.append(0)

        left = 0
        for char in s[n2:]:
            window[ord(char) - ord("a")] += 1  # add new char
            window[ord(s[left]) - ord("a")] -= 1  # remove left most
            left += 1
            if window == count:  # O(26)
                answer.append(left)

        return answer
