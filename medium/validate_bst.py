class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBstHelper(tree, minValue, maxValue):
    if tree is None:
        return True
    if tree.value < minValue or tree.value >= maxValue:
        return False

    left_is_valid = validateBstHelper(tree.left, minValue, tree.value)
    right_is_valid = validateBstHelper(tree.right, tree.value, maxValue)
    return left_is_valid & right_is_valid


def validateBst(tree):
    return validateBstHelper(tree, float("-inf"), float("inf"))


if __name__ == "__main__":
    root = BST(10)
    root.left = BST(5)
    root.left.left = BST(2)
    root.left.left.left = BST(1)
    root.left.right = BST(5)
    root.right = BST(15)
    root.right.left = BST(13)
    root.right.left.right = BST(14)
    root.right.right = BST(22)
    print(validateBst(root))
