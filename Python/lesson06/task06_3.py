from unittest import TestCase
from ASD2.lesson06.task06 import BSTNode, BalancedBST
from ASD2.lesson06.task06_2 import BSTNode as BSTNode2, BalancedBST as BalancedBST2

class Test(TestCase):

    def test_only_root(self):
        arr: list = [8]
        tree: BalancedBST = BalancedBST()
        tree.GenerateTree(arr)
        self.assertEqual(8, tree.Root.NodeKey)
        self.assertIsNone(tree.Root.Parent)
        self.assertIsNone(tree.Root.LeftChild)
        self.assertIsNone(tree.Root.RightChild)
        self.assertEqual(0, tree.Root.Level)

    def test_two_children_tree(self):
        arr: list = [8, 4, 10]
        tree: BalancedBST = BalancedBST()
        tree.GenerateTree(arr)
        self.assertEqual(8, tree.Root.NodeKey)
        self.assertIsNone(tree.Root.Parent)
        self.assertEqual(0, tree.Root.Level)

        self.assertEqual(4, tree.Root.LeftChild.NodeKey)
        self.assertEqual(1, tree.Root.LeftChild.Level)
        self.assertEqual(8, tree.Root.LeftChild.Parent.NodeKey)

        self.assertEqual(10, tree.Root.RightChild.NodeKey)
        self.assertEqual(1, tree.Root.LeftChild.Level)
        self.assertEqual(8, tree.Root.LeftChild.Parent.NodeKey)

    def test_big_tree(self):
        arr: list = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 11, 15, 13]
        # [1, 2, 3, 4, 5, 6, 8, 10, 11, 12, 13, 14, 15] 8
        # [1, 2, 3, 4, 5, 6] [10, 11, 12, 13, 14, 15] 4,      13
        # [1, 2, 3] [5, 6] [10, 11, 12] [14, 15]    2, 6,   11, 15
        # [1] [3] [5] [10] [12] [14]
        tree: BalancedBST = BalancedBST()
        tree.GenerateTree(arr)
        self.assertEqual(8, tree.Root.NodeKey)
        self.assertIsNone(tree.Root.Parent)
        self.assertEqual(0, tree.Root.Level)

        self.assertEqual(4, tree.Root.LeftChild.NodeKey)
        self.assertEqual(1, tree.Root.LeftChild.Level)
        self.assertEqual(8, tree.Root.LeftChild.Parent.NodeKey)
        self.assertEqual(2, tree.Root.LeftChild.LeftChild.NodeKey)
        self.assertEqual(2, tree.Root.LeftChild.LeftChild.Level)
        self.assertEqual(4, tree.Root.LeftChild.LeftChild.Parent.NodeKey)
        self.assertEqual(6, tree.Root.LeftChild.RightChild.NodeKey)
        self.assertEqual(2, tree.Root.LeftChild.RightChild.Level)
        self.assertEqual(4, tree.Root.LeftChild.RightChild.Parent.NodeKey)

        self.assertEqual(1, tree.Root.LeftChild.LeftChild.LeftChild.NodeKey)
        self.assertEqual(3, tree.Root.LeftChild.LeftChild.LeftChild.Level)
        self.assertEqual(2, tree.Root.LeftChild.LeftChild.LeftChild.Parent.NodeKey)
        self.assertEqual(3, tree.Root.LeftChild.LeftChild.RightChild.NodeKey)
        self.assertEqual(3, tree.Root.LeftChild.LeftChild.RightChild.Level)
        self.assertEqual(2, tree.Root.LeftChild.LeftChild.RightChild.Parent.NodeKey)

        self.assertEqual(5, tree.Root.LeftChild.RightChild.LeftChild.NodeKey)
        self.assertEqual(3, tree.Root.LeftChild.RightChild.LeftChild.Level)
        self.assertEqual(6, tree.Root.LeftChild.RightChild.LeftChild.Parent.NodeKey)

        self.assertEqual(13, tree.Root.RightChild.NodeKey)
        self.assertEqual(1, tree.Root.LeftChild.Level)
        self.assertEqual(8, tree.Root.LeftChild.Parent.NodeKey)

    def test_is_right_only_root(self):
        arr: list = [8]
        tree: BalancedBST2 = BalancedBST2()
        tree.GenerateTree(arr)
        self.assertTrue(tree.is_right(tree.Root))

    def test_is_right_small_tree(self):
        arr: list = [8, 4, 10]
        tree: BalancedBST2 = BalancedBST2()
        tree.GenerateTree(arr)
        self.assertTrue(tree.is_right(tree.Root))

    def test_is_right_big_tree(self):
        arr: list = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 11, 15, 13]
        tree: BalancedBST2 = BalancedBST2()
        tree.GenerateTree(arr)
        self.assertTrue(tree.is_right(tree.Root))

    def test_is_right_negative(self):
        arr: list = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 11, 15, 13]
        tree: BalancedBST2 = BalancedBST2()
        tree.GenerateTree(arr)
        tree.Root.LeftChild.LeftChild.LeftChild, tree.Root.LeftChild.LeftChild.RightChild = (
            tree.Root.LeftChild.LeftChild.RightChild, tree.Root.LeftChild.LeftChild.LeftChild)
        self.assertFalse(tree.is_right(tree.Root))

    def test_isBalanced_only_root(self):
        arr: list = [8]
        tree: BalancedBST = BalancedBST()
        tree.GenerateTree(arr)
        self.assertTrue(tree.IsBalanced(tree.Root))

    def test_isBalanced_small_tree(self):
        arr: list = [8, 4, 10]
        tree: BalancedBST = BalancedBST()
        tree.GenerateTree(arr)
        self.assertTrue(tree.IsBalanced(tree.Root))

    def test_isBalanced_big_tree(self):
        arr: list = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 11, 15, 13]
        tree: BalancedBST = BalancedBST()
        tree.GenerateTree(arr)
        self.assertTrue(tree.IsBalanced(tree.Root))

    def test_isBalanced_negative(self):
        arr: list = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 11, 15, 13]
        tree: BalancedBST = BalancedBST()
        tree.GenerateTree(arr)
        self.assertEqual(1, tree.Root.LeftChild.LeftChild.LeftChild.NodeKey)
        self.assertEqual(3, tree.Root.LeftChild.LeftChild.RightChild.NodeKey)

        tree.Root.LeftChild.LeftChild.RightChild.Parent = tree.Root.LeftChild.LeftChild.LeftChild
        tree.Root.LeftChild.LeftChild.RightChild.Level = 4
        tree.Root.LeftChild.LeftChild.LeftChild.RightChild = tree.Root.LeftChild.LeftChild.RightChild
        tree.Root.LeftChild.LeftChild.RightChild = None

        self.assertFalse(tree.IsBalanced(tree.Root))
