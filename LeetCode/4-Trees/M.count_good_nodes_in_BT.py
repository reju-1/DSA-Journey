"""
1448. Count Good Nodes in Binary Tree
link: https://leetcode.com/problems/count-good-nodes-in-binary-tree/
"""

from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        Time: O(n)
        Space: O(n)
        Remarks:
            - BFS approach
        """
        queue = deque([(root, root.val)])  # [(Node, parent_value), ]
        count = 0

        while queue:
            node, parent_value = queue.popleft()
            if node.val >= parent_value:
                count += 1

            new_max = max(node.val, parent_value)
            if node.left:
                queue.append((node.left, new_max))
            if node.right:
                queue.append((node.right, new_max))

        return count
