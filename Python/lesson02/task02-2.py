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

    # Рефлексия (техдолг):
    # 2. Двоичные деревья поиска
    # 2.1.* метод, проверяющий, идентично ли текущее дерево дереву-параметру.
    # Здесь сначала проверяю количество узлов для раннего выхода, чтобы не перебирать узлы заведомо неидентичных деревьев.
    # И только при равенстве рекурсивно проверяю сначала левое поддерево, потом правое

    # 2. Двоичные деревья поиска
    # 2.2.* метод, который находит все пути от корня к листьям, длина которых равна заданной величине.
    # Алгоритм решения следующий: начиная с корня рекурсивно обрабатывает левые поддеревья, затем правые, накапливая путь из узлов в массиве.
    # Останавливаюсь либо на листе, либо при превышении заданной глубины depth. При равенстве уровня листа и depth в результирующий список добавляется сохраненный путь.
    # При возврате обратно по стеку вызовов из текущего пути удаляем конечные неподходящие узлы (с учетом необходимости пройти правое дерево -
    # т.е. при возврате с левого поддерева мы текущий узел из пути не удаляем, пока не пройдем правое поддерево)
    # Пути дальнейшей оптимизации/упрощения решения: если для каждого узла хранить его уровень, можно избавиться от модфицирования параметра depth в рекурсивных вызовах.
    # А в целом, алгоритм представляет собой несколько усложненный и "грязноватый" pre-order DFS из следующего занятия.

    # 2. Двоичные деревья поиска
    # 2.3.* метод, который находит все пути от корня к листьям, чтобы сумма значений узлов была максимальной.
    # Аналогичный алгоритм обхода узлов, как и в предыдущей задаче с одним лишь различием - нет ранней остановки по достижению глубины. Самое главное по этим двум задачам не учел, что они "одинаковые".
    # Т.к. в первой из них есть еще ограничитель depth, как-то они подсознательно не соединились в одну. Собственно очевидное сходство и необходимость избавления от копипасты я осознал после разбора код ревью,
    # где сигнатуры отобразились визуально рядом. И хотя проблемы указаны разные для этих двух методов они как раз однотипные для обоих (т.е. обе проблемы присутствуют в каждом методе).
    # В общем конечно очень плохо, что при написании кода у меня произошло очередное игнорирование правильного написания таких конструкций (и в третьем занятии аналогично), только в текущем занятии добавил лямбду в обход дерева.

    # 2. Двоичные деревья поиска
    # 2.4.* метод проверки, симметрично ли дерево относительно своего корня.
    # Здесь алгоритм достаточно очевидный. От корня берем левого наследника и правого наследника и у них рекурсивно сравниваем (наличие + value) узлов левого поддерева с узлами правого поддерева противоположного узла
    # и наоборот - узлов правого поддерева с узлами левого поддерева. Решение с эталонным алгоритмом совпало.