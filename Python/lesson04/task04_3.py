from unittest import TestCase

from task04 import aBST

class Test(TestCase):

    def test_create_tree(self):
        tree = aBST(0)
        self.assertEqual(1, len(tree.Tree))
        tree = aBST(1)
        self.assertEqual(3, len(tree.Tree))
        tree = aBST(2)
        self.assertEqual(7, len(tree.Tree))
        tree = aBST(3)
        self.assertEqual(15, len(tree.Tree))
        tree = aBST(4)
        self.assertEqual(31, len(tree.Tree))

    def test_AddKey_to_empty_tree(self):
        tree = aBST(2)
        self.assertEqual(7, len(tree.Tree))
        tree.AddKey(8)
        self.assertEqual(8, tree.Tree[0])
        for i in range(1, 7):
            self.assertIsNone(tree.Tree[i])

    def test_AddKey_to_full_tree(self):
        tree = aBST(2)
        self.assertEqual(7, len(tree.Tree))
        slot = tree.AddKey(8)
        self.assertEqual(8, tree.Tree[0])
        self.assertEqual(0, slot)
        slot = tree.AddKey(4)
        self.assertEqual(1, slot)
        slot = tree.AddKey(12)
        self.assertEqual(2, slot)
        slot = tree.AddKey(6)
        self.assertEqual(4, slot)
        slot = tree.AddKey(10)
        self.assertEqual(5, slot)
        slot = tree.AddKey(2)
        self.assertEqual(3, slot)
        slot = tree.AddKey(14)
        self.assertEqual(6, slot)

        slot = tree.AddKey(100)
        self.assertEqual(-1, slot)

    def test_FindKey_in_full_tree_positive(self):
        tree = aBST(2)
        self.assertEqual(7, len(tree.Tree))
        slot = tree.AddKey(8)
        self.assertEqual(8, tree.Tree[0])
        self.assertEqual(0, slot)
        slot = tree.AddKey(4)
        self.assertEqual(1, slot)
        slot = tree.AddKey(12)
        self.assertEqual(2, slot)
        slot = tree.AddKey(6)
        self.assertEqual(4, slot)
        slot = tree.AddKey(10)
        self.assertEqual(5, slot)
        slot = tree.AddKey(2)
        self.assertEqual(3, slot)
        slot = tree.AddKey(14)
        self.assertEqual(6, slot)

        self.assertEqual(0, tree.FindKeyIndex(8))
        self.assertEqual(1, tree.FindKeyIndex(4))
        self.assertEqual(2, tree.FindKeyIndex(12))
        self.assertEqual(3, tree.FindKeyIndex(2))
        self.assertEqual(4, tree.FindKeyIndex(6))
        self.assertEqual(5, tree.FindKeyIndex(10))
        self.assertEqual(6, tree.FindKeyIndex(14))


    def test_FindKey_in_full_tree_negative(self):
        tree = aBST(2)
        self.assertEqual(7, len(tree.Tree))
        slot = tree.AddKey(8)
        self.assertEqual(8, tree.Tree[0])
        self.assertEqual(0, slot)
        slot = tree.AddKey(4)
        self.assertEqual(1, slot)
        slot = tree.AddKey(12)
        self.assertEqual(2, slot)
        slot = tree.AddKey(6)
        self.assertEqual(4, slot)
        slot = tree.AddKey(10)
        self.assertEqual(5, slot)
        slot = tree.AddKey(2)
        self.assertEqual(3, slot)
        slot = tree.AddKey(14)
        self.assertEqual(6, slot)

        slot = tree.FindKeyIndex(100)
        self.assertIsNone(slot)
