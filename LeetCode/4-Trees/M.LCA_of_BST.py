"""
235. Lowest Common Ancestor of a Binary Search Tree
link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(slf, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Time: O(log N)
        Space: O(1)
        Remarks:
            - Iterative binary search in the BST.
            - Root is the Common ancestor of all, we are traversing top to bottom until the divergence.
            - Problem statement ensure that `p` and `q` exist on the tree
        """

        curr = root
        while curr:
            # Both p & q > current: LCA is on the right
            if curr.val < p.val and curr.val < q.val:
                curr = curr.right

            # both p & q < current:  LCA is on the left
            elif curr.val > p.val and curr.val > q.val:
                curr = curr.left
            else:  # when there is spilt means we found the LCA
                return curr

    def lowestCommonAncestor(slf, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Time: O(n)
        Space: O(h)
        Remarks:
            - Same iterative code but using recursion.
        """
        if root is None:
            return None

        if root.val < p.val and root.val < q.val:
            return slf.lowestCommonAncestor(root.right, p, q)
        elif root.val > p.val and root.val > q.val:
            return slf.lowestCommonAncestor(root.left, p, q)
        else:
            return root
