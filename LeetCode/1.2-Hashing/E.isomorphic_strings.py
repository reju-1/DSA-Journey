"""
205. Isomorphic Strings
link: https://leetcode.com/problems/isomorphic-strings/
"""


class Solution:
    def isIsomorphicV1(self, s: str, t: str) -> bool:
        """
        Time: O(N)
        Space: O(1), because `s` and `t` consist of any valid ascii character.
        Remarks:
            - Bidirectional character mapping using two hash maps.
        """
        mapST = {}  # s -> t mapping
        mapTS = {}  # t -> s mapping

        for ch1, ch2 in zip(s, t):
            # Check for invalid existing mapping
            if ch1 in mapST and mapST[ch1] != ch2:
                return False
            if ch2 in mapTS and mapTS[ch2] != ch1:
                return False

            # Add new entry or overwrite with the same mapping
            mapST[ch1] = ch2
            mapTS[ch2] = ch1

        return True

    def isIsomorphicV2(self, s: str, t: str) -> bool:
        """
        Time: O(N)
        Space: O(N)
        Approach:
            - Use a HashMap to map each character in `s` to a character in `t`.
            - Ensure the mapping is one-to-one by checking that the number of unique values
              matches the number of keys.
        Example:
            s = "abc", t = "xyx"
            Forward mapping:
                a -> x
                b -> y
                c -> x
            len(map.keys()) != len(map.values())
        """
        hashMap = {}  # One directional mapping
        for c1, c2 in zip(s, t):
            if c1 in hashMap and hashMap[c1] != c2:
                return False
            hashMap[c1] = c2

        return len(hashMap.keys()) == len(set(hashMap.values()))

    def isIsomorphicV3(self, s: str, t: str) -> bool:
        """
        Time: O(N)
        Space: O(N)
        Remarks:
            - Uses set length comparison as a shortcut.
        Why it works:
            - If the mapping between s and t is bijective (one-to-one and onto), then:
              - Number of unique characters in s,
              - Number of unique characters in t,
              - Number of unique character pairs (s[i], t[i])
              ...must all be equal.
        """

        return len(set(s)) == len(set(t)) == len(set(zip(s, t)))
