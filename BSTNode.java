
import java.io.*;
import java.util.*;

class BSTNode<T>
{
    public int NodeKey;
    public T NodeValue;
    public BSTNode<T> Parent;
    public BSTNode<T> LeftChild;
    public BSTNode<T> RightChild;

    public BSTNode(int key, T val, BSTNode<T> parent)
    {
        NodeKey = key;
        NodeValue = val;
        Parent = parent;
        LeftChild = null;
        RightChild = null;
    }
}

class BSTFind<T>
{
    public BSTNode<T> Node;
    public boolean NodeHasKey;
    public boolean ToLeft;

    public BSTFind() { Node = null; }

    public BSTFind(BSTNode<T> node, boolean nodeHasKey, boolean toLeft) {
        Node = node;
        NodeHasKey = nodeHasKey;
        ToLeft = toLeft;
    }
}

class BST<T>
{
    BSTNode<T> Root;

    public BST(BSTNode<T> node)
    {
        Root = node;
    }

    public BSTFind<T> FindNodeByKey(int key)
    {
        if (Root == null) return new BSTFind<>(null, false, false);
        return FindNodeByKey(key, Root, Root, false);
    }

    private BSTFind<T> FindNodeByKey(int key, BSTNode<T> node, BSTNode<T> prevNode, boolean toLeft) {
        if (node == null) return new BSTFind<>(prevNode, false, toLeft);
        BSTFind<T> foundNode;
        if (node.NodeKey == key) {
            return new BSTFind<>(node, true, false);
        }
        if (node.NodeKey > key) {
            foundNode = FindNodeByKey(key, node.LeftChild, node, true);
        } else {
            foundNode = FindNodeByKey(key, node.RightChild, node, false);
        }
        return foundNode;
    }

    public boolean AddKeyValue(int key, T val)
    {
        BSTFind<T> nodeToAdd = FindNodeByKey(key);
        if (nodeToAdd.NodeHasKey) return false;
        if (nodeToAdd.ToLeft) {
            nodeToAdd.Node.LeftChild = new BSTNode<>(key, val, nodeToAdd.Node);
        } else {
            nodeToAdd.Node.RightChild = new BSTNode<>(key, val, nodeToAdd.Node);
        }
        return true;
    }

    public BSTNode<T> FinMinMax(BSTNode<T> FromNode, boolean FindMax)
    {
        if (Root == null) return null;
        if (FindMax) return findMax(FromNode);
        return findMin(FromNode);
    }

    private BSTNode<T> findMax(BSTNode<T> node) {
        if (node.RightChild == null) return node;
        return findMax(node.RightChild);
    }

    private BSTNode<T> findMin(BSTNode<T> node) {
        if (node.LeftChild == null) return node;
        return findMin(node.LeftChild);
    }

    public boolean DeleteNodeByKey(int key)
    {
        BSTFind<T> foundNode = FindNodeByKey(key);
        if (!foundNode.NodeHasKey) return false;
        BSTNode<T> node = foundNode.Node;
        if (node == Root) {
            Root = null;
            return true;
        }

        if (node.RightChild == null && node.LeftChild == null) {
            replaceLinkInParent(node, null);
            return true;
        }

        if (node.RightChild == null) {
            node.LeftChild.Parent = node.Parent;
            replaceLinkInParent(node, node.LeftChild);
            return true;
        }

        if (node.LeftChild == null) {
            node.RightChild.Parent = node.Parent;
            replaceLinkInParent(node, node.RightChild);
            return true;
        }

        BSTNode<T> deepNode = node.RightChild;
        for (; deepNode.LeftChild != null;) {
            deepNode = deepNode.LeftChild;
        }

        if (deepNode.RightChild != null) {
            node.NodeValue = deepNode.NodeValue;
            node.NodeKey = deepNode.NodeKey;
            deepNode.NodeKey = deepNode.RightChild.NodeKey;
            deepNode.NodeValue = deepNode.RightChild.NodeValue;
            deepNode.RightChild = null;
            return true;
        }
        node.NodeValue = deepNode.NodeValue;
        node.NodeKey = deepNode.NodeKey;
        replaceLinkInParent(deepNode, null);
        return true;
    }

    private void replaceLinkInParent(BSTNode<T> child, BSTNode<T> newChild) {
        if (child.Parent.LeftChild == child) {
            child.Parent.LeftChild = newChild;
            return;
        }
        child.Parent.RightChild = newChild;
    }

    public int Count()
    {
        return childrenCount(Root);
    }

    private int childrenCount(BSTNode<T> node) {
        if (node == null) return 0;
        return 1 + childrenCount(node.LeftChild) + childrenCount(node.RightChild);
    }
}



