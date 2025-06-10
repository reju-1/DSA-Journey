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
    """
    Do not return anything, modify root in-place instead.
    """

    def flatten(self, root: TreeNode | None) -> None:
        """
        Time: O(N)
        Space: O(H)
        """
        if root is None:
            return None

        self.flatten(root.left)

        cur_right = root.right
        root.right = root.left
        root.left = None
        while root.right:
            root = root.right
        root.right = cur_right

        self.flatten(root.right)

    def flattenV2(self, root: TreeNode | None) -> None:
        """
        Time: O(N)
        Space: O(1)
        Remarks:
            - Modified `Morris traversal` approach
        link:
            - https://leetcode.com/problems/flatten-binary-tree-to-linked-list/solutions/1207642/js-python-java-c-simple-o-1-space-recursive-solutions-w-explanation/
        """
        curr = root

        while curr:
            if curr.left:
                # If the current node has a left subtree, find its rightmost node (predecessor)
                # Attach the current node's right subtree to the `right of that predecessor`.
                pred = curr.left
                while pred.right:
                    pred = pred.right
                pred.right = curr.right

                curr.right = curr.left
                curr.left = None

            curr = curr.right
