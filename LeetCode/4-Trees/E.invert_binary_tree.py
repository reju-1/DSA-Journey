"""
226. Invert Binary Tree
link: https://leetcode.com/problems/invert-binary-tree/
"""

from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Time: O(n)
    Space: O(h) # recursion stack
    Remarks:
        - DFS approach
    """

    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if root is None:
            return None

        # Swap children
        root.left, root.right = root.right, root.left

        # Recursively inverting Left and Right sub-tree
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

    def invertTreeV2(self, root: TreeNode | None) -> TreeNode | None:
        """
        Time: O(N)
        Space: O(Height)
        Remarks:
            - Iterative DFS, maintaining own stack.
        """

        if root is None:
            return None

        stack = [root]
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return root

    def invertTreeV3(self, root: TreeNode | None) -> TreeNode | None:
        """
        Time: O(n)
        Space: O(w), max width of tree
        Remark:
            - BFS approach
            - for perfect binary tree the last level contains n/2 + 1 number of nodes making O(N) space complexity
        """

        if root is None:
            return None

        queue = deque([root])

        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root
