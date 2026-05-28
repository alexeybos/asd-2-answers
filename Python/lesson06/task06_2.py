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

    # 6. Строим сбалансированные двоичные деревья поиска (2)
    # 6.2.* Добавьте метод проверки, действительно ли дерево получилось правильным
    # Сложность: время O(n), память O(h), где h высота дерева
    def is_right(self, root_node: BSTNode | None) -> bool:
        if root_node is None:
            return True
        left = root_node.LeftChild
        right = root_node.RightChild
        if left is not None and left.NodeKey >= root_node.NodeKey:
            return False
        if right is not None and right.NodeKey < root_node.NodeKey:
            return False
        left_result = self.is_right(left)
        if not left_result:
            return False
        return self.is_right(right)

    # 6. Строим сбалансированные двоичные деревья поиска (2)
    # 6.3.* Добавьте метод проверки, действительно ли дерево получилось сбалансированным
    # Сложность: время O(n), память O(h), где h высота дерева
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


    # Рефлексия по 6.2.* Добавьте метод проверки, действительно ли дерево получилось правильным.
    # Здесь реализовал одной рекурсивной функцией, с передачей текущего корневого узла. В принципе, для красоты можно было бы сделать отдельный метод-обертку без параметров, но сделал по аналогии с isBalanced.
    # Обход дерева DFS pre-order. Опять же, сделал по рекомендованному в задании алгоритму, но есть подозрение, что данная проверка не полная - проверяю на соответствие "ближайшую" тройку корень-левый-правый потомки,
    # но глобально, например, в правом поддереве где-то дальше может оказаться элемент меньше, чем текущий корень, от которого растет этот правый потомок.
    # Тогда, насколько я понимаю, дерево будет неправильным, но данный метод этого не увидит.

    # Рефлексия по 6.3.* Добавьте метод проверки, действительно ли дерево получилось сбалансированным
    # Здесь, в отличие от 6.2, есть и метод-обертка и сама рекурсивная функция. Одной функцией реализовать не получилось. Сначала сделал без передачи дополнительного параметра root_level,
    # который используется в случае отсутствия узла, но при такой реализации получилось еще больше дополнительных проверок в функции. Так что остановился на данном варианте с доп параметром.

    # Рефлексия по эталонным решениям для занятия 4. Двоичные деревья поиска (2):
    # для 4.2 Поиск наименьшего общего предка (LCA): тут, исходя из формулировки задания (а точнее из формулировки вопроса) реализовал решение не классической рекурсией, а итерационно, с использованием индексов.
    # Если я не ошибся при подсчете сложности, в случае массива по оценке времени алгоритмы одинаковы, а для памяти в итерационном варианте O(1), тогда как рекурсивный даст O(h)
    #
    # для 4.3 Переделайте метод обход дерева в ширину, оптимизируя его за счёт прямого доступа к элементам массива
    # В данном решении, в отличие от эталонного, я вообще не использовал очередь. Фактически же массив - это уже результат BFS, только с лишними пустыми узлами, поэтому задачу решил просто итерацией по массиву.
    # Ну и здесь скорее получилась не оптимизация, а упрощение.


