"""
230. Kth Smallest Element in a BST
link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallestV2(self, root: TreeNode, k: int) -> int:
        """
        Time: O(n)
        Space: O(h)
        Remarks:
            - Modified version of InOrder traversal
        """
        result = -1
        count = 0

        def dfs(curr: TreeNode):
            nonlocal count, k, result

            if curr is None:
                return

            dfs(curr.left)
            # Visit current node
            count += 1
            if count == k:
                result = curr.val
                return

            dfs(curr.right)

        dfs(root)
        return result
