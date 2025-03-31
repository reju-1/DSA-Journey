"""
110. Balanced Binary Tree
link: https://leetcode.com/problems/balanced-binary-tree/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        """
        Time: O(n)
        Space: O(h)
        Remarks:
            - Related problem: LeetCode 104 (Maximum Depth of Binary Tree).
        """

        def DFS(curr: TreeNode | None) -> tuple[int, bool]:
            if curr is None:
                return 0, True  # (depth, status)

            left, stat1 = DFS(curr.left)
            right, stat2 = DFS(curr.right)
            status = stat1 and stat2 and abs(left - right) <= 1

            return 1 + max(left, right), status

        return DFS(root)[1]
