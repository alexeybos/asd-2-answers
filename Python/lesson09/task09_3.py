from unittest import TestCase
from task09 import SimpleTree, SimpleTreeNode
from task09_2 import SimpleTree as SimpleTree2, SimpleTreeNode as SimpleTreeNode2

class TestHeap(TestCase):
    def setUp(self):
        self.root_tree_node = SimpleTreeNode(1, None)
        self.big_tree = SimpleTree(self.root_tree_node)
        # 7 nodes
        #       (1)
        #     /     \
        #   (2)     (3)
        #          /   \
        #        (4)    (5)
        #              /   \
        #            (6)   (7)
        self.tree_node1 = SimpleTreeNode(2, None)
        self.big_tree.AddChild(self.root_tree_node, self.tree_node1)
        self.tree_node2 = SimpleTreeNode(3, None)
        self.big_tree.AddChild(self.root_tree_node, self.tree_node2)
        self.tree_node3 = SimpleTreeNode(4, None)
        self.big_tree.AddChild(self.tree_node2, self.tree_node3)
        self.tree_node4 = SimpleTreeNode(5, None)
        self.big_tree.AddChild(self.tree_node2, self.tree_node4)
        tree_node5 = SimpleTreeNode(6, None)
        self.big_tree.AddChild(self.tree_node4, tree_node5)
        tree_node6 = SimpleTreeNode(7, None)
        self.big_tree.AddChild(self.tree_node4, tree_node6)


    def test_EvenTrees(self):
        tree_node7 = SimpleTreeNode(8, None)
        self.big_tree.AddChild(self.tree_node4, tree_node7)
        to_forest: list[SimpleTreeNode] = self.big_tree.EvenTrees()
        self.assertEqual(4, len(to_forest))
        self.assertEqual(1, to_forest[0].NodeValue)
        self.assertEqual(3, to_forest[1].NodeValue)
        self.assertEqual(3, to_forest[2].NodeValue)
        self.assertEqual(5, to_forest[3].NodeValue)

    def test_EvenTrees_empty(self):
        tree: SimpleTree = SimpleTree(None)
        self.assertEqual(0, len(tree.EvenTrees()))

    def test_EvenTrees_one_root(self):
        tree: SimpleTree = SimpleTree(SimpleTreeNode(1, None))
        self.assertEqual(0, len(tree.EvenTrees()))

    def test_EvenTrees_odd(self):
        self.assertEqual(0, len(self.big_tree.EvenTrees()))

    def test_EvenTrees_even(self):
        tree_node7 = SimpleTreeNode(8, None)
        self.big_tree.AddChild(self.tree_node1, tree_node7)
        to_forest: list[SimpleTreeNode] = self.big_tree.EvenTrees()
        self.assertEqual(2, len(to_forest))
        self.assertEqual(1, to_forest[0].NodeValue)
        self.assertEqual(2, to_forest[1].NodeValue)

    def test_balance_tree(self):
        root_tree_node = SimpleTreeNode2(1, None)
        big_tree = SimpleTree2(root_tree_node)
        # 6 nodes
        #       (1)
        #     /     \
        #   (2)     (3)
        #          /   \
        #        (4)    (5)
        #              /
        #            (6)
        tree_node1 = SimpleTreeNode2(2, None)
        big_tree.AddChild(root_tree_node, tree_node1)
        tree_node2 = SimpleTreeNode2(3, None)
        big_tree.AddChild(root_tree_node, tree_node2)
        tree_node3 = SimpleTreeNode2(4, None)
        big_tree.AddChild(tree_node2, tree_node3)
        tree_node4 = SimpleTreeNode2(5, None)
        big_tree.AddChild(tree_node2, tree_node4)
        tree_node5 = SimpleTreeNode2(6, None)
        big_tree.AddChild(tree_node4, tree_node5)
        leaves: list[SimpleTreeNode2] = big_tree.get_leaves(big_tree.Root, [])
        leaves.sort(key=lambda x: x.level)
        self.assertTrue((leaves[len(leaves) - 1].level - leaves[0].level) > 1)
        big_tree.balance_tree()
        leaves = big_tree.get_leaves(big_tree.Root, [])
        leaves.sort(key=lambda x: x.level)
        leaves: list[SimpleTreeNode2] = big_tree.get_leaves(big_tree.Root, [])
        leaves.sort(key=lambda x: x.level)
        self.assertTrue((leaves[len(leaves) - 1].level - leaves[0].level) < 2)

        nodes: list[SimpleTreeNode2] = big_tree.GetAllNodes()
        self.assertEqual(6, len(nodes))

        nodes.sort(key=lambda x: x.NodeValue)
        for i in range(6):
            self.assertEqual(i + 1, nodes[i].NodeValue)

    def test_count_even_trees(self):
        root_tree_node = SimpleTreeNode2(1, None)
        big_tree = SimpleTree2(root_tree_node)
        # 6 nodes
        #       (1)
        #     /     \
        #   (2)     (3)
        #          /   \
        #        (4)    (5)
        #              /
        #            (6)
        tree_node1 = SimpleTreeNode2(2, None)
        big_tree.AddChild(root_tree_node, tree_node1)
        tree_node2 = SimpleTreeNode2(3, None)
        big_tree.AddChild(root_tree_node, tree_node2)
        tree_node3 = SimpleTreeNode2(4, None)
        big_tree.AddChild(tree_node2, tree_node3)
        tree_node4 = SimpleTreeNode2(5, None)
        big_tree.AddChild(tree_node2, tree_node4)
        tree_node5 = SimpleTreeNode2(6, None)
        big_tree.AddChild(tree_node4, tree_node5)
        self.assertEqual(2, big_tree.get_even_trees_count(big_tree.Root))

        tree_node6 = SimpleTreeNode(7, None)
        big_tree.AddChild(tree_node4, tree_node6)
        self.assertEqual(0, big_tree.get_even_trees_count(big_tree.Root))