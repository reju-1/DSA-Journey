"""
236. Lowest Common Ancestor of a Binary Tree
link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
"""

from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


Node = Optional[TreeNode]  # For concise annotations


class Solution:
    def lowestCommonAncestor(self, root: Node, p: Node, q: Node) -> Node:
        """
        Time: O(N)
        Space: O(H)
        Remarks:
            - DFS (post-order) traversal.
            - https://www.youtube.com/watch?v=Oi3_06ultic

        Alternative Approaches:
            - A brute force solution would require two searches from the root to p and q, each O(N) time,
              and O(N) space for storing the paths. The LCA is determined by comparing both paths.
            - Binary lifting.
            - Tarjan's Offline LCA algorithm.
        """

        if root == None or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If both left and right are non-null, root is the LCA
        if left and right:
            return root

        # Otherwise, return the non-null result
        # If one of the nodes is a descendant of the other, (that node) the ancestor node will be returned.
        # since the other side will be null, indicating that the LCA is already found.
        return left if left else right
