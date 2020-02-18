# TO-DO: complete the help function below to merge 2 sorted arrays
def merge(arrA, arrB):
    merged_arr = []
    # TO-DO

    while True:
        if len(arrA) == 0:
            merged_arr += arrB
            break
        elif len(arrB) == 0:
            merged_arr += arrA
            break

        if arrA[0] < arrB[0]:
            merged_arr.append(arrA.pop(0))
        else:
            merged_arr.append(arrB.pop(0))

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO

    if len(arr) <= 1:
        return arr

    arr1 = arr[: len(arr) // 2]
    arr2 = arr[len(arr) // 2 :]

    arr1 = merge_sort(arr1)
    arr2 = merge_sort(arr2)

    return merge(arr1, arr2)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr


def binary_insertion_sort(arr):
    new_arr = [arr.pop(0)]

