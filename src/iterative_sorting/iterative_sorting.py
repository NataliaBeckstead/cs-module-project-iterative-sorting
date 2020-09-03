# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        smallest_index = i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        # Your code here
        if smallest_index != i:
            arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Loop through your array
    # Compare each element to its neighbor
    # If elements in wrong position (relative to each other, swap them)
    # If no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1.
    for i in range(0, len(arr) - 1):
        for j in range(0, len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''

'''Without using max'''
# def counting_sort(arr, maximum=None):
#     # Count appearance of each element in the array
#     counts = {}
#     for n in arr:
#         if n not in counts:
#             counts[n] = 0
#         counts[n] += 1
#     sorted_ = []
#     for n, count in sorted(counts.items()):
#         for i in range(count):
#             sorted_.append(n)
#     return sorted_

'''Using max'''
def counting_sort(arr, maximum=None):
    counts = [0] * (maximum + 1)
    for n in arr:
        counts[n] += 1
    sorted_ = []
    for i in range(0, len(counts)):
        for n in range(counts[i]):
            sorted_.append(i)
    return sorted_

print(counting_sort([1, 3, 3, 2, 5, 1, 2, 0], 5))
print(counting_sort([3, 3, 2, 3, 0], 3))