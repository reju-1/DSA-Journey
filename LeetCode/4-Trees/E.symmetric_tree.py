"""
101. Symmetric Tree
link: https://leetcode.com/problems/symmetric-tree/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        """
        Time: O(n)
        Space: O(h)
        Note:
            - Similar to `lc: 100. Same Tree`
        """

        def dfs(root1: TreeNode | None, root2: TreeNode | None) -> bool:
            if not root1 and not root2:  # Both None
                return True
            if not root1 or not root2:  # One of em is None
                return False

            return (
                root1.val == root2.val
                and dfs(root1.left, root2.right)
                and dfs(root1.right, root2.left)
            )

        return dfs(root, root)
