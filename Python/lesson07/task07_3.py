from unittest import TestCase
from task07 import Heap
from task07_2 import Heap as Heap2

class TestHeap(TestCase):
    def test_MakeHeap_only_root(self):
        heap: Heap = Heap()
        a: list = [8]
        heap.MakeHeap(a, 0)
        self.assertEqual(8, heap.HeapArray[0])
        self.assertEqual(1, len(heap.HeapArray))

    def test_MakeHeap_small(self):
        heap: Heap = Heap()
        a: list = [8, 10, 4]
        heap.MakeHeap(a, 1)
        self.assertEqual(3, len(heap.HeapArray))
        self.assertEqual(10, heap.HeapArray[0])
        self.assertEqual(8, heap.HeapArray[1])
        self.assertEqual(4, heap.HeapArray[2])


    def test_MakeHeap_big(self):
        heap: Heap = Heap()
        a: list = [8, 10, 4, 11, 9, 2, 5, 7, 3, 6, 1]
        heap.MakeHeap(a, 3)
        self.assertEqual(15, len(heap.HeapArray))
        self.assertEqual(11, heap.HeapArray[0])
        self.assertEqual(10, heap.HeapArray[1])
        self.assertEqual(9, heap.HeapArray[2])
        self.assertEqual(8, heap.HeapArray[3])
        self.assertEqual(7, heap.HeapArray[4])
        self.assertEqual(6, heap.HeapArray[5])
        self.assertEqual(5, heap.HeapArray[6])
        self.assertEqual(4, heap.HeapArray[7])
        self.assertEqual(3, heap.HeapArray[8])
        self.assertEqual(2, heap.HeapArray[9])
        self.assertEqual(1, heap.HeapArray[10])
        self.assertIsNone(heap.HeapArray[11])
        self.assertIsNone(heap.HeapArray[12])
        self.assertIsNone(heap.HeapArray[13])
        self.assertIsNone(heap.HeapArray[14])

    def test_getMax_empty(self):
        heap: Heap = Heap()
        heap.MakeHeap([], 0)
        res: int = heap.GetMax()
        self.assertEqual(-1, res)

    def test_getMax_only_root(self):
        heap: Heap = Heap()
        a: list = [8]
        heap.MakeHeap(a, 0)
        res: int = heap.GetMax()
        self.assertEqual(8, res)
        self.assertIsNone(heap.HeapArray[0])

    def test_getMax_small(self):
        heap: Heap = Heap()
        a: list = [8, 10, 4]
        heap.MakeHeap(a, 1)
        res: int = heap.GetMax()
        self.assertEqual(10, res)
        self.assertEqual(8, heap.HeapArray[0])
        self.assertEqual(4, heap.HeapArray[1])
        self.assertIsNone(heap.HeapArray[2])

    def test_getMax_big(self):
        heap: Heap = Heap()
        a: list = [8, 10, 4, 11, 9, 2, 5, 7, 3, 6, 1]
        heap.MakeHeap(a, 3)
        res: int = heap.GetMax()
        self.assertEqual(11, res)
        self.assertEqual(10, heap.HeapArray[0])
        self.assertEqual(10, heap.GetMax())
        self.assertEqual(9, heap.GetMax())
        self.assertEqual(8, heap.GetMax())
        self.assertEqual(7, heap.GetMax())
        self.assertEqual(6, heap.GetMax())
        self.assertEqual(5, heap.GetMax())
        self.assertEqual(4, heap.GetMax())
        self.assertEqual(3, heap.GetMax())
        self.assertEqual(2, heap.GetMax())
        self.assertEqual(1, heap.GetMax())
        self.assertEqual(-1, heap.GetMax())

    def test_Add_to_empty(self):
        heap: Heap = Heap()
        heap.MakeHeap([], 0)
        self.assertTrue(heap.Add(8))
        self.assertFalse(heap.Add(9))
        self.assertEqual(8, heap.HeapArray[0])
        self.assertEqual(8, heap.GetMax())
        self.assertEqual(-1, heap.GetMax())

    def test_Add_to_small(self):
        heap: Heap = Heap()
        heap.MakeHeap([], 1)
        self.assertTrue(heap.Add(8))
        self.assertEqual(8, heap.HeapArray[0])
        self.assertTrue(heap.Add(4))
        self.assertEqual(8, heap.HeapArray[0])
        self.assertTrue(heap.Add(11))
        self.assertEqual(11, heap.HeapArray[0])
        self.assertEqual(4, heap.HeapArray[1])
        self.assertEqual(8, heap.HeapArray[2])

    def test_Add_to_big(self):
        heap: Heap = Heap()
        a: list = [8, 10, 4, 11, 9, 2, 5, 7, 3, 6, 1]
        heap.MakeHeap(a, 3)
        self.assertTrue(heap.Add(15))
        self.assertEqual(15, heap.HeapArray[0])
        self.assertTrue(heap.Add(12))
        self.assertEqual(15, heap.HeapArray[0])
        self.assertIn(12, (heap.HeapArray[1], heap.HeapArray[2]))

    def test_is_correct_empty_or_one_root(self):
        heap: Heap2 = Heap2()
        heap.MakeHeap([], 0)
        self.assertTrue(heap.is_correct())
        heap.Add(5)
        self.assertTrue(heap.is_correct())
        heap.MakeHeap([], 1)
        heap.Add(5)
        self.assertTrue(heap.is_correct())

    def test_is_correct_small_positive(self):
        heap: Heap2 = Heap2()
        a: list = [8, 10, 4]
        heap.MakeHeap(a, 1)
        self.assertTrue(heap.is_correct())

    def test_is_correct_small_negative(self):
        heap: Heap2 = Heap2()
        a: list = [8, 10, 4]
        heap.MakeHeap(a, 1)
        heap.HeapArray[0], heap.HeapArray[1] = heap.HeapArray[1], heap.HeapArray[0]
        self.assertFalse(heap.is_correct())

    def test_is_correct_big_positive(self):
        heap: Heap2 = Heap2()
        a: list = [8, 10, 4, 11, 9, 2, 5, 7, 3, 6, 1]
        heap.MakeHeap(a, 3)
        self.assertTrue(heap.is_correct())

    def test_is_correct_big_negative(self):
        heap: Heap2 = Heap2()
        a: list = [8, 10, 4, 11, 9, 2, 5, 7, 3, 6, 1]
        heap.MakeHeap(a, 3)
        heap.HeapArray[3], heap.HeapArray[7] = heap.HeapArray[7], heap.HeapArray[3]
        self.assertFalse(heap.is_correct())

    def test_find_max_in_range_empty(self):
        heap: Heap2 = Heap2()
        heap.MakeHeap([], 0)
        self.assertIsNone(heap.find_max_in_range(10, 15))

    def test_find_max_in_range_one_root_positive(self):
        heap: Heap2 = Heap2()
        heap.MakeHeap([8], 0)
        self.assertEqual(8, heap.find_max_in_range(8, 15))
        heap.MakeHeap([8], 2)
        self.assertEqual(8, heap.find_max_in_range(8, 15))

    def test_find_max_in_range_one_root_negative(self):
        heap: Heap2 = Heap2()
        heap.MakeHeap([8], 0)
        self.assertIsNone(heap.find_max_in_range(9, 15))
        heap.MakeHeap([8], 2)
        self.assertIsNone(heap.find_max_in_range(9, 15))

    def test_find_max_in_range_big_positive(self):
        heap: Heap2 = Heap2()
        heap.MakeHeap([8, 5, 11, 15, 4, 7, 18, 6], 3)
        self.assertEqual(8, heap.find_max_in_range(5, 10))

    def test_find_max_in_range_big_negative(self):
        heap: Heap2 = Heap2()
        heap.MakeHeap([8, 5, 11, 15, 4, 7, 18, 6], 3)
        self.assertIsNone(heap.find_max_in_range(1, 3))

    def test_union(self):
        heap: Heap2 = Heap2()
        heap.MakeHeap([8, 5, 11, 15, 4, 7, 18, 6], 3)
        heap2: Heap2 = Heap2()
        heap2.MakeHeap([1, 3, 14], 2)
        heap3 = heap.union(heap2)
        self.assertTrue(heap3.is_correct())
        self.assertEqual(18, heap3.HeapArray[0])
        self.assertEqual(7, heap._get_last_node_index())
        self.assertEqual(10, heap3._get_last_node_index())
