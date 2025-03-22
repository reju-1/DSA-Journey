"""
226. Invert Binary Tree
link: https://leetcode.com/problems/invert-binary-tree/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Time: O(n)
    Space: O(n) # recursion stack
    Note:
        - DFS
    """

    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if root is None:
            return None

        # Swap children
        root.left, root.right = root.right, root.left

        # Recursively inverting Left and Right sub-tree
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
