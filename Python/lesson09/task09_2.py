class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val
        self.Parent = parent
        self.Children = []
        self.level = None


class SimpleTree:

    def __init__(self, root):
        self.Root = root
        self.Root.level = 0

    # 9. Чётные деревья и леса
    # 9.2.* Добавьте метод, который сбалансирует чётное двоичное дерево.
    # Сложность: время O(n); пространство O(n)
    # рефлексия по 9.2.
    # В конечном итоге остановился на простом в реализации варианте пересоздания дерева из массива узлов, т.к. уже есть метод получения всех узлов дерева.
    # Для проверки результата сделал метод получения всех листьев и использовал добавленное поле level в классе SimpleTree.
    # Но кроме этого некоторое время обдумывал такой вариант: получаем все листья (у нас дерево, в котором у всех узлов проставлены уровни).
    # Далее сортирую список по уровню и, если разница между наименьшим уровнем листа и наибольшим больше 1, беру узлы с самым большим уровнем
    # и переношу их к листу на самом маленьком уровне. Но этот момент с последующим пересчетом уровня и отслеживанием новых листов показался мне излишним усложнением задачи
    # и я вернулся к варианту с простой реализацией пересоздания дерева.
    def balance_tree(self) -> None:
        if self.Root is None:
            return
        nodes: list[SimpleTreeNode] = self.GetAllNodes()
        self.Root = self._generate_sub_tree(nodes, None, 0, len(nodes) -1)

    def _generate_sub_tree(self, nodes: list[SimpleTreeNode], parent: SimpleTreeNode | None, start: int, end: int) -> SimpleTreeNode | None:
        if start >= len(nodes) or end < 0 or end >= len(nodes) or end < start:
            return None
        middle_index: int = int((start + end) / 2)
        cur_parent: SimpleTreeNode = SimpleTreeNode(nodes[middle_index].NodeValue, parent)
        self.AddChild(parent, cur_parent)
        self._generate_sub_tree(nodes, cur_parent, start, middle_index - 1)
        self._generate_sub_tree(nodes, cur_parent, middle_index + 1, end)
        return cur_parent

    # 9. Чётные деревья и леса
    # 9.3.* Добавьте метод, который для любого заданного подузла текущего дерева определит общее количество чётных поддеревьев.
    # Сложность: время O(n); пространство O(h) где h высота дерева
    # рефлексия по 9.3.
    # В качестве решения я взял созданный ранее в первом занятии метод count_child, который применяю поочередно ко всем потомкам указанного узла
    # и далее рекурсивно к их потомкам. Если количество узлов четной, увеличиваю счетчик.
    def get_even_trees_count(self, node: SimpleTreeNode) -> int:
        if len(node.Children) == 0:
            return 0
        even_trees: int = 0
        for child in node.Children:
            child_count: int = self.count_child(child)
            if child_count % 2 == 0:
                even_trees += 1
            even_trees += self.get_even_trees_count(child)
        return even_trees

    def get_leaves(self, node: SimpleTreeNode, leaves: list[SimpleTreeNode]) -> list[SimpleTreeNode]:
        inner_leaves: list[SimpleTreeNode] = leaves.copy()
        if len(node.Children) == 0:
            inner_leaves.append(node)
            return inner_leaves
        for child in node.Children:
            inner_leaves = self.get_leaves(child, inner_leaves)
        return inner_leaves

    def AddChild(self, ParentNode: SimpleTreeNode, NewChild: SimpleTreeNode) -> None:
        if ParentNode is None:
            self.Root = NewChild
            NewChild.level = 0
            return
        NewChild.Parent = ParentNode
        NewChild.level = ParentNode.level + 1
        ParentNode.Children.append(NewChild)

    def DeleteNode(self, NodeToDelete):
        if self.Root == NodeToDelete:
            self.Root = None
            return
        NodeToDelete.Parent.Children.remove(NodeToDelete)
        NodeToDelete.Parent = None

    def GetAllNodes(self):
        if self.Root is None:
            return []
        nodes = []
        nodes.append(self.get_child(self.Root, nodes))
        return nodes

    def get_child(self, NodeToGet, nodes):
        if len(NodeToGet.Children) == 0:
            return NodeToGet
        for child in NodeToGet.Children:
            nodes.append(self.get_child(child, nodes))
        return NodeToGet

    def FindNodesByValue(self, val):
        if self.Root is None:
            return []
        result_list = []
        self.find_in_child(self.Root, val, result_list)
        return result_list

    def find_in_child(self, node, val, result_list):
        if node.NodeValue == val:
            result_list.append(node)
        if len(node.Children) == 0:
            return
        for child in node.Children:
            self.find_in_child(child, val, result_list)

    def MoveNode(self, OriginalNode, NewParent):
        self.DeleteNode(OriginalNode)
        self.AddChild(NewParent, OriginalNode)

    def Count(self):
        if self.Root is None:
            return 0
        return self.count_child(self.Root)

    def count_child(self, node, mode = 'all'):
        if len(node.Children) == 0:
            return 1
        cnt = 0
        if mode == 'all':
            cnt = 1
        for child in node.Children:
            cnt += self.count_child(child, mode)
        return cnt

    def LeafCount(self):
        if self.Root is None:
            return 0
        return self.count_child(self.Root, 'leaf')

    def EvenTrees(self):
        if self.Root is None or self.Count() % 2 != 0:
            return []
        result_list: list[SimpleTreeNode] = []
        self.is_sub_tree_even(self.Root, result_list)
        return result_list

    def is_sub_tree_even(self, node: SimpleTreeNode, nodes: list[SimpleTreeNode]) -> None:
        for child in node.Children:
            children_count: int = self.count_child(child)
            if children_count % 2 == 0:
                nodes.append(node)
                nodes.append(child)
            self.is_sub_tree_even(child, nodes)

    # Рефлексия по эталонным решениям для занятия 7. Пирамиды
    # для 7.4.* Добавьте метод поиска максимального элемента в заданном диапазоне значений.
    # Тут я конечно догадался, что надо просмотреть всю кучу (кроме частного случая когда корень уже меньше нижней границы диапазона),
    # но вот что можно было просто искать прямо по массиву как-то и не подумал.

    # для 7.5* Подумайте над эффективным алгоритмом поиска в куче элемента по заданному условию (например, меньше заданного значения).
    # Здесь в своих рассуждениях не совсем в ту степь двинулся. Не отметил главный вариант с "отсечением" ветвей с неудовлетворяющим условию корнем.

    # для 7.6.* Добавьте метод объединения текущей кучи с кучей-параметром.
    # Подход выбран в целом верный. Кучу-параметр я копирую, но кроме этого решил пойти еще дальше - сделал метод,
    # который и текущую кучу копирует. Т.е. в результат я не меняю ни кучу-парамер, ни текущую, создавая новый объект.