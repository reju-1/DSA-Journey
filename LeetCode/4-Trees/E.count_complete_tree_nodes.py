"""
222. Count Complete Tree Nodes
link: https://leetcode.com/problems/count-complete-tree-nodes/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: TreeNode | None) -> int:
        """
        Time: O(N)
        Space: O(H)
        Remarks:
            - DFS (InOrder) approach
        """
        self.count = 0

        def dfs(curr: TreeNode | None):
            if curr is None:
                return

            dfs(curr.left)
            self.count += 1
            dfs(curr.right)

        dfs(root)
        return self.count

    #
    def countNodes(self, root: TreeNode | None) -> int:
        """
        Time: O(N)
        Space: O(H)
        Remarks:
            -Recursive solution
        """
        if root is None:
            return 0

        c1 = self.countNodes(root.left)
        c2 = self.countNodes(root.right)
        return 1 + c1 + c2

    #
    def countNodes(self, root: TreeNode | None) -> int:
        """
        Time: O(log N * log N) or O(log² N)
        Space: O(log N) or O(H)
        Remarks:
            - Uses a modified divide-and-conquer approach leveraging the properties of a Complete Binary Tree.
            - At each recursive call, computes left and right depths in O(log N) time.
            - In the worst case, recurses down log N levels, resulting in O(log N * log N) total time.
            - Recurrence relation: T(n) = T(n/2) + O(log n)
        """
        if root is None:
            return 0

        left_node = right_node = root
        left_depth = right_depth = 0

        while left_node:
            left_depth += 1
            left_node = left_node.left
        while right_node:
            right_depth += 1
            right_node = right_node.right

        if left_depth == right_depth:
            return 2**left_depth - 1  # Complete tree: 2**depth - 1 nodes
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
