from unittest import TestCase

from ASD2.lesson02.task02 import BST, BSTFind, BSTNode

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

    def test_find_in_empty(self):
        tree = BST(None)
        find_res = tree.FindNodeByKey(8)
        self.assertIsNone(find_res.Node)
        self.assertFalse(find_res.NodeHasKey)
        self.assertFalse(find_res.ToLeft)

    def test_find_in_only_parent_find(self):
        parent = BSTNode(8, '8', None)
        tree = BST(parent)
        find_res = tree.FindNodeByKey(8)
        self.assertEqual(8, find_res.Node.NodeKey)
        self.assertEqual('8', find_res.Node.NodeValue)
        self.assertIsNone(find_res.Node.Parent)
        self.assertTrue(find_res.NodeHasKey)
        self.assertFalse(find_res.ToLeft)

    def test_find_in_only_parent_left(self):
        parent = BSTNode(8, '8', None)
        tree = BST(parent)
        find_res = tree.FindNodeByKey(4)
        self.assertEqual(8, find_res.Node.NodeKey)
        self.assertEqual('8', find_res.Node.NodeValue)
        self.assertIsNone(find_res.Node.Parent)
        self.assertFalse(find_res.NodeHasKey)
        self.assertTrue(find_res.ToLeft)

    def test_find_in_only_parent_right(self):
        parent = BSTNode(8, '8', None)
        tree = BST(parent)
        find_res = tree.FindNodeByKey(12)
        self.assertEqual(8, find_res.Node.NodeKey)
        self.assertEqual('8', find_res.Node.NodeValue)
        self.assertIsNone(find_res.Node.Parent)
        self.assertFalse(find_res.NodeHasKey)
        self.assertFalse(find_res.ToLeft)

    def test_find_in_big_tree_positive(self):
        find_res = self.big_tree.FindNodeByKey(3)
        self.assertEqual(3, find_res.Node.NodeKey)
        self.assertEqual('3', find_res.Node.NodeValue)
        self.assertEqual('2', find_res.Node.Parent.NodeValue)
        self.assertTrue(find_res.NodeHasKey)
        self.assertFalse(find_res.ToLeft)

    def test_find_in_big_tree_left(self):
        find_res = self.big_tree.FindNodeByKey(13)
        self.assertEqual(14, find_res.Node.NodeKey)
        self.assertEqual('14', find_res.Node.NodeValue)
        self.assertEqual('12', find_res.Node.Parent.NodeValue)
        self.assertFalse(find_res.NodeHasKey)
        self.assertTrue(find_res.ToLeft)

    def test_find_in_big_tree_right(self):
        find_res = self.big_tree.FindNodeByKey(7)
        self.assertEqual(6, find_res.Node.NodeKey)
        self.assertEqual('6', find_res.Node.NodeValue)
        self.assertEqual('4', find_res.Node.Parent.NodeValue)
        self.assertFalse(find_res.NodeHasKey)
        self.assertFalse(find_res.ToLeft)

    def test_AddKeyValue_to_empty(self):
        tree = BST(None)
        result = tree.AddKeyValue(8, '8')
        self.assertTrue(result)
        find_res = tree.FindNodeByKey(8)
        self.assertEqual(8, find_res.Node.NodeKey)
        self.assertEqual('8', find_res.Node.NodeValue)
        self.assertIsNone(find_res.Node.Parent)
        self.assertTrue(find_res.NodeHasKey)
        self.assertFalse(find_res.ToLeft)

    def test_AddKeyValue_to_big_tree_right(self):
        find_res = self.big_tree.FindNodeByKey(11)
        self.assertEqual(10, find_res.Node.NodeKey)
        self.assertEqual('10', find_res.Node.NodeValue)
        self.assertEqual('12', find_res.Node.Parent.NodeValue)
        self.assertFalse(find_res.NodeHasKey)
        self.assertFalse(find_res.ToLeft)
        result = self.big_tree.AddKeyValue(11, '11')
        self.assertTrue(result)
        find_res = self.big_tree.FindNodeByKey(11)
        self.assertEqual(11, find_res.Node.NodeKey)
        self.assertEqual('11', find_res.Node.NodeValue)
        self.assertEqual('10', find_res.Node.Parent.NodeValue)
        self.assertTrue(find_res.NodeHasKey)
        self.assertFalse(find_res.ToLeft)


    def test_AddKeyValue_to_big_tree_left(self):
        find_res = self.big_tree.FindNodeByKey(1)
        self.assertEqual(2, find_res.Node.NodeKey)
        self.assertEqual('2', find_res.Node.NodeValue)
        self.assertEqual('4', find_res.Node.Parent.NodeValue)
        self.assertFalse(find_res.NodeHasKey)
        self.assertTrue(find_res.ToLeft)
        result = self.big_tree.AddKeyValue(1, '1')
        self.assertTrue(result)
        find_res = self.big_tree.FindNodeByKey(1)
        self.assertEqual(1, find_res.Node.NodeKey)
        self.assertEqual('1', find_res.Node.NodeValue)
        self.assertEqual('2', find_res.Node.Parent.NodeValue)
        self.assertTrue(find_res.NodeHasKey)
        self.assertFalse(find_res.ToLeft)

    def test_AddKeyValue_to_big_tree_key_exists(self):
        find_res = self.big_tree.FindNodeByKey(10)
        self.assertEqual(self.big_tree_node6, find_res.Node)
        result = self.big_tree.AddKeyValue(10, '100')
        self.assertFalse(result)
        find_res = self.big_tree.FindNodeByKey(10)
        self.assertEqual(self.big_tree_node6, find_res.Node)
        self.assertEqual('10', find_res.Node.NodeValue)

    def test_find_min_in_empty(self):
        tree = BST(None)
        node = tree.FinMinMax(None, False)
        self.assertIsNone(node)

    def test_find_max_in_empty(self):
        tree = BST(None)
        node = tree.FinMinMax(None, True)
        self.assertIsNone(node)

    def test_find_min_in_only_parent(self):
        parent = BSTNode(8, '8', None)
        tree = BST(parent)
        node = tree.FinMinMax(parent, False)
        self.assertEqual(8, node.NodeKey)
        self.assertEqual('8', node.NodeValue)

    def test_find_max_in_only_parent(self):
        parent = BSTNode(8, '8', None)
        tree = BST(parent)
        node = tree.FinMinMax(parent, True)
        self.assertEqual(8, node.NodeKey)
        self.assertEqual('8', node.NodeValue)

    def test_find_min_in_big_tree(self):
        result = self.big_tree.FinMinMax(self.big_tree.Root, False)
        self.assertEqual(2, result.NodeKey)
        self.assertEqual('2', result.NodeValue)

    def test_find_max_in_big_tree(self):
        result = self.big_tree.FinMinMax(self.big_tree.Root, True)
        self.assertEqual(14, result.NodeKey)
        self.assertEqual('14', result.NodeValue)

    def test_find_min_in_subtree(self):
        result = self.big_tree.FinMinMax(self.big_tree_node3, False)
        self.assertEqual(10, result.NodeKey)
        self.assertEqual('10', result.NodeValue)

    def test_find_max_in_subtree(self):
        result = self.big_tree.FinMinMax(self.big_tree_node2, True)
        self.assertEqual(6, result.NodeKey)
        self.assertEqual('6', result.NodeValue)

    def test_DeleteNodeByKey_from_empty(self):
        tree = BST(None)
        del_res = tree.DeleteNodeByKey(1)
        self.assertFalse(del_res)

    def test_DeleteNodeByKey_only_root(self):
        root = BSTNode(8, '8', None)
        tree = BST(root)
        self.assertEqual(root, tree.Root)
        self.assertEqual(1, tree.Count())
        del_res = tree.DeleteNodeByKey(8)
        self.assertTrue(del_res)
        self.assertIsNone(tree.Root)
        self.assertEqual(0, tree.Count())

    def test_DeleteNodeByKey_leaf(self):
        find_res = self.big_tree.FindNodeByKey(10)
        self.assertEqual(8, self.big_tree.Count())
        self.assertTrue(find_res.NodeHasKey)
        del_res = self.big_tree.DeleteNodeByKey(10)
        self.assertTrue(del_res)
        self.assertIsNone(self.big_tree_node3.LeftChild)
        self.assertEqual(12, self.big_tree_node3.NodeKey)
        find_res = self.big_tree.FindNodeByKey(10)
        self.assertEqual(7, self.big_tree.Count())
        self.assertFalse(find_res.NodeHasKey)

    def test_DeleteNodeByKey_next_leaf(self):
        self.big_tree.AddKeyValue(7, '7')
        self.big_tree.AddKeyValue(5, '5')
        find_res = self.big_tree.FindNodeByKey(4)
        self.assertTrue(find_res.NodeHasKey)

        del_res = self.big_tree.DeleteNodeByKey(4)
        self.assertTrue(del_res)
        find_res = self.big_tree.FindNodeByKey(4)
        self.assertFalse(find_res.NodeHasKey)

        self.assertEqual(5, self.big_tree.Root.LeftChild.NodeKey)
        find_res = self.big_tree.FindNodeByKey(5)
        self.assertTrue(find_res.NodeHasKey)
        self.assertEqual(2, find_res.Node.LeftChild.NodeKey)
        self.assertEqual(6, find_res.Node.RightChild.NodeKey)
        find_res = self.big_tree.FindNodeByKey(6)
        self.assertTrue(find_res.NodeHasKey)
        self.assertIsNone(find_res.Node.LeftChild)
        self.assertEqual(7, find_res.Node.RightChild.NodeKey)

    def test_DeleteNodeByKey_lift_right(self):
        self.big_tree.AddKeyValue(9, '9')
        self.big_tree.AddKeyValue(11, '11')
        self.big_tree.AddKeyValue(13, '13')
        self.big_tree.AddKeyValue(15, '15')
        find_res = self.big_tree.FindNodeByKey(8)
        self.assertTrue(find_res.NodeHasKey)

        del_res = self.big_tree.DeleteNodeByKey(8)
        self.assertTrue(del_res)
        find_res = self.big_tree.FindNodeByKey(8)
        self.assertFalse(find_res.NodeHasKey)

        self.assertEqual(9, self.big_tree.Root.NodeKey)
        self.assertIsNone(self.big_tree.Root.Parent)
        find_res = self.big_tree.FindNodeByKey(9)
        self.assertTrue(find_res.NodeHasKey)
        self.assertEqual(4, find_res.Node.LeftChild.NodeKey)
        self.assertEqual(12, find_res.Node.RightChild.NodeKey)
        find_res = self.big_tree.FindNodeByKey(12)
        self.assertTrue(find_res.NodeHasKey)
        self.assertEqual(10, find_res.Node.LeftChild.NodeKey)
        self.assertEqual(14, find_res.Node.RightChild.NodeKey)
        find_res = self.big_tree.FindNodeByKey(10)
        self.assertIsNone(find_res.Node.LeftChild)
        self.assertEqual(11, find_res.Node.RightChild.NodeKey)


    def test_count_empty(self):
        tree = BST(None)
        self.assertEqual(0, tree.Count())

    def test_count_only_root(self):
        root = BSTNode(8, '8', None)
        tree = BST(root)
        self.assertEqual(1, tree.Count())
