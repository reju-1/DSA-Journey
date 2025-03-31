"""
104. Maximum Depth of Binary Tree
link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        """
        Time: O(n)
        Space: O(h)
        Remarks:
            - DFS approach
        """

        if root is None:
            return 0

        # Recursively find the depth of left & right subtree
        left_depth = 1 + self.maxDepth(root.left)
        right_depth = 1 + self.maxDepth(root.right)

        return max(left_depth, right_depth)

    def maxDepth(self, root: TreeNode | None) -> int:
        """
        Time: O(n)
        Space: O(w) max width of tree
        Remarks:
            - BFS approach (level order traversal)
        """

        if root is None:
            return 0

        queue = [root]
        level = 0

        while queue:
            for _ in range(len(queue)):  # for each level
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1  # increase level

        return level
