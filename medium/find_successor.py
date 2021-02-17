class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    inOrderTraversalOrder = getInOrderTraversalOrder(tree)


    pass


def getInOrderTraversalOrder(node, order=[]):
    if node is None:
        return order
    getInOrderTraversalOrder(node.left, order)
    order.append(node)
    getInOrderTraversalOrder(node.right, order)


if __name__ == "__main__":
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.left.parent = root
    root.right = BinaryTree(3)
    root.right.parent = root
    root.left.left = BinaryTree(4)
    root.left.left.parent = root.left
    root.left.right = BinaryTree(5)
    root.left.right.parent = root.left
    root.left.left.left = BinaryTree(6)
    root.left.left.left.parent = root.left.left
    node = root.left.right
    expected = root
    actual = findSuccessor(root, node)
    print(actual, expected)
