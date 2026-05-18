from unittest import TestCase

from ASD2.lesson03.task03 import BST, BSTFind, BSTNode

class Test(TestCase):
    def setUp(self):
        self.big_tree_node1 = BSTNode(8, '8', None)
        self.big_tree_node2 = BSTNode(4, '4', self.big_tree_node1)
        self.big_tree_node3 = BSTNode(12, '12', self.big_tree_node1)
        self.big_tree_node1.LeftChild = self.big_tree_node2
        self.big_tree_node1.RightChild = self.big_tree_node3
        self.big_tree_node4 = BSTNode(2, '2', self.big_tree_node2)
        self.big_tree_node5 = BSTNode(6, '6', self.big_tree_node2)
        self.big_tree_node2.LeftChild = self.big_tree_node4
        self.big_tree_node2.RightChild = self.big_tree_node5
        self.big_tree_node6 = BSTNode(10, '10', self.big_tree_node3)
        self.big_tree_node7 = BSTNode(14, '14', self.big_tree_node3)
        self.big_tree_node3.LeftChild = self.big_tree_node6
        self.big_tree_node3.RightChild = self.big_tree_node7
        self.big_tree_node8 = BSTNode(3, '3', self.big_tree_node4)
        self.big_tree_node4.RightChild = self.big_tree_node8
        self.big_tree = BST(self.big_tree_node1)
        self.big_tree.cnt = 8

    def test_WideAllNodes_empty(self):
        tree = BST(None)
        wide = tree.WideAllNodes()
        self.assertEqual((), wide)

    def test_WideAllNodes_one_root(self):
        parent = BSTNode(8, '8', None)
        tree = BST(parent)
        wide = tree.WideAllNodes()
        self.assertEqual(1, len(wide))
        self.assertEqual(8, wide[0].NodeKey)

    def test_WideAllNodes(self):
        wide = self.big_tree.WideAllNodes()
        self.assertEqual(8, len(wide))
        self.assertEqual(8, wide[0].NodeKey)
        self.assertEqual(4, wide[1].NodeKey)
        self.assertEqual(12, wide[2].NodeKey)
        self.assertEqual(2, wide[3].NodeKey)
        self.assertEqual(6, wide[4].NodeKey)
        self.assertEqual(10, wide[5].NodeKey)
        self.assertEqual(14, wide[6].NodeKey)
        self.assertEqual(3, wide[7].NodeKey)

    def test_DeepAllNodes_empty(self):
        tree = BST(None)
        deep = tree.DeepAllNodes(0)
        self.assertEqual((), deep)

    def test_DeepAllNodes_one_root(self):
        parent = BSTNode(8, '8', None)
        tree = BST(parent)
        deep = tree.DeepAllNodes(0)
        self.assertEqual(1, len(deep))
        self.assertEqual(8, deep[0].NodeKey)

    def test_DeepAllNodes_in_order(self):
        deep = self.big_tree.DeepAllNodes(0)
        self.assertEqual(8, len(deep))
        self.assertEqual(2, deep[0].NodeKey)
        self.assertEqual(3, deep[1].NodeKey)
        self.assertEqual(4, deep[2].NodeKey)
        self.assertEqual(6, deep[3].NodeKey)
        self.assertEqual(8, deep[4].NodeKey)
        self.assertEqual(10, deep[5].NodeKey)
        self.assertEqual(12, deep[6].NodeKey)
        self.assertEqual(14, deep[7].NodeKey)

    def test_DeepAllNodes_pre_order(self):
        deep = self.big_tree.DeepAllNodes(2)
        self.assertEqual(8, len(deep))
        self.assertEqual(8, deep[0].NodeKey)
        self.assertEqual(4, deep[1].NodeKey)
        self.assertEqual(2, deep[2].NodeKey)
        self.assertEqual(3, deep[3].NodeKey)
        self.assertEqual(6, deep[4].NodeKey)
        self.assertEqual(12, deep[5].NodeKey)
        self.assertEqual(10, deep[6].NodeKey)
        self.assertEqual(14, deep[7].NodeKey)

    def test_DeepAllNodes_post_order(self):
        deep = self.big_tree.DeepAllNodes(1)
        self.assertEqual(8, len(deep))
        self.assertEqual(3, deep[0].NodeKey)
        self.assertEqual(2, deep[1].NodeKey)
        self.assertEqual(6, deep[2].NodeKey)
        self.assertEqual(4, deep[3].NodeKey)
        self.assertEqual(10, deep[4].NodeKey)
        self.assertEqual(14, deep[5].NodeKey)
        self.assertEqual(12, deep[6].NodeKey)
        self.assertEqual(8, deep[7].NodeKey)
