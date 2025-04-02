"""
114. Flatten Binary Tree to Linked List
link: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        Naive approach: find the PreOrder sequence and converted into linked list.
        """
        if root is None:
            return None

        def preOrder(curr: TreeNode | None):
            if curr is None:
                return []
            return [curr.val] + preOrder(curr.left) + preOrder(curr.right)

        sequence = preOrder(root)

        temp = root
        temp.left = None

        for num in sequence[1:]:
            temp.right = TreeNode(num)
            temp = temp.right
