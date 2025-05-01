"""
14. Longest Common Prefix
link: https://leetcode.com/problems/longest-common-prefix/
"""


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        """
        Time: O(N*M), where N is the number of strings and M is the length of the shortest string
        Space: O(1)
        Approach:
            - Use the first word as a reference for comparison.
            - For each character index in the base, compare it with the same index in all other words.
        """
        base = strs[0]

        for i in range(len(base)):
            # Compare base[i] with each word's i-th character
            for word in strs:
                # Return prefix if index out of bounds or mismatch
                if i >= len(word) or word[i] != base[i]:
                    return base[:i]  # Return [0 to i) string

        return base  # All chars matched

    def longestCommonPrefixV2(self, strs: list[str]) -> str:
        """
        Time: O(N*log N), due to sorting
        Space: O(N), TimSort
        Approach:
            - Sort the list lexicographically.
            - The Longest common prefix must be between the first and last word after sorting.
        """
        strs.sort()
        first = strs[0]
        last = strs[-1]
        count = 0
        for c1, c2 in zip(first, last):
            if c1 != c2:
                return first[:count]
            count += 1

        return first[:count]


## TODO: Solve via Trie
