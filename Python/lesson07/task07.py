
class Heap:

    def __init__(self):
        self.HeapArray = []

    def MakeHeap(self, a, depth):
        self.HeapArray = [None] * ((2 ** (depth + 1)) - 1)
        a.sort(reverse=True)
        for i in range(len(a)):
            self.HeapArray[i] = a[i]

    def GetMax(self):
        if len(self.HeapArray) == 0 or self.HeapArray[0] is None:
            return -1
        max_node: int = self.HeapArray[0]
        last_node: int = self._get_last_node_index()
        self.HeapArray[0], self.HeapArray[last_node] = self.HeapArray[last_node], None
        self._sift_down(0, last_node - 1)
        return max_node

    def _sift_down(self, ind: int, last_node: int) -> None:
        child: int = 2 * ind + 1
        if child > last_node:
            return
        if child + 1 <= last_node and self.HeapArray[child + 1] > self.HeapArray[child]:
            child += 1
        if self.HeapArray[ind] < self.HeapArray[child]:
            self.HeapArray[ind], self.HeapArray[child] = self.HeapArray[child], self.HeapArray[ind]
            self._sift_down(child, last_node)

    def _get_last_node_index(self) -> int:
        for i in range(len(self.HeapArray) - 1, -1, -1):
            if self.HeapArray[i] is not None:
                return i
        return -1

    def Add(self, key):
        last_ind: int = self._get_last_node_index()
        if last_ind == len(self.HeapArray) - 1:
            return False
        self.HeapArray[last_ind + 1] = key
        self._sift_up(last_ind + 1)
        return True

    def _sift_up(self, ind: int) -> None:
        parent: int = int((ind - 1) / 2)
        if parent < 0:
            return
        if self.HeapArray[parent] < self.HeapArray[ind]:
            self.HeapArray[parent], self.HeapArray[ind] = self.HeapArray[ind], self.HeapArray[parent]
            self._sift_up(parent)




