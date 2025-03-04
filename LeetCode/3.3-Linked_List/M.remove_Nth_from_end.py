"""
19. Remove Nth Node From End of List
link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)


class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        """
        Time: O(n)
        Space: O(1)
        Note: Similar to the sliding window approach. maintaining fixed distance
        """

        pointer, count = 0, 0
        desired, prev = head, None

        temp = head
        while temp.next:
            count += 1
            if count - pointer == n:  # maintaining fixed distance
                pointer += 1
                prev = desired
                desired = desired.next
            temp = temp.next

        if prev is None:  # first node removal or list has one element
            head = head.next
        else:
            prev.next = desired.next

        return head


head = ListNode(10, ListNode(20, ListNode(30, ListNode(40, ListNode(50)))))
new_list = Solution().removeNthFromEnd(head, 5)
