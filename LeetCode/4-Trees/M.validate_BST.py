"""
98. Validate Binary Search Tree
link: https://leetcode.com/problems/validate-binary-search-tree/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        """
        Time: O(n)
        Space: O(n)
        Approach:
            - Find the in-order sequence of the BST and check whether the sequence is sorted or not.
        """

        def dfs(curr: TreeNode | None) -> list[int]:
            if curr is None:
                return []

            left = dfs(curr.left)
            right = dfs(curr.right)

            return left + [curr.val] + right

        sequence = dfs(root)  # In-Order sequence

        return all(sequence[i] < sequence[i + 1] for i in range(len(sequence) - 1))
