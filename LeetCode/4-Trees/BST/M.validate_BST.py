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

    #
    #
    def isValidBST(self, root: TreeNode | None) -> bool:
        """
        Time: O(n)
        Space: O(h)
        Approach:
            - similar to lc: 530 approach
            - Traverse InOrder fashion. By comparing the previous and current value we validate the BST
        """
        status = True
        previous = None

        def inOrder(curr: TreeNode | None):
            if curr is None:
                return

            inOrder(curr.left)
            # Processing the node
            nonlocal status, previous
            if previous is not None:
                if curr.val <= previous:
                    status = False
                    return
            previous = curr.val

            inOrder(curr.right)

        inOrder(root)
        return status

    #
    #
    def isValidBST(self, root: TreeNode | None) -> bool:
        """
        Time and Space: Typical DFS complexity
        """

        def valid(curr: TreeNode | None, left_border: int, right_border: int) -> bool:
            if curr is None:
                return True

            if not (left_border < curr.val < right_border):
                return False

            s1 = valid(curr.left, left_border=left_border, right_border=curr.val)
            s2 = valid(curr.right, left_border=curr.val, right_border=right_border)

            return s1 and s2

        return valid(root, -float("inf"), float("inf"))

    #
    #
    def isValidBST(self, root: TreeNode | None) -> bool:
        """
        Time & Space: Typical BFS complexity
        """

        INF = float("inf")
        queue = [(-INF, root, INF)]  # (left, node, right)

        while queue:
            left, node, right = queue.pop(0)

            if not (left < node.val < right):
                return False

            if node.left:
                queue.append((left, node.left, node.val))
            if node.right:
                queue.append((node.val, node.right, right))

        return True
