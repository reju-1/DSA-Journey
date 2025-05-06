"""
151. Reverse Words in a String
link: https://leetcode.com/problems/reverse-words-in-a-string/
"""


class Solution:
    def reverseWordsV1(self, s: str) -> str:
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

    def reverseWordsV4(self, s: str) -> str:
        """
        Time: O(N)
        Space: O(1)

        Remarks:
            - Follow-up: If strings are mutable in your language, can you solve it in-place using O(1) space?
        Approach:
            1. Convert the input string into a list of characters in "reversed order" to allow in-place operations.
            2. Traverse the list, skip extra spaces, and shift valid words forward.
            3. Reverse each individual word to restore their order.
            4. Insert single spaces between words and remove any extra trailing space.
        """

        def reverse(left, right):
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        s = list(s[::-1])
        n = len(s)
        i = j = 0  # i: read pointer, j: write pointer

        while i < n:
            # Skip spaces
            while i < n and s[i] == " ":
                i += 1

            if i == n:
                break  # End of string

            # Capture the start of the new word
            start = j
            while i < n and s[i] != " ":
                # Shifting characters forward
                s[j] = s[i]
                i += 1
                j += 1

            # Reverse the copied word to fix its order
            reverse(start, j - 1)

            if j < n:  # Insert a single space if there are more words
                s[j] = " "
                j += 1

        return "".join(s[:j]).rstrip()  # Right striping probable space
