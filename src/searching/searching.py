# STRETCH: implement Linear Search
def linear_search(arr, target):

    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1


import math

# STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, target):

    low = 0
    high = len(arr) - 1
    middle = high // 2

    while high - low > 1:

        if arr[middle] == target:
            return middle

        else:
            if arr[middle] > target:
                high = middle
                middle = math.ceil((high + low) / 2)
            else:
                low = middle
                middle = math.ceil((high + low) / 2)

    if arr[middle] == target:
        return middle
    elif arr[middle - 1] == target:
        return middle - 1
    else:
        return -1


# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(arr, target, low, high):

    middle = (low + high) // 2
    if len(arr) == 0:
        return -1  # array empty
    # TO-DO: add missing if/else statements, recursive calls

