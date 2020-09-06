def bubbleSort(arr):
    for i in range(len(arr) - 2, -1, -1):
        for j in range(0, i + 1):
            if arr[j] > arr[j + 1]:
                swap(j, j + 1, arr)
    return arr


def swap(i, j, arr):
    arr[i], arr[j] = arr[j], arr[i]
