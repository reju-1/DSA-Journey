"""
103. Binary Tree Zigzag Level Order Traversal
link: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        """
        Time & Space: Typical BFS complexity
        """

        if root is None:
            return []

        queue = [root]
        results = []
        flip = False

        while queue:
            level_size = len(queue)
            curr_level = []

            for _ in range(level_size):
                node = queue.pop(0)
                curr_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if flip:
                curr_level = curr_level[::-1]

            flip = not flip
            results.append(curr_level)

        return results
