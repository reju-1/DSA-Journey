"""
100. Same Tree
link: https://leetcode.com/problems/same-tree/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        """
        Time: O(n)
        Space: O(h)
        Remarks:
            - DFS approach
        """

        if p is None and q is None:
            return True
        elif p is None or q is None:  # Either one of is None
            return False

        # Same tree if the values and left and right sub-tree are equal
        return (
            p.val == q.val
            and self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
        )
