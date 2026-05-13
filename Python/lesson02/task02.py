
class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey = key
        self.NodeValue = val
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None


class BSTFind:

    def __init__(self):
        self.Node = None
        self.NodeHasKey = False
        self.ToLeft = False


class BST:

    def __init__(self, node):
        self.Root = node
        self.cnt = 0
        if node is not None:
            self.cnt = 1

    def FindNodeByKey(self, key):
        if self.Root is None:
            return BSTFind()
        return self.find_in_child(self.Root, key)

    def find_in_child(self, node, key):
        if node.NodeKey == key:
            result = BSTFind()
            result.Node = node
            result.NodeHasKey = True
            return result
        if node.NodeKey > key and node.LeftChild is not None:
            return self.find_in_child(node.LeftChild, key)
        if node.NodeKey < key and node.RightChild is not None:
            return self.find_in_child(node.RightChild, key)
        result = BSTFind()
        result.Node = node
        result.NodeHasKey = False
        result.ToLeft = node.NodeKey > key
        return result

    def AddKeyValue(self, key, val):
        find_result = self.FindNodeByKey(key)
        if find_result.NodeHasKey:
            return False
        self.cnt += 1
        if self.Root is None:
            self.Root = BSTNode(key, val, None)
            return True
        new_node = BSTNode(key, val, find_result.Node)
        if find_result.ToLeft:
            find_result.Node.LeftChild = new_node
            return True
        find_result.Node.RightChild = new_node
        return True

    def FinMinMax(self, FromNode, FindMax):
        if FromNode is None:
            return None
        return self.find_min_max_in_child(FromNode, FindMax)

    def find_min_max_in_child(self, node, find_max):
        next_node = node.LeftChild
        if find_max:
            next_node = node.RightChild
        if next_node is None:
            return node
        return self.find_min_max_in_child(next_node, find_max)

    def DeleteNodeByKey(self, key):
        delete_find_res = self.FindNodeByKey(key)
        if not delete_find_res.NodeHasKey:
            return False
        self.cnt -= 1
        del_node = delete_find_res.Node
        if self.cnt == 0:
            self.Root = None
            return True
        if del_node.RightChild is None and del_node.LeftChild is None:
            self.replace_in_parent(del_node, None)
            return True
        if del_node.RightChild is None:
            del_node.LeftChild.parent = del_node.Parent
            self.replace_in_parent(del_node, del_node.LeftChild)
            return True
        if del_node.LeftChild is None:
            del_node.RightChild.parent = del_node.Parent
            self.replace_in_parent(del_node, del_node.RightChild)
            return True
        node_in_deep = del_node.RightChild
        while node_in_deep.LeftChild is not None:
            node_in_deep = node_in_deep.LeftChild

        if node_in_deep.RightChild is not None:
            del_node.NodeValue = node_in_deep.NodeValue
            del_node.NodeKey = node_in_deep.NodeKey
            node_in_deep.NodeKey = node_in_deep.RightChild.NodeKey
            node_in_deep.NodeValue = node_in_deep.RightChild.NodeValue
            node_in_deep.RightChild = None
            return True
        del_node.NodeValue = node_in_deep.NodeValue
        del_node.NodeKey = node_in_deep.NodeKey
        self.replace_in_parent(node_in_deep, None)
        return True

    def replace_in_parent(self, node, new_child):
        if node.Parent.LeftChild == node:
            node.Parent.LeftChild = new_child
            return
        node.Parent.RightChild = new_child

    def Count(self):
        return self.cnt



    