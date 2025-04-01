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
    def kthSmallestV1(self, root: TreeNode, k: int) -> int:
        """
        Time: O(n)
        Space: O(n)
        Remarks:
            - Finds InOrder sequence of tree then returns (K-1)th element
        """

        def inOrder(curr: TreeNode | None) -> list:
            if curr is None:
                return []
            return inOrder(curr.left) + [curr.val] + inOrder(curr.right)

        sequence = inOrder(root)
        return sequence[k - 1]  # 1-indexed

    #
    #
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

    #
    #
    def kthSmallestV3(self, root: TreeNode, k: int) -> int:
        """
        Time: O(n)
        Space: O(h)
        Remarks:
            - Iterative DFS approach
        """
        stack = [root]
        curr = root

        while stack or curr:
            # Go all the way to the leftmost node
            while curr:
                stack.append(curr)
                curr = curr.left

            # Process the node
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val

            # Move to the right subtree
            curr = curr.right
