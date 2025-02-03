"""
206. Reverse Linked List
link: https://leetcode.com/problems/reverse-linked-list/
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)


def print_linked_list(head: ListNode) -> None:
    while head:
        print(head, end=" -> ")
        head = head.next
    print(head)


# --------------------------------Solution------------------------------------------------------
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Two pointer technique."""
        prev, current = None, head

        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        return prev

    def reverseListV2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """By tail recursion. with helper function"""

        def reverse(current: ListNode, prev):
            if current is None:
                return prev

            next_node = current.next
            current.next = prev
            return reverse(next_node, current)

        return reverse(current=head, prev=None)

    def reverseListV3(self, head: Optional[ListNode], prev: ListNode = None):
        """By tail recursion. with function additional parameter"""

        if head is None:
            return prev

        nxt = head.next
        head.next = prev

        return self.reverseListV3(head=nxt, prev=head)


# --------------------------------End-Solution------------------------------------------------------

h = ListNode(10)
h.next = ListNode(20)
h.next.next = ListNode(30)
h.next.next.next = ListNode(40)

print_linked_list(h)
rev = Solution().reverseListV3(h)
print_linked_list(rev)
