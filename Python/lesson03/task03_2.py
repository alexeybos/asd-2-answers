from collections import deque

    # 3. Способы обхода дерева
    # 3.3 Реализуйте алгоритм инвертирования дерева.
    # сложность O(n) - time, пространственная сложность по стеку вызовов: О(h) - высота дерева (в худшем случае так же O(n))
    def invert_tree(self):
        self.swap_children(self.Root)

    def swap_children(self, node):
        if node is None:
            return
        self.swap_children(node.LeftChild)
        self.swap_children(node.RightChild)
        node.RightChild, node.LeftChild = node.LeftChild, node.RightChild

    # 3. Способы обхода дерева
    # 3.4 Добавьте метод, который находит уровень в текущем дереве, сумма значений узлов на котором максимальна
    # сложность O(n) - time, пространственная сложность: O(n) на хранение узлов
    def get_level_with_max_sum(self):
        if self.Root is None:
            return ()
        queue = deque([self.Root])
        current_max = self.Root.NodeKey
        result = [self.Root]
        while queue:
            level_sum = 0
            level_size = len(queue)
            cur_level = []
            for index in range(level_size):
                cur_node = queue.popleft()
                level_sum += cur_node.NodeKey
                cur_level.append(cur_node)
                if cur_node.LeftChild is not None:
                    queue.append(cur_node.LeftChild)
                if cur_node.RightChild is not None:
                    queue.append(cur_node.RightChild)
            if level_sum > current_max:
                result = cur_level.copy()
        return tuple(result)

    # 3. Способы обхода дерева
    # 3.5 разработайте функцию для восстановления оригинального дерева по результатам обхода дерева в префиксном и инфиксном порядке
    # нужны оба прохода для однозначного определения взаимного расположения узлов, т.к. по префиксному проходу мы можем понять только
    # порядок следования узлов, а вот их взаимная конфигурация относительно друг друга проясняется по смещениям "корней" в инфиксном проходе
    # время O(nlogn) - рекурсивный обход всех узлов + поиск текущего корня в массиве inOrder,
    # пространственная: О(nlogn) - (по стеку вызовов O(h) высота дерева (в худшем случае O(n) и + O(nlogn) на хранение временных массивов)

    def restore_tree(self, in_order, pre_order):
        root_pointer = 0
        self.Root, root_pointer = self.restore_sub_tree(None, in_order, pre_order, root_pointer)

    def restore_sub_tree(self, parent, in_order, pre_order, root_pointer):
        if len(in_order) == 0:
            return None, root_pointer
        cur_root = BSTNode(pre_order[root_pointer], None, parent)
        root_position = self.indexOf(in_order, pre_order[root_pointer])
        left = in_order[:root_position]
        right = in_order[root_position + 1:]
        root_pointer += 1
        cur_root.LeftChild, root_pointer = self.restore_sub_tree(cur_root, left, pre_order, root_pointer)
        cur_root.RightChild, root_pointer = self.restore_sub_tree(cur_root, right, pre_order, root_pointer)
        return cur_root, root_pointer

    def indexOf(self, arr, key):
        for i in range(len(arr)):
            if arr[i] == key:
                return i
            i += 1
        return -1

    def standart_BFS(self):
        queue = deque([self.Root])
        cur_level = 0
        while queue:
            level_size = len(queue)
            for index in range(level_size):
                cur_node = queue.popleft()
                if cur_node.LeftChild is not None:
                    queue.append(cur_node.LeftChild)
                if cur_node.RightChild is not None:
                    queue.append(cur_node.RightChild)
                # process_action()
            cur_level += 1