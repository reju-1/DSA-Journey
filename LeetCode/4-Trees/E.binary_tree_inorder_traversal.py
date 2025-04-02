"""
94. Binary Tree InOrder Traversal
link: https://leetcode.com/problems/binary-tree-inorder-traversal/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversalV1(self, root: TreeNode | None) -> int:
        """
        Time: O(n)
        Space: O(h)
        Remarks:
            - Recursive DFS
        """

        if root is None:
            return []

        return (
            self.inorderTraversal(root.left)
            + [root.val]
            + self.inorderTraversal(root.right)
        )

    #
    def inorderTraversalV2(self, root: TreeNode | None) -> int:
        """
        Time: O(n)
        Space: O(h)
        Remarks:
            - Iterative DFS
        """

        answer = []
        curr = root
        stack: list[TreeNode] = []

        while stack or curr:
            while curr:  # Going to extreme left
                stack.append(curr)
                curr = curr.left

            # Process the top node on the stack
            node = stack.pop()
            answer.append(node.val)

            # Move to right subtree
            curr = node.right

        return answer

    def inorderTraversalV3(self, root: TreeNode | None) -> int:
        """
        Time: O(n)
        Space: O(1)
        Remarks:
            - **Morris Traversal**
            - https://www.youtube.com/watch?v=80Zug6D1_r4
        """
        result = []
        current = root

        while current:
            if current.left is None:
                result.append(current.val)
                current = current.right
            else:
                # Find the inOrder predecessor of current
                predecessor = current.left
                while predecessor.right and predecessor.right is not current:
                    predecessor = predecessor.right

                if predecessor.right is None:
                    # Make current the right child of its inOrder predecessor
                    predecessor.right = current
                    current = current.left
                else:
                    # Revert the changes (restore tree structure)
                    predecessor.right = None
                    result.append(current.val)
                    current = current.right

        return result
