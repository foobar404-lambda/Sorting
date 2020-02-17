# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    if arr == []:
        return []
    rtn_array = [arr.pop(0)]

    while len(arr) > 0:
        temp = arr.pop(0)
        rtn_array.append(None)

        for i in range(len(rtn_array) - 2, -1, -1):
            if temp >= rtn_array[i]:
                rtn_array[i + 1] = temp
                break
            else:
                rtn_array[i + 1] = rtn_array[i]

            if i == 0:
                rtn_array[0] = temp

    return rtn_array


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    swaps = 1

    while swaps > 0:
        swaps = 0

        for i in range(0, len(arr) - 1):

            if arr[i] > arr[i + 1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp

                swaps += 1

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
