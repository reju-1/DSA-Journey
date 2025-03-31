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

    def levelOrderV2(self, root: TreeNode | None) -> list[list[int]]:
        """
        Time: O(n)
        Space: O(h)
        Remarks:
            DFS Pre-order traversal (node, left, right) that uses each node's depth
            to place values in the correct level list, creating new lists as
            needed when visiting deeper levels for the first time.
        """
        answer = []  # 2D list

        def dfs(curr: TreeNode | None, depth):
            if curr is None:
                return

            # Create a new level list when reaching a new depth for the first time
            if len(answer) == depth:
                answer.append([])

            # Append the current node's value to it's level list
            answer[depth].append(curr.val)

            # Recursively traverse left and right subtrees
            dfs(curr.left, depth + 1)
            dfs(curr.right, depth + 1)

        dfs(root, 0)
        return answer
