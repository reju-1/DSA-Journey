"""
543. Diameter of Binary Tree
link: https://leetcode.com/problems/diameter-of-binary-tree/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode | None) -> int:
        """
        Time: O(N)
        Space: O(H), where H is height of tree
        """

        def DFS(curr: TreeNode | None) -> tuple[int, int]:
            if curr is None:
                return 0, 0  # (height, diameter)

            left, d1 = DFS(curr.left)
            right, d2 = DFS(curr.right)

            # left_height + right_height sum is the current node diameter
            curr_d = left + right

            # increasing height and taking the max diameter out of 3
            return 1 + max(left, right), max(curr_d, d1, d2)

        return DFS(root)[1]
