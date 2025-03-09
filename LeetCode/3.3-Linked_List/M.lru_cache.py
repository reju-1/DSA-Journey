"""
146. LRU Cache
link: https://leetcode.com/problems/lru-cache/



LRU Cache Design (HashMap + DLL):
    - `HashMap` for efficient O(1) lookups.
    - `Doubly Linked List` for maintaining the order of usage.

Structure:

null <-- head <---> [n number of nodes] <---> tail --> null

    - `head.next` Most Recently Used (MRU) node
    - `tail.prev` Least Recently Used (LRU) node
    - Nodes are stored between `head` and `tail`.

Alternative:
    - Can be implemented using `OrderedDict()` for simplicity.
"""


# Doubly linked list node
class Node:
    def __init__(self, key, value, nxt=None, prev=None):
        self.key = key
        self.value = value

        self.next = nxt
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # {key : Node Address}

        # Dummy head and tail (to simplify edge cases)
        self.head = Node(-1, -1)  # MRU
        self.tail = Node(-1, -1)  # LRU

        # Initialize an empty DLL
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add(self, node: Node):
        """
        Add a Node at most recent position in Doubly linked list
        """

        next_node: Node = self.head.next

        # connect head <--> node
        self.head.next = node
        node.prev = self.head

        # connect node <--> next_node
        node.next = next_node
        next_node.prev = node

    def _remove(self, node: Node):
        """
        Remove a node from the Doubly linked list.
        """
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        """
        Retrieves value and moves the accessed node to the MRU position.
        """

        if key not in self.cache:
            return -1

        node: Node = self.cache[key]
        self._remove(node)
        self._add(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        """
        Inserts or updates a key-value pair and moves it to MRU.
        If capacity exceeds, removes the LRU node.
        """

        if key in self.cache:
            node: Node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add(node)

        else:
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add(new_node)

            if len(self.cache) > self.capacity:
                lru: Node = self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]  # Delete from hashmap


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
