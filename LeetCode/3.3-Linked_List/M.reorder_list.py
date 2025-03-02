"""
143. Reorder List
link: https://leetcode.com/problems/reorder-list/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)

    def to_list(self):
        t = self
        l = []
        while t:
            l.append(t.val)
            t = t.next
        return l


# --------------------------Solution----------------------------------------


class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Time: O(n)
        Space: O(n)
        Note: In-place modification (Stack solution)
        """

        stack: list[ListNode] = []
        temp = head

        while temp:
            stack.append(temp)
            temp = temp.next

        last_node: ListNode | None = None

        for _ in range(len(stack) // 2):
            next_node = head.next

            head.next = stack.pop()
            head.next.next = next_node

            head = next_node
            last_node = next_node

        if last_node:  # If list have more then 1 node
            last_node.next = None


# --------------------------End-Solution-------------------------------------
h = ListNode(10, ListNode(20, ListNode(30, ListNode(40))))

print(f"Before: {h.to_list()}")
Solution().reorderList(h)
print(f"After: {h.to_list()}")
