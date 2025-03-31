"""
100. Same Tree
link: https://leetcode.com/problems/same-tree/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        """
        Time: O(n) or O(n+m)
        Space: O(h) or O(h_p + h_q)
        Remarks:
            - DFS approach
        """

        if p is None and q is None:
            return True
        elif p is None or q is None:  # Either one of is None
            return False

        # Same tree if the values and left and right sub-tree are equal
        return (
            p.val == q.val
            and self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
        )

    def isSameTreeV2(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        """
        Time: O(n)
        Space: O(n)
        Remarks:
            - Modified level-order traversal with `None` marker for Tracking structural integrity
        """

        queue = [p, q]

        while queue:
            node1 = queue.pop(0)
            node2 = queue.pop(0)

            if not node1 and not node2:  # Both None, meaning identical structure
                continue

            # If only one of the node is None OR values differ, trees are not the same
            if not node1 or not node2 or node1.val != node2.val:
                return False

            # left sub-tree with left sub-tree
            queue.append(node1.left)
            queue.append(node2.left)
            # right sub-tree with right sub-tree
            queue.append(node1.right)
            queue.append(node2.right)

        return True
