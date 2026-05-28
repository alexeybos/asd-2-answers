
class BSTNode:

    def __init__(self, key, parent):
        self.NodeKey = key
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None
        self.Level = 0


class BalancedBST:

    def __init__(self):
        self.Root = None

    def GenerateTree(self, a):
        a.sort()
        self.Root = self._generate_sub_tree(None, a, 0)

    def _generate_sub_tree(self, parent: BSTNode | None, arr: list, level: int) -> BSTNode | None:
        if arr is None or len(arr) == 0:
            return None
        middle_index: int = int(len(arr) / 2)
        cur_root: BSTNode = BSTNode(arr[middle_index], parent)
        cur_root.Level = level
        cur_root.LeftChild = self._generate_sub_tree(cur_root, arr[:middle_index], level + 1)
        cur_root.RightChild = self._generate_sub_tree(cur_root, arr[middle_index + 1:], level + 1)
        return cur_root

    def IsBalanced(self, root_node):
        if root_node is None:
            return True
        return self._sub_tree_depth(root_node, root_node.Level) >= 0

    def _sub_tree_depth(self, root_node: BSTNode | None, root_level: int) -> int:
        if root_node is None:
            return root_level
        left_depth: int = self._sub_tree_depth(root_node.LeftChild, root_node.Level)
        if left_depth < 0:
            return -1
        right_depth: int = self._sub_tree_depth(root_node.RightChild, root_node.Level)
        if right_depth < 0 or abs(left_depth - right_depth) > 1:
            return -1
        return max(left_depth, right_depth)





