class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val
        self.Parent = parent
        self.Children = []
        self.level = None

class SimpleTree:

    def __init__(self, root):
        self.Root = root

    # 1. Деревья
    # 1.1 Напишите метод, который перебирает всё дерево и прописывает каждому узлу его уровень.
    # сложность O(n) - time, пространственная сложность по стеку вызовов: О(h) - высота дерева (в худшем случае так же O(n))
    #
    def add_levels(self):
        if self.Root is None:
            return
        self.Root.level = 1
        self.add_children_level(self.Root.Children)

    def add_children_level(self, nodes):
        if len(nodes) == 0:
            return
        for node in nodes:
            node.level = node.Parent.level + 1
            self.add_children_level(node.Children)

    # 1.2. Придумайте, как лучше организовать поддержку уровня узлов без анализа всего дерева.
    # Поле level в классе. Метод AddChild: новому узлу прописывается level+1.
    # Метод MoveNode: тут надо будет обновить level у всего переносимого поддерева согласно mewParent.level + 1



