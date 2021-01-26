class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# O(n) time | O(n) space
def in_order_traverse(tree: BST, array):
    if tree is not None:
        in_order_traverse(tree.left, array)
        array.append(tree.value)
        in_order_traverse(tree.right, array)
    return array


# O(n) time | O(n) space
def pre_order_traverse(tree, array):
    if tree is not None:
        array.append(tree.value)
        pre_order_traverse(tree.left, array)
        pre_order_traverse(tree.right, array)
    return array


# O(n) time | O(n) space
def post_order_traverse(tree, array):
    if tree is not None:
        post_order_traverse(tree.left, array)
        post_order_traverse(tree.right, array)
        array.append(tree.value)
    return array


if __name__ == "__main__":
    root = BST(10)
    root.left = BST(5)
    root.left.left = BST(2)
    root.left.left.left = BST(1)
    root.left.right = BST(5)
    root.right = BST(15)
    root.right.right = BST(22)

    in_order = [1, 2, 5, 5, 10, 15, 22]
    pre_order = [10, 5, 2, 1, 5, 15, 22]
    post_order = [1, 2, 5, 5, 22, 15, 10]

    assert in_order == in_order_traverse(root, [])
    assert pre_order == pre_order_traverse(root, [])
    assert post_order == post_order_traverse(root, [])
