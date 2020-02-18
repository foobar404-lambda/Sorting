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

    while low <= high:
        middle = low + (high - low) // 2

        if arr[middle] == target:
            return middle

        else:
            if arr[middle] > target:
                high = middle - 1
            elif arr[middle] < target:
                low = middle + 1
            else:
                return middle

    return -1


print(binary_search([2, 3, 52, 35, 3, 9], 9))

# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(arr, target, low, high):

    middle = (low + high) // 2
    if len(arr) == 0:
        return -1  # array empty
    # TO-DO: add missing if/else statements, recursive calls

