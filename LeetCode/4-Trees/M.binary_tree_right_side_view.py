"""
199. Binary Tree Right Side View
link: https://leetcode.com/problems/binary-tree-right-side-view/
"""

from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        """
        Time: O(n)
        Space: O(n)
        Remarks:
            - Modified level order traversal(BFS)
        """
        if root is None:
            return []

        answer = []
        queue = deque([root])

        while queue:
            level_size = len(queue)

            for i in range(level_size):
                node = queue.popleft()
                if i == level_size - 1:  # if curr node is the last node of this level
                    answer.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return answer
