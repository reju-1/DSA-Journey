"""
102. Binary Tree Level Order Traversal
link: https://leetcode.com/problems/binary-tree-level-order-traversal/
"""

from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        """
        Time: O(n)
        Space: O(n)
        """
        if root is None:
            return []

        results = []
        queue = deque([root])

        while queue:
            level_nodes = []
            level_size = len(queue)

            # start of a level
            for _ in range(level_size):
                node = queue.popleft()
                level_nodes.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # end of level
            results.append(level_nodes)

        return results
