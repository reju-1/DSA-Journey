"""
Python version 3.9 or Grater
"""


class Node:
    def __init__(self, frequency: int, character: str = None):
        self.frequency = frequency
        self.character = character
        self.left = None
        self.right = None

    # Comparison based on frequency
    def __lt__(self, other):
        return self.frequency < other.frequency

    def __repr__(self):
        return f"Node({self.frequency}, {self.character})"


def _calculate_frequency(input_str: str) -> dict[str, int]:
    """Return frequency of each character"""

    result = {}
    for character in input_str:
        result[character] = result.get(character, 0) + 1

    return result


def _generate_code_word(
    root: Node, result: dict, current_code: str = ""
) -> dict[str, str]:
    """
    Traverse huffman tree and generate code word.
    Left branch  -> 0
    Right branch -> 1
    Single Node case -> 0
    """

    if root.character is not None:
        # Single-node case code is "0"
        result[root.character] = current_code if current_code else "0"
        return

    if root.left:
        _generate_code_word(root.left, result, current_code + "0")
    if root.right:
        _generate_code_word(root.right, result, current_code + "1")

    return result


def _print_result(data: list[str, (int, int)]) -> None:
    """
    Print the result into  a table
    """

    print(f"| {'Character':^10} | {'Frequency':^10} | {'Code':^10} |")
    print("-" * 38)

    for char, (freq, code) in data:
        print(f"| {char:^10} | {freq:^10} | {code:^10} |")


import heapq


def huffman_coding(message: str):
    # Finding frequencies
    frequency = _calculate_frequency(message)

    min_heap = [Node(f, c) for c, f in frequency.items()]
    heapq.heapify(min_heap)

    # Building huffman tree
    while len(min_heap) > 1:
        node1 = heapq.heappop(min_heap)
        node2 = heapq.heappop(min_heap)

        new_node = Node(node1.frequency + node2.frequency)
        new_node.left = node1
        new_node.right = node2
        heapq.heappush(min_heap, new_node)

    root = heapq.heappop(min_heap)
    code_word = _generate_code_word(root, {})

    # Result processing (combining character frequency, code-word & finally sorting )
    final_result = {}
    for k, v in code_word.items():
        final_result[k] = frequency[k], v
    final_result = sorted(final_result.items(), key=lambda x: x[0])

    # Output
    _print_result(final_result)


huffman_coding("ABRACADARBACDADRDARC")
