    # 2. Двоичные деревья поиска
    # 2.1.* метод, проверяющий, идентично ли текущее дерево дереву-параметру.
    # Сложность временная O(n) и пространственная по стеку вызовов: О(h) - высота дерева (в худшем случае O(n))
    def is_equal(self, tree):
        if self.cnt != tree.Count():
            return False
        return self.is_node_equal(self.Root, tree.Root)

    def is_node_equal(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False
        left_subtree_eq = False
        if node1.NodeKey == node2.NodeKey and node1.NodeValue == node2.NodeValue:
            left_subtree_eq = self.is_node_equal(node1.LeftChild, node2.LeftChild)
        if not left_subtree_eq:
            return False
        return self.is_node_equal(node1.RightChild, node2.RightChild)

    # 2. Двоичные деревья поиска
    # 2.2.* метод, который находит все пути от корня к листьям, длина которых равна заданной величине.
    # Сложность временная: O(n), пространственная по стеку вызовов: О(length)
    def get_path_to_leaves(self, length):
        paths = []
        nodes = []
        self.seek_in_depth(self.Root, length, paths, nodes, False)
        return paths

    def seek_in_depth(self, start_node, depth, paths, nodes, exclude_parent):
        if start_node is None:
            if exclude_parent:
                nodes.pop()
            return
        if depth == 0 and start_node.LeftChild is None and start_node.RightChild is None:
            nodes.append(start_node)
            paths.append(nodes.copy())
            nodes.pop()
            return
        if start_node.LeftChild is None and start_node.RightChild is None:
            if exclude_parent:
                nodes.pop()
            return
        nodes.append(start_node)
        self.seek_in_depth(start_node.LeftChild, depth - 1, paths, nodes, False)
        self.seek_in_depth(start_node.RightChild, depth - 1, paths, nodes, True)

    # 2. Двоичные деревья поиска
    # 2.3.* метод, который находит все пути от корня к листьям, чтобы сумма значений узлов была максимальной.
    # Сложность временная: O(n), пространственная по стеку вызовов: О(h) - высота дерева (в худшем случае O(n))
    def get_paths_to_leaves_with_max_sum(self):
        paths = []
        nodes = []
        max = [1]
        self.seek_max_paths_in_depth(self.Root, paths, nodes, max, 0, False)
        return paths

    def seek_max_paths_in_depth(self, start_node, paths, nodes, current_max, sum, exclude_parent):
        if start_node is None:
            if exclude_parent:
                nodes.pop()
            return
        if start_node.RightChild is None and start_node.LeftChild is None:
            if sum >= current_max[0]:
                if sum > current_max[0]:
                    paths.clear()
                    current_max[0] = sum
                    nodes.append(start_node)
                    paths.append(nodes.copy())
                    nodes.pop()
                if exclude_parent:
                    nodes.pop()
                return
        nodes.append(start_node)
        self.seek_max_paths_in_depth(start_node.RightChild, paths, nodes, current_max, sum + start_node.NodeKey, False)
        self.seek_max_paths_in_depth(start_node.LeftChild, paths, nodes, current_max, sum + start_node.NodeKey, True)

    # 2. Двоичные деревья поиска
    # 2.4.* метод проверки, симметрично ли дерево относительно своего корня.
    # Сложность временная: O(n), пространственная по стеку вызовов: О(h) - высота дерева (в худшем случае O(n/2))
    def is_symmetric(self):
        if self.Root is None:
            return False
        return self.is_childes_symmetric(self.Root.LeftChild, self.Root.RightChild)

    def is_childes_symmetric(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if not self.is_childes_symmetric(left.LeftChild, right.RightChild):
            return False
        return self.is_childes_symmetric(left.RightChild, right.LeftChild)