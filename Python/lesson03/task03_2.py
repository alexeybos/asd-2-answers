from collections import deque
from typing import Callable

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

    # Рефлексия (техдолг):
    # 3. Способы обхода дерева
    # 3.3 Реализуйте алгоритм инвертирования дерева.
    # Для инвертирования дерева выбрал DFS, хотя мне сложно сказать что вот прям сознательно. По времени сложность у BFS и DFS одинаковая O(n), по памяти зависит от глубины дерева для DFS, и от ширины для BFS.
    # В целом DFS как-то более естественно смотрится в этой задаче (чисто для меня). Использовался post-order - опять же по причине некоей привычности подхода "сначала упереться в дно, потом подниматься",
    # аргумента по меньшей глубины рекурсии для pre-order обхода при обдумывании способа решения задачи я также не видел в моменте.

    # 3. Способы обхода дерева
    # 3.4 Добавьте метод, который находит уровень в текущем дереве, сумма значений узлов на котором максимальна
    # Здесь по условию задачи по сути явно проговаривается использование BFS в решении, т.к. движемся по уровням дерева - собственно его и использовал.
    # Ну и привычно к сожалению вновь без копипасты обхода не обошлось, т.е. логику суммирования я не выделил в отдельный метод, а все зашито непосредственно в обходе дерева.
    # Здесь надо будет опять поработать надо собой и кодом (добавил в конце после рефлексии такую реализацию).

    # 3. Способы обхода дерева
    # 3.5 разработайте функцию для восстановления оригинального дерева по результатам обхода дерева в префиксном и инфиксном порядке
    # Т.к. в задании не сказано, что это бинарное дерево поиска, да и в качестве примера дано не дерево поиска, по префиксному массиву мы однозначно восстановить дерево не можем.
    # Поэтому определяем порядок следования узлов по префиксному массиву, а по инфиксному уже однозначно определяем, с какой стороны от корня нужно расположить очередной узел.
    # Для бинарного дерева поиска действительно достаточно только префиксного массива, т.к. мы точно знаем с какой стороны вершины находятся узлы с ключами больше/меньше.

    # встраивание логики подсчета суммы и формирования в обход дерева
    ProcessNodeOnLevel = Callable[[BSTNode, int], None]

    def standart_BFS(self, processor: ProcessNodeOnLevel) -> None:
        queue: deque = deque([self.Root])
        cur_level = 0
        while queue:
            level_size = len(queue)
            for index in range(level_size):
                cur_node = queue.popleft()
                if cur_node.LeftChild is not None:
                    queue.append(cur_node.LeftChild)
                if cur_node.RightChild is not None:
                    queue.append(cur_node.RightChild)
                processor(cur_node, cur_level)
            cur_level += 1

    def get_level_with_max_sum_new(self) -> tuple:
        max_level_nodes: list = []
        current_level_nodes: list = []
        max_sum: int = 0
        current_sum: int = 0
        current_level: int = 0
        def process_sum(node: BSTNode, level: int) -> None:
            nonlocal current_sum, current_level, max_sum, current_level_nodes, max_level_nodes
            if current_level == level:
                current_sum += node.NodeValue
                current_level_nodes.append(node)
                return
            current_level = level
            if current_sum > max_sum:
                max_sum = current_sum
                max_level_nodes = current_level_nodes.copy()
                current_level_nodes = [node]
        self.standart_BFS(process_sum)

        if current_sum > max_sum:
            return tuple(current_level_nodes)
        return tuple(max_level_nodes)