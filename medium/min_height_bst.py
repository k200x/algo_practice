def construct_min_height_bst(array, bst, startIdx, endIdx):
    if endIdx < startIdx:
        return
    midIdx = (startIdx + endIdx) // 2
    valueToAdd = array[midIdx]
    if bst is None:
        bst = BST(valueToAdd)
    else:
        bst.insert(valueToAdd)
    construct_min_height_bst(array, bst, startIdx, midIdx - 1)
    construct_min_height_bst(array, bst, midIdx + 1, endIdx)
    return bst


def min_height_bst(array):
    return construct_min_height_bst(array, None, 0, len(array) - 1)


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)


if __name__ == "__main__":
    array = [1, 2, 5, 7, 10, 13, 14, 15, 22]
    tree = min_height_bst(array)
    print(tree)
