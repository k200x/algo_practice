class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def getTreeInfo(tree):
    if tree is None:
        return TreeInfo(0, 0)

    left_tree_info = getTreeInfo(tree.left)
    right_tree_info = getTreeInfo(tree.right)

    longest_path_through_root = left_tree_info.height + right_tree_info.height
    max_diameter_so_far = max(left_tree_info.diameter, right_tree_info.diameter)
    current_diameter = max(longest_path_through_root, max_diameter_so_far)
    current_height = 1 + max(left_tree_info.height, right_tree_info.height)

    return TreeInfo(current_diameter, current_height)


def binaryTreeDiameter(tree):
    return getTreeInfo(tree).diameter


class TreeInfo:
    def __init__(self, diameter, height):
        self.diameter = diameter
        self.height = height


if __name__ == "__main__":
    root = BinaryTree(1)
    root.left = BinaryTree(3)
    root.left.left = BinaryTree(7)
    root.left.left.left = BinaryTree(8)
    root.left.left.left.left = BinaryTree(9)
    root.left.right = BinaryTree(4)
    root.left.right.right = BinaryTree(5)
    root.left.right.right.right = BinaryTree(6)
    root.right = BinaryTree(2)
    expected = 6
    actual = binaryTreeDiameter(root)
    print(6 == actual)
