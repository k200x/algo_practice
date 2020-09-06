def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array) - 1)


def binarySearchHelper(array, target, lft, rgt):
    if lft > rgt:
        return -1
    mid = (lft + rgt) // 2
    value = array[mid]
    if target == value:
        return mid
    elif target < value:
        return binarySearchHelper(array, target, lft, mid - 1)
    else:
        return binarySearchHelper(array, target, mid + 1, rgt)
