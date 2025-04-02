"""
530. Minimum Absolute Difference in BST
link: https://leetcode.com/problems/minimum-absolute-difference-in-bst/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: TreeNode | None) -> int:
        """
        Time and space: Typical DFS complexity
        Approach:
            - In-order traversal of the BST produces a sorted sequence, and the adjacent sorted elements yield the minimum difference.
        """
        self.prev = None
        self.answer = float("INF")

        def inOrder(curr: TreeNode | None):
            if curr is None:
                return

            inOrder(curr.left)
            if self.prev is not None:
                self.answer = min(self.answer, abs(curr.val - self.prev))
            self.prev = curr.val  # Update the pervious value with current
            inOrder(curr.right)

        inOrder(root)
        return self.answer
