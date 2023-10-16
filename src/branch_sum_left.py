"""
Sum of Left Leaves in a Binary Tree
"""
class BinaryTree:
    """
    A binary tree class.
    
    Attributes:
        value: The value of the node.
        left: The left child node.
        right: The right child node.
    """
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

def sum_of_left_leaves(root):
    """
    Returns the sum of all left leaves in a binary tree.

    Args:
        root: The root node of the binary tree.

    Returns:
        The sum of all left leaves in the binary tree.
    """
    def is_leaf(node):
        return not node.left and not node.right

    def find_left_leaves(node):
        if not node:
            return 0
        left_sum = 0
        if node.left and is_leaf(node.left):
            left_sum += node.left.value
        left_sum += find_left_leaves(node.left)
        left_sum += find_left_leaves(node.right)
        return left_sum

    if not root:
        return 0
    return find_left_leaves(root)
