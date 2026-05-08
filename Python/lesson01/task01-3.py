from unittest import TestCase

from ASD2.lesson01.task01 import SimpleTree, SimpleTreeNode


class Test(TestCase):
    def setUp(self):
        self.root_tree_node = SimpleTreeNode('A', None)
        self.big_tree = SimpleTree(self.root_tree_node)
        # 7 nodes, 4 leaves
        self.tree_node1 = SimpleTreeNode('B', None)
        self.big_tree.AddChild(self.root_tree_node, self.tree_node1)
        self.tree_node2 = SimpleTreeNode('C', None)
        self.big_tree.AddChild(self.root_tree_node, self.tree_node2)
        tree_node3 = SimpleTreeNode('D', None)
        self.big_tree.AddChild(self.tree_node2, tree_node3)
        self.tree_node4 = SimpleTreeNode('E', None)
        self.big_tree.AddChild(self.tree_node2, self.tree_node4)
        tree_node5 = SimpleTreeNode('F', None)
        self.big_tree.AddChild(self.tree_node4, tree_node5)
        tree_node6 = SimpleTreeNode('G', None)
        self.big_tree.AddChild(self.tree_node4, tree_node6)

    def test_add_as_root(self):
        tree = SimpleTree(None)
        tree.AddChild(None, SimpleTreeNode('A', None))
        self.assertEqual(tree.Root.NodeValue, 'A')
        self.assertEqual(tree.Root.Parent, None)
        self.assertEqual(len(tree.Root.Children), 0)

    def test_add_as_one_child(self):
        tree_node = SimpleTreeNode('A', None)
        tree = SimpleTree(tree_node)
        tree.AddChild(tree_node, SimpleTreeNode('B', None))
        self.assertEqual(tree.Root.NodeValue, 'A')
        self.assertEqual(tree.Root.Parent, None)
        self.assertEqual(len(tree.Root.Children), 1)
        self.assertEqual(tree.Root.Children[0].NodeValue, 'B')
        self.assertEqual(tree.Root.Children[0].Parent.NodeValue, 'A')
        self.assertEqual(len(tree.Root.Children[0].Children), 0)

    def test_add_as_second_child(self):
        tree_node = SimpleTreeNode('A', None)
        tree = SimpleTree(tree_node)
        tree.AddChild(tree_node, SimpleTreeNode('B', None))
        tree.AddChild(tree_node, SimpleTreeNode('C', None))
        self.assertEqual(tree.Root.NodeValue, 'A')
        self.assertEqual(tree.Root.Parent, None)
        self.assertEqual(len(tree.Root.Children), 2)
        self.assertEqual(tree.Root.Children[0].NodeValue, 'B')
        self.assertEqual(tree.Root.Children[0].Parent.NodeValue, 'A')
        self.assertEqual(len(tree.Root.Children[0].Children), 0)
        self.assertEqual(tree.Root.Children[1].NodeValue, 'C')
        self.assertEqual(tree.Root.Children[1].Parent.NodeValue, 'A')
        self.assertEqual(len(tree.Root.Children[1].Children), 0)

    def test_add_as_child_of_child(self):
        root_tree_node = SimpleTreeNode('A', None)
        tree = SimpleTree(root_tree_node)
        tree_node = SimpleTreeNode('B', None)
        tree.AddChild(root_tree_node, tree_node)
        tree.AddChild(tree_node, SimpleTreeNode('C', None))
        self.assertEqual(tree.Root.NodeValue, 'A')
        self.assertEqual(tree.Root.Parent, None)
        self.assertEqual(len(tree.Root.Children), 1)
        self.assertEqual(tree.Root.Children[0].NodeValue, 'B')
        self.assertEqual(tree.Root.Children[0].Parent.NodeValue, 'A')
        self.assertEqual(len(tree.Root.Children[0].Children), 1)
        self.assertEqual(tree.Root.Children[0].Children[0].NodeValue, 'C')
        self.assertEqual(tree.Root.Children[0].Children[0].Parent.NodeValue, 'B')
        self.assertEqual(len(tree.Root.Children[0].Children[0].Children), 0)

    # тест: проверяем отсутствие удалённого узла и его потомков
    def test_del_in_empty_tree(self):
        tree = SimpleTree(None)
        tree.DeleteNode(None)
        self.assertIsNone(tree.Root)

    def test_del_root(self):
        root_tree_node = SimpleTreeNode('A', None)
        tree = SimpleTree(root_tree_node)
        tree.DeleteNode(root_tree_node)
        self.assertIsNone(tree.Root)

    def test_del_single_child(self):
        root_tree_node = SimpleTreeNode('A', None)
        tree = SimpleTree(root_tree_node)
        tree_node = SimpleTreeNode('B', root_tree_node)
        tree.AddChild(root_tree_node, tree_node)
        self.assertEqual(tree.Root.NodeValue, 'A')
        self.assertEqual(tree.Root.Parent, None)
        self.assertEqual(len(tree.Root.Children), 1)
        self.assertEqual(tree.Root.Children[0].NodeValue, 'B')
        self.assertEqual(tree.Root.Children[0].Parent.NodeValue, 'A')
        self.assertEqual(len(tree.Root.Children[0].Children), 0)
        tree.DeleteNode(tree_node)
        self.assertEqual(tree.Root.NodeValue, 'A')
        self.assertEqual(tree.Root.Parent, None)
        self.assertEqual(len(tree.Root.Children), 0)


    def test_del_not_single_child(self):
        root_tree_node = SimpleTreeNode('A', None)
        tree = SimpleTree(root_tree_node)
        tree_node1 = SimpleTreeNode('B', None)
        tree_node2 = SimpleTreeNode('C', None)
        tree.AddChild(root_tree_node, tree_node1)
        tree.AddChild(root_tree_node, tree_node2)
        self.assertEqual(tree.Root.NodeValue, 'A')
        self.assertEqual(tree.Root.Parent, None)
        self.assertEqual(len(tree.Root.Children), 2)
        self.assertEqual(tree.Root.Children[0].NodeValue, 'B')
        self.assertEqual(tree.Root.Children[0].Parent.NodeValue, 'A')
        self.assertEqual(len(tree.Root.Children[0].Children), 0)
        self.assertEqual(tree.Root.Children[1].NodeValue, 'C')
        self.assertEqual(tree.Root.Children[1].Parent.NodeValue, 'A')
        self.assertEqual(len(tree.Root.Children[1].Children), 0)
        tree.DeleteNode(tree_node1)
        self.assertEqual(tree.Root.NodeValue, 'A')
        self.assertEqual(tree.Root.Parent, None)
        self.assertEqual(len(tree.Root.Children), 1)
        self.assertEqual(tree.Root.Children[0].NodeValue, 'C')
        self.assertEqual(tree.Root.Children[0].Parent.NodeValue, 'A')
        self.assertEqual(len(tree.Root.Children[0].Children), 0)


    def test_del_single_child_this_children(self):
        root_tree_node = SimpleTreeNode('A', None)
        tree = SimpleTree(root_tree_node)
        tree_node = SimpleTreeNode('B', None)
        tree.AddChild(root_tree_node, tree_node)
        tree.AddChild(tree_node, SimpleTreeNode('C', None))
        self.assertEqual(tree.Root.NodeValue, 'A')
        self.assertEqual(tree.Root.Parent, None)
        self.assertEqual(len(tree.Root.Children), 1)
        self.assertEqual(tree.Root.Children[0].NodeValue, 'B')
        self.assertEqual(tree.Root.Children[0].Parent.NodeValue, 'A')
        self.assertEqual(len(tree.Root.Children[0].Children), 1)
        self.assertEqual(tree.Root.Children[0].Children[0].NodeValue, 'C')
        self.assertEqual(tree.Root.Children[0].Children[0].Parent.NodeValue, 'B')
        self.assertEqual(len(tree.Root.Children[0].Children[0].Children), 0)
        tree.DeleteNode(tree_node)
        self.assertEqual(tree.Root.Parent, None)
        self.assertEqual(len(tree.Root.Children), 0)

    def test_GetAllNodes_empty_tree(self):
        tree = SimpleTree(None)
        nodes = tree.GetAllNodes()
        self.assertEqual(len(nodes), 0)

    def test_GetAllNodes_one_root_tree(self):
        root_tree_node = SimpleTreeNode('A', None)
        tree = SimpleTree(root_tree_node)
        nodes = tree.GetAllNodes()
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].NodeValue, 'A')

    def test_GetAllNodes_simple_tree(self):
        root_tree_node = SimpleTreeNode('A', None)
        tree = SimpleTree(root_tree_node)
        tree_node1 = SimpleTreeNode('B', None)
        tree_node2 = SimpleTreeNode('C', None)
        tree.AddChild(root_tree_node, tree_node1)
        tree.AddChild(root_tree_node, tree_node2)
        nodes = tree.GetAllNodes()
        self.assertEqual(len(nodes), 3)
        self.assertEqual(1, nodes.count(root_tree_node))
        self.assertEqual(1, nodes.count(tree_node1))
        self.assertEqual(1, nodes.count(tree_node2))

    def test_GetAllNodes_big_tree(self):
        nodes = self.big_tree.GetAllNodes()
        self.assertEqual(len(nodes), 7)
        self.assertEqual(1, nodes.count(self.root_tree_node))
        values = []
        for node in nodes:
            values.append(node.NodeValue)
        self.assertEqual(1, values.count('A'))
        self.assertEqual(1, values.count('B'))
        self.assertEqual(1, values.count('C'))
        self.assertEqual(1, values.count('D'))
        self.assertEqual(1, values.count('E'))
        self.assertEqual(1, values.count('F'))
        self.assertEqual(1, values.count('G'))

    def test_FindNodesByValue_in_empty_tree(self):
        tree = SimpleTree(None)
        nodes = tree.FindNodesByValue('A')
        self.assertEqual(len(nodes), 0)

    def test_FindNodesByValue_in_one_root_tree_positive(self):
        root_tree_node = SimpleTreeNode('A', None)
        tree = SimpleTree(root_tree_node)
        nodes = tree.FindNodesByValue('A')
        self.assertEqual(1, len(nodes))

    def test_FindNodesByValue_in_one_root_tree_negative(self):
        root_tree_node = SimpleTreeNode('A', None)
        tree = SimpleTree(root_tree_node)
        nodes = tree.FindNodesByValue('B')
        self.assertEqual(0, len(nodes))

    def test_FindNodesByValue_in_big_tree_negative(self):
        nodes = self.big_tree.FindNodesByValue('Q')
        self.assertEqual(0, len(nodes))

    def test_FindNodesByValue_in_big_tree_positive_single(self):
        nodes = self.big_tree.FindNodesByValue('A')
        self.assertEqual(1, len(nodes))
        nodes = self.big_tree.FindNodesByValue('C')
        self.assertEqual(1, len(nodes))
        nodes = self.big_tree.FindNodesByValue('G')
        self.assertEqual(1, len(nodes))
        nodes = self.big_tree.FindNodesByValue('F')
        self.assertEqual(1, len(nodes))
        nodes = self.big_tree.FindNodesByValue('D')
        self.assertEqual(1, len(nodes))

    def test_FindNodesByValue_in_big_tree_positive_list(self):
        self.big_tree.AddChild(self.root_tree_node, SimpleTreeNode('G', None))
        self.big_tree.AddChild(self.root_tree_node.Children[0], SimpleTreeNode('A', None))
        self.big_tree.AddChild(self.root_tree_node.Children[1].Children[0], SimpleTreeNode('A', None))
        nodes = self.big_tree.FindNodesByValue('A')
        self.assertEqual(len(nodes), 3)
        nodes = self.big_tree.FindNodesByValue('G')
        self.assertEqual(len(nodes), 2)
        nodes = self.big_tree.FindNodesByValue('C')
        self.assertEqual(len(nodes), 1)

    def test_MoveNode(self):
        self.assertEqual(0, len(self.tree_node1.Children))
        self.assertEqual(2, len(self.tree_node2.Children))
        self.assertEqual(2, len(self.tree_node4.Children))
        self.big_tree.MoveNode(self.tree_node4, self.tree_node1)
        self.assertEqual(1, len(self.tree_node1.Children))
        self.assertEqual('E', self.tree_node1.Children[0].NodeValue)
        self.assertEqual(1, len(self.tree_node2.Children))
        self.assertEqual('D', self.tree_node2.Children[0].NodeValue)
        self.assertEqual(2, len(self.tree_node4.Children))
        self.assertEqual('F', self.tree_node4.Children[0].NodeValue)
        self.assertEqual('G', self.tree_node4.Children[1].NodeValue)
        nodes = self.big_tree.GetAllNodes()
        self.assertEqual(7, len(nodes))
        self.assertEqual(7, self.big_tree.Count())
        self.assertEqual(3, self.big_tree.LeafCount())

    def test_Count_empty(self):
        tree = SimpleTree(None)
        self.assertEqual(0, tree.Count())

    def test_Count(self):
        self.assertEqual(7, self.big_tree.Count())
        self.big_tree.AddChild(self.tree_node2, SimpleTreeNode('B2', None))
        self.assertEqual(8, self.big_tree.Count())
        self.big_tree.DeleteNode(self.tree_node4)
        self.assertEqual(5, self.big_tree.Count())

    def test_LeafCount_empty(self):
        tree = SimpleTree(None)
        self.assertEqual(0, tree.LeafCount())

    def test_LeafCount(self):
        self.assertEqual(4, self.big_tree.LeafCount())
        self.big_tree.AddChild(self.tree_node1, SimpleTreeNode('B2', None))
        self.assertEqual(4, self.big_tree.LeafCount())
        self.big_tree.DeleteNode(self.tree_node4)
        self.assertEqual(2, self.big_tree.LeafCount())