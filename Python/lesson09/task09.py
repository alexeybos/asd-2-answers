
class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val
        self.Parent = parent
        self.Children = []


class SimpleTree:

    def __init__(self, root):
        self.Root = root

    def AddChild(self, ParentNode, NewChild):
        if ParentNode is None:
            self.Root = NewChild
            return
        NewChild.Parent = ParentNode
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




