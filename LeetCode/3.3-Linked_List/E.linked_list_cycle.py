"""
141. Linked List Cycle
link: https://leetcode.com/problems/linked-list-cycle/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode | None) -> bool:
        fast = slow = head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                return True

        return False
