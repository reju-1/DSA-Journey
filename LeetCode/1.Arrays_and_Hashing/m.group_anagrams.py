"""
49. Group Anagrams
link: https://leetcode.com/problems/group-anagrams/description/
"""

from collections import defaultdict


class Solution:

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = defaultdict(list)

        for string in strs:
            sorted_key = "".join(sorted(string))
            anagrams[sorted_key].append(string)

        return list(anagrams.values())

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """
        Neetcode solution.
        Time complexity: O(m*n)
        Time complexity: O(m)
        """

        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)
        return list(res.values())

    def first_solution(self, strs: list[str]) -> list[list[str]]:
        """
        Time complexity O(n*m*log m)
        """
        hash_map: dict[str, list[str]] = {}

        for keyword in strs:
            sorted_key = "".join(sorted(keyword))

            if sorted_key in hash_map:
                hash_map[sorted_key].append(keyword)
            else:
                new_list: list = [keyword]
                hash_map[sorted_key] = new_list

        dict_vals = hash_map.values()

        return list(dict_vals)
