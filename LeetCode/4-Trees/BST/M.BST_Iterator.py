"""
173. Binary Search Tree Iterator
link: https://leetcode.com/problems/binary-search-tree-iterator/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()


class BSTIterator:
    """
    Complexity:
        Time: O(1) on average
        Space: O(H)
    Remarks:
        - This solution doesn't utilize the properties of a BST, so it can be considered a general Binary tree problem.

    Alternate Approach:
        - A naive solution would be to store the inOrder traversal of the BST in an array
          and return one element at a time, requiring O(N) time and space.
    """

    def __init__(self, root: TreeNode | None):
        self.stack = []
        while root:  # Push all leftmost nodes onto the stack
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        node = self.stack.pop()

        # Push all leftmost nodes of the right subtree onto the stack
        curr = node.right
        while curr:
            self.stack.append(curr)
            curr = curr.left

        return node.val

    #
    def hasNext(self) -> bool:
        return len(self.stack) != 0
