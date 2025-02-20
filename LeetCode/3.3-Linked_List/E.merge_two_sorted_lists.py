"""
21. Merge Two Sorted Lists
link: https://leetcode.com/problems/merge-two-sorted-lists/description/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        """gives string representation from current node to end of linked list"""
        data = []
        temp = self

        while temp:
            data.append(temp.val)
            temp = temp.next

        data.append(None)
        return " -> ".join(map(str, data))


# ------------------------Solution------------------------------------------
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        """
        Time: O(n+m)
        Space: O(1)
        """

        if list1 is None:
            return list2

        if list2 is None:
            return list1

        p1 = list1
        last_ptr = list1

        p2 = list2

        while p1 and p2:
            if p1.val < p2.val:
                if p1.next is not None:
                    last_ptr = p1.next
                p1 = p1.next

            else:
                # Swap
                p1.val, p2.val = p2.val, p1.val

                temp = p1.next
                p1.next = p2
                p2 = p2.next
                p1.next.next = temp
        if p2:
            last_ptr.next = p2

        return list1

    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        """
        Time: O(n+m)
        Space: O(1)
        """

        dummy_node = current_node = ListNode()

        while list1 and list2:

            if list1.val < list2.val:
                current_node.next = list1
                list1 = list1.next

            else:
                current_node.next = list2
                list2 = list2.next

            current_node = current_node.next

        # current_node.next = list1 or list2 # concise
        if list1:
            current_node.next = list1
        if list2:
            current_node.next = list2

        return dummy_node.next


# ------------------------------End Solution-------------------------------

l1 = ListNode(10, ListNode(20, ListNode(50, ListNode(90))))
l2 = ListNode(30, ListNode(40, ListNode(60, ListNode(70, ListNode(80)))))
s = Solution().mergeTwoLists(l1, l2)
print(s)
