"""
Test the sum_of_left_leaves function in the BinaryTree class.
"""
import sys
import unittest

from src.branch_sum_left import BinaryTree, sum_of_left_leaves

sys.path.append('/Users/ledan/projects/labs_algo/lab3') # past your path here to root of repo


class TestSumOfLeftLeaves(unittest.TestCase):
    """
    This class contains unit tests for the sum_of_left_leaves function in the BinaryTree class.
    """

    def test_single_node_tree(self):
        """
        Test the sum_of_left_leaves function on a single node tree.
        """
        root = BinaryTree(1)
        self.assertEqual(sum_of_left_leaves(root), 0)

    def test_only_left_leaves(self):
        """
        Test the sum_of_left_leaves function on a tree with only left leaves.
        """
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.left.left = BinaryTree(3)
        root.left.right = BinaryTree(4)
        self.assertEqual(sum_of_left_leaves(root), 3)

    def test_mixed_leaves(self):
        """
        Test the sum_of_left_leaves function on a tree with mixed left and right leaves.
        """
        root = BinaryTree(3)
        root.left = BinaryTree(9)
        root.right = BinaryTree(20)
        root.right.left = BinaryTree(15)
        root.right.right = BinaryTree(7)
        self.assertEqual(sum_of_left_leaves(root), 24)


if __name__ == '__main__':
    unittest.main()
