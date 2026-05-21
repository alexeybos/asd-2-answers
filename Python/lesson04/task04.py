
class aBST:

    def __init__(self, depth):
        tree_size: int = (2 ** (depth + 1)) - 1
        self.Tree: list = [None] * tree_size

    def FindKeyIndex(self, key):
        if self.Tree[0] is None or self.Tree[0] == key:
            return 0
        return self.find_in_children(key, 0)

    def find_in_children(self, key: int, node: int) -> int | None:
        if self.Tree[node] is None:
            return -node
        if self.Tree[node] == key:
            return node

        if self.Tree[node] > key:
            child: int = 2 * node + 1
        else:
            child: int = 2 * node + 2

        if child >= len(self.Tree):
            return None

        return self.find_in_children(key, child)

    def AddKey(self, key):
        slot: int | None = self.FindKeyIndex(key)
        if slot is None:
            return -1
        self.Tree[abs(slot)] = key
        return abs(slot)






