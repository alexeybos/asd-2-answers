from unittest import TestCase
from ASD2.lesson05.task05 import *

class Test(TestCase):

    def test_only_root(self):
        arr: list = [8]
        tree: list = GenerateBBSTArray(arr)
        self.assertEqual(8, tree[0])

    def test_1_depth(self):
        arr: list = [8, 4, 9]
        tree: list = GenerateBBSTArray(arr)
        self.assertEqual(8, tree[0])
        self.assertEqual(4, tree[1])
        self.assertEqual(9, tree[2])

    def test_2_depth(self):
        arr: list = [2, 6, 7, 3, 5, 1, 4]
        tree: list = GenerateBBSTArray(arr)
        self.assertEqual(4, tree[0])
        self.assertEqual(2, tree[1])
        self.assertEqual(6, tree[2])
        self.assertEqual(1, tree[3])
        self.assertEqual(3, tree[4])
        self.assertEqual(5, tree[5])
        self.assertEqual(7, tree[6])

    def test_3_depth(self):
        arr: list = [8, 4, 12, 2, 6, 10, 14, 1, 3, 7, 5, 9, 11, 15, 13]
        tree: list = GenerateBBSTArray(arr)
        self.assertEqual(8, tree[0])
        self.assertEqual(4, tree[1])
        self.assertEqual(12, tree[2])
        self.assertEqual(2, tree[3])
        self.assertEqual(6, tree[4])
        self.assertEqual(10, tree[5])
        self.assertEqual(14, tree[6])
        self.assertEqual(1, tree[7])
        self.assertEqual(3, tree[8])
        self.assertEqual(5, tree[9])
        self.assertEqual(7, tree[10])
        self.assertEqual(9, tree[11])
        self.assertEqual(11, tree[12])
        self.assertEqual(13, tree[13])
        self.assertEqual(15, tree[14])
