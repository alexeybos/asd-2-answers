# 5. Строим сбалансированные двоичные деревья поиска
# 5.2. Оцените, насколько поиск узла в дереве, представленном в виде массива, эффективнее (или неэффективнее) поиска узла в классическом дереве с указателями.
# Если просто оценить сложность, то в обеих реализациях получается, если не ошибаюсь, сложность O(log n) по времени и O(h) по памяти (O(n) в худшем).
# Так что "базовая" эффективность видится одинаковой. Соответственно при выборе структуры на практике необходимо идти от требований и ограничений системы (обычная заполненность/незаполненность дерева, использование кэша).

# 5. Строим сбалансированные двоичные деревья поиска
# 5.3.* Реализуйте метод удаления узла из двоичного дерева, заданного в виде массива.
# Сложность по времени: O(n*logn) из-за использования сортировки при пересоздании дерева (в худшем в принципе даже может O(n^2)); память - O(n) для регенерации (балансировки)

class aBST:

    def __init__(self, depth):
        tree_size: int = (2 ** (depth + 1)) - 1
        self.Tree: list = [None] * tree_size

    # Сам метод удаления
    def delete_key(self, key: int) -> bool:
        if self.Tree[0] == None:
            return False
        index: int = self.FindKeyIndex(key)
        if index is None or index < 0:
            return False
        self.Tree[index] = None
        arr: list = self.BFS()
        self.GenerateBBSTArray(arr)
        return True

    def BFS(self) -> list:
        nodes: list[int] = []
        self.clean_BFS_traversal(lambda val: nodes.append(val))
        return nodes

    def clean_BFS_traversal(self, processor) -> None:
        if self.Tree[0] is None:
            return
        for i in range(0, len(self.Tree)):
            if self.Tree[i] is not None:
                processor(self.Tree[i])

    def GenerateBBSTArray(self, arr: list):
        arr.sort()
        result_tree: list = [None] * len(self.Tree)
        self.Tree = self.process_sub_tree_no_side_effect(arr, result_tree, 0, 0, len(arr) - 1)

    def process_sub_tree_no_side_effect(self, arr: list, tree: list, root_ind: int, start: int, end: int) -> list:
        new_tree: list = tree.copy()
        if root_ind >= len(arr):
            return new_tree
        if start > end:
            return new_tree
        middle_index: int = int((start + end) / 2)
        new_tree[root_ind] = arr[middle_index]
        new_tree = self.process_sub_tree_no_side_effect(arr, new_tree, root_ind * 2 + 1, start, middle_index - 1)
        new_tree = self.process_sub_tree_no_side_effect(arr, new_tree, root_ind * 2 + 2, middle_index + 1, end)
        return new_tree

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

# 5. Строим сбалансированные двоичные деревья поиска
# 5.4.* Подумайте, как ответить на вопрос с картинки (Sort B-tree in O(1) time).
# По сути B-tree это дерево с уже упорядоченными (отсортированными) элементами. Оно само поддерживает упорядоченность при операциях вставки/удаления, так что можно сказать,
# что метод sort (если вдруг таковой будет в классе) для B tree отрабатывает всегда за O(1). Собственно он ничего не будет делать.


# Рефлексия 5.3.* Реализуйте метод удаления узла из двоичного дерева, заданного в виде массива.
# В данном решении использовал метод регенерации дерева, реализованный ранее в данном задании. Использован для перебалансировки дерева после удаления узла.
# Подумал, что если использовать стандартный алгоритм удаления узла (из второго задания) с обработкой наследников правого потомка, то получим сложность по времени - поиск узла O(log n), сама замена O(h).
# Пространство - O(h) - глубина рекурсии для "подтягивания" потомков. Но здесь не будет перебалансировки дерева, поэтому оставил первый вариант реализации.

# Рефлексия 5.4.* Подумайте, как ответить на вопрос с картинки (Sort B-tree in O(1) time).
# Ну тут особой рефлексии наверное не будет - собственно ответ следует из определения данного дерева.