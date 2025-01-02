"""
Bucket Sort (or Bin Sort).

Bucket Sort is a sorting algorithm that divides the input array into a number of 
buckets, sorts each bucket individually, and then merges the results. It is 
particularly effective for uniformly distributed data.

Time Complexity:
    Best Case: 
        O(n + k), where n is the number of elements and k is the number of buckets.
    Worst Case: 
        O(n^2), when all elements fall into a single bucket.

Space Complexity:
    O(n + k), where n is the input size and k is the number of buckets.

Notes:
    - The best-case complexity can be reduced to O(n + k) by using linked lists 
      for buckets and applying insertion sort within each bucket (not implemented 
      in this version).
    - This implementation uses Python's built-in `sorted()` function, which 
      employs Timsort for efficient bucket sorting.
    - Handles both integers and floating-point numbers.

Edge Cases:
    - Returns the input array as-is if it is empty or has only one element.
    - Handles uniform data gracefully (all elements are the same).

"""


def bucket_sort(arr):
    if len(arr) <= 1:
        return arr

    min_value, max_value = min(arr), max(arr)
    if min_value == max_value:
        return arr  # all are same

    # Creating buckets
    num_buckets = int(len(arr) ** 0.5)  # Optimal number of buckets
    bucket_range = (max_value - min_value) / num_buckets
    buckets = [[] for _ in range(num_buckets)]

    # Distributing elements into buckets
    for num in arr:
        bucket_index = int((num - min_value) / bucket_range)  # Tricky part

        if bucket_index == num_buckets:  # Handle edge case for max_value
            bucket_index -= 1
        buckets[bucket_index].append(num)

    # Sort individual buckets and merge results
    sorted_array = []
    for bucket in buckets:
        print(f" # {bucket =}")
        sorted_array.extend(sorted(bucket))  # Sorting of buckets by Timsort

    return sorted_array


arr = [5, 71, 10, 35, 0.9, 54, 63, 27, 49, 0.5]
print("Original Array:", arr)
print("Sorted Array:", bucket_sort(arr))
