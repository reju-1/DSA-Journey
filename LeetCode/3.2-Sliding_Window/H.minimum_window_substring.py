"""
76. Minimum Window Substring
link: https://leetcode.com/problems/minimum-window-substring/
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Time: O(N)
        Space: O(M) where M is the number of unique characters in both strings
        Remarks:
            - Use sliding window: expand right to include required chars,
              then shrink left to minimize the valid window.

        Credit:
            - https://www.youtube.com/watch?v=jSto0O4AJbM
        """
        countT, window = {}, {}

        # Count frequency of characters in t
        for char in t:
            countT[char] = 1 + countT.get(char, 0)

        have, need = 0, len(countT)
        ans, ansLen = (-1, -1), float("inf")
        l = 0

        for r in range(len(s)):
            char = s[r]
            # Add current character to the window
            window[char] = 1 + window.get(char, 0)

            if char in countT and window[char] == countT[char]:
                # Only increment 'have' when the count in window matches exactly
                # (frequency in window can exceed countT, but we only care about exact matches)
                have += 1

            # Shrink the window from the left while it still contains all required characters
            while have == need:
                # Update result if this window is smaller
                if (r - l + 1) < ansLen:
                    ans = (l, r)
                    ansLen = r - l + 1

                # Remove the leftmost character from the window
                leftChar = s[l]
                window[leftChar] -= 1

                if leftChar in countT and window[leftChar] < countT[leftChar]:
                    # If the frequency in the window is now less than required, we lost a match
                    have -= 1
                l += 1

        return s[ans[0] : ans[1] + 1] if ansLen != float("inf") else ""
