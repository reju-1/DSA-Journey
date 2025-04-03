"""
112. Path Sum
link: https://leetcode.com/problems/path-sum/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        """
        Time: O(N)
        Space: O(H)
        Remarks:
            - DFS (Summing root to leaf)
        """
        target = targetSum
        status = False

        def dfs(curr: TreeNode | None, parent_sum: int):
            if curr is None:
                return

            if not curr.left and not curr.right:  # if current node is leaf node
                nonlocal target, status
                if parent_sum + curr.val == target:
                    status = True
                    return

            dfs(curr.left, parent_sum + curr.val)
            dfs(curr.right, parent_sum + curr.val)

        dfs(root, 0)
        return status
