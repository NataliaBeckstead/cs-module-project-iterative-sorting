def linear_search(arr, target):
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    start = 0
    stop = len(arr) - 1
    while start <= stop:
        midpoint = start + (stop - start) // 2
        if arr[midpoint] == target:
            return midpoint
        elif target < arr[midpoint]:
            stop = midpoint - 1
        else:
            start = midpoint + 1

    return -1  # not found
