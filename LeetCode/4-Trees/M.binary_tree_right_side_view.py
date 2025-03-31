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

    def rightSideView(self, root: TreeNode | None) -> list[int]:
        """
        Time & Space: Typical DFS complexity.
        Remarks:
            - Related problem LeetCode 102. Binary Tree Level Order Traversal (especially **DFS approach**).
        """
        answer: list[int] = []

        def dfs(curr: TreeNode | None, depth):
            if curr is None:
                return

            # When DFS reaches a new level for the first time, this block executes.
            # It runs once per level, ensuring we capture the rightmost node first.
            # We traverse the right subtree first, which allows us to take the right-side view of the tree.
            if len(answer) == depth:
                answer.append(curr.val)

            dfs(curr.right, depth + 1)
            dfs(curr.left, depth + 1)

        dfs(root, 0)
        return answer
