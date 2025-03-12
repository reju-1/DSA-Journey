"""
424. Longest Repeating Character Replacement
link: https://leetcode.com/problems/longest-repeating-character-replacement/

Key Idea:
    - If the number of less frequent characters in the current window is ≤ k,
      we can replace them to make the substring uniform.

Valid Condition:
    - (window_size - most_frequent_char_count) ≤ k

Invalid Condition:
    - If the number of replacements needed exceeds k, shrink the window from the left.
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Time: O(26 * N) = O(N)
        Space: O(26) = O(1)
        """

        count = {}  # char : frequency
        left, answer = 0, 0

        for right, char in enumerate(s):
            count[char] = 1 + count.get(char, 0)

            if (right - left + 1) - max(count.values()) > k:  # Invalid window
                count[s[left]] -= 1
                left += 1

            window = right - left + 1
            answer = max(answer, window)

        return answer

    def characterReplacement(self, s: str, k: int) -> int:
        left, result = 0, 0
        counter = {}

        for right, char in enumerate(s):

            counter[char] = counter.get(char, 0) + 1
            window = right - left + 1

            if window - max(counter.values()) <= k:
                result = max(result, window)

            else:  # shrink the window from the left.
                counter[s[left]] -= 1
                left += 1

        return result
