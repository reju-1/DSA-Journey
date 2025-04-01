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

    def goodNodesV2(self, root: TreeNode) -> int:
        """
        DFS with return value
        """

        def dfs(curr: TreeNode, maxSoFar: int) -> int:
            if curr is None:
                return 0

            count = 0
            if curr.val >= maxSoFar:
                count = 1

            count += dfs(curr.left, max(curr.val, maxSoFar))
            count += dfs(curr.right, max(curr.val, maxSoFar))
            return count

        return dfs(root, float("-INF"))

    def goodNodesV3(self, root: TreeNode) -> int:
        """
        DFS with global variable
        """
        self.result = 0

        def dfs(curr: TreeNode, maxSoFar):
            if curr is None:
                return
            if curr.val >= maxSoFar:
                self.result += 1

            dfs(curr.left, max(curr.val, maxSoFar))
            dfs(curr.right, max(curr.val, maxSoFar))

        dfs(root, float("-inf"))
        return self.result
