"""
129. Sum Root to Leaf Numbers
link: https://leetcode.com/problems/sum-root-to-leaf-numbers/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        """
        Time & Space: Typical DFS complexity
        Remarks:
            - DFS pre-order is preferred as it avoids exploring null children after reaching leaf nodes.
            - In-order and post-order also work but may unnecessarily process null paths.
        """

        self.sum = 0

        def dfs(curr: TreeNode | None, number):
            if curr is None:
                return

            number = number * 10 + curr.val  # building the number
            if not curr.left and not curr.right:  # leaf node
                self.sum += number
                return

            dfs(curr.left, number)
            dfs(curr.right, number)

        dfs(root, 0)
        return self.sum

    #
    #
    def sumNumbersV2(self, root: TreeNode | None) -> int:
        """
        Time & Space: Typical BFS complexity
        """
        total_sum = 0
        queue = [(root, 0)]

        while queue:
            node, num = queue.pop(0)
            num = num * 10 + node.val

            if not node.left and not node.right:  # Leaf node ?
                total_sum += num
                continue  # No need to explore farther

            if node.left:
                queue.append((node.left, num))
            if node.right:
                queue.append((node.right, num))

        return total_sum
