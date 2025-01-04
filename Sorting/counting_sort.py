def print_index_map(arr: list[int], offset: int) -> None:
    """Only for visualization purpose"""

    # Print header
    print(f"+{'-'*8}+{'-'*8}+{'-'*8}+")
    print(f"|{'Index':^8}|{'Offset':^8}|{'Count':^8}|")
    print(f"+{'-'*8}+{'-'*8}+{'-'*8}+")

    # Print each row
    for i in range(len(arr)):
        index = i
        value = arr[i]
        actual_value = i - offset
        print(f"|{index:^8}|{actual_value:^8}|{value:^8}|")

    # Footer
    print(f"+{'-'*8}+{'-'*8}+{'-'*8}+")


def counting_sort(arr: list[int]) -> list[int]:
    """
    A linier time sorting algorithm.

    Complexity O(n+k) time & Space:
        - n = size of input array
        - k = range of number

    Note:
        - range k >> n counting sort is not a good idea.

    """

    min_val = min(arr)
    max_val = max(arr)

    value_range = max_val - min_val + 1
    offset = abs(min_val)

    # Counting the occurrences
    count_array = [0] * value_range
    for num in arr:
        count_array[num + offset] += 1

    # Printing counting array status
    print_index_map(count_array, offset)

    # Reconstruction
    sorted_arr = []
    for i in range(len(count_array)):
        sorted_arr.extend([i - offset] * count_array[i])

    return sorted_arr


arr = [8, 0, -5, 11, -2, 5, 0]
print("Sorted Array:", counting_sort(arr))
