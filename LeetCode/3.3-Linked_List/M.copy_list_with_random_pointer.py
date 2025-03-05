"""
138. Copy List with Random Pointer
link: https://leetcode.com/problems/copy-list-with-random-pointer/
"""

# Definition for a Node.
# class Node:
#     def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
#         self.val = int(x)
#         self.next = next
#         self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":

        hash_map = {None: None}  # Old_node -> New_node

        # Creating new Nodes
        curr = head
        while curr:
            new_node = Node(curr.val)
            hash_map[curr] = new_node
            curr = curr.next

        # Connecting nodes: next to next & random to random
        curr = head
        while curr:
            new_node = hash_map[curr]

            new_node.next = hash_map[curr.next]
            new_node.random = hash_map[curr.random]

            curr = curr.next

        return hash_map[head]  # New list head
