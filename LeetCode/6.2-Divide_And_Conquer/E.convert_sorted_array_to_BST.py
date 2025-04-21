"""
108. Convert Sorted Array to Binary Search Tree
link: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        """
        Time: O(N)
        Space: O(H)
        Remarks:
            - Divide and Conquer technique
        """

        def divideAndConquer(left, right):
            if left > right:
                return None

            mid = (left + right) // 2
            node = TreeNode(nums[mid])

            node.left = divideAndConquer(left, mid - 1)
            node.right = divideAndConquer(mid + 1, right)
            return node

        return divideAndConquer(0, len(nums) - 1)

    #
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        """
        Time: O(N)
        Space: O(N), due to slicing (new sub-lists are created at each level)
            - Total copies ≈ N + N/2 + N/4 + ... + 1 = 2N = O(N)

        Remarks:
            - Concise version
        """

        if not nums:  # "not []" =/= "[] is None"
            return None

        mid = len(nums) // 2

        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1 :])

        return root
