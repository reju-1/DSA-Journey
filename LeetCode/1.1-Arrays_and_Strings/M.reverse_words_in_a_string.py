"""
151. Reverse Words in a String
link: https://leetcode.com/problems/reverse-words-in-a-string/
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Time: O(N)
        Space: O(N)
        Remarks:
            - Uses built-in functions
        """
        return " ".join(s.split()[::-1])

    def reverseWordsV2(self, s: str) -> str:
        """
        Time: O(N)
        Space: O(N)
        Remarks:
            - Manual parsing of words (Two pointers approach)
        """
        words = []
        length = len(s)
        index, start = 0, 0

        while index < length:
            if s[index] == " ":
                if index > start:  # Non-empty word [index - begin > 0]
                    words.append(s[start:index])
                start = index + 1  # Reset: Skip current space
            index += 1

        if index > start:  # Any last word
            words.append(s[start:index])

        return " ".join(words[::-1])

    def reverseWordsV3(self, s: str) -> str:
        """
        Time: O(N)
        Space: O(N)
        Approach:
            - Traverses the string from right to left
            - Skips multiple spaces
            - Extracts each word and appends to result list in reverse order
        """
        result = []
        i = len(s) - 1

        while i >= 0:
            if s[i] == " ":  # Escape multiple spaces
                i -= 1

            else:  # Valid character
                # Make current word
                end = i
                while i >= 0 and s[i] != " ":
                    i -= 1

                result.append(s[i + 1 : end + 1])

        return " ".join(result)
