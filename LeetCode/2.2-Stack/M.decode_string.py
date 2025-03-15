"""
394. Decode String
link: https://leetcode.com/problems/decode-string/
"""


class Solution:
    def decodeString(self, s: str) -> str:
        """
        Time: O(n)
        Space: O(n)

        Algo:
            Add characters to the stack until "]" is encountered. Then, pop until "[",
            extract the multiplier, multiply the sequence, and push it back to the stack.
        """

        stack = []
        for char in s:
            if char == "]":
                seq = ""
                while stack[-1] != "[":
                    seq = stack.pop() + seq
                stack.pop()  # pop the `[`

                num_str = ""
                while stack and stack[-1].isdigit():  # extract the multiplier
                    num_str = stack.pop() + num_str

                stack.append(seq * int(num_str))
            else:
                stack.append(char)

        return "".join(stack)


Solution().decodeString("10[a]2[bc]")
