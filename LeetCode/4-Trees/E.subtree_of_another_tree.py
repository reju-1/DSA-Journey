"""
572. Subtree of Another Tree
link: https://leetcode.com/problems/subtree-of-another-tree/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: TreeNode | None, sRoot: TreeNode | None) -> bool:
        """
        Time: O(n * m), where n and m are the number of nodes in root and subRoot, respectively.
        Space: O(height_root, height_subRoot)
        Remarks:
            - DFS approach
        """

        if not root:
            return False

        if self.sameTree(root, sRoot):
            return True

        else:  # Recursively check the left and right subtrees of root
            return self.isSubtree(root.left, sRoot) or self.isSubtree(root.right, sRoot)

    #
    def sameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        """This part is Lc: 100. same tree problem"""

        if not p and not q:
            return True
        if not p or not q:
            return False

        return (
            p.val == q.val
            and self.sameTree(p.left, q.left)
            and self.sameTree(p.right, q.right)
        )
