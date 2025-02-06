import java.util.*;

class BSTNode
{
    public int NodeKey;
    public BSTNode Parent;
    public BSTNode LeftChild;
    public BSTNode RightChild;
    public int     Level;

    public BSTNode(int key, BSTNode parent)
    {
        NodeKey = key;
        Parent = parent;
        LeftChild = null;
        RightChild = null;
    }
}

class BalancedBST
{
    public BSTNode Root;

    public BalancedBST()
    {
        Root = null;
    }

    public void GenerateTree(int[] a)
    {
        Arrays.sort(a);
        Root = generateChildren(a, null, 0, a.length - 1, 0);
    }

    private BSTNode generateChildren(int[] a, BSTNode parent, int start, int end, int level) {
        if (start > end) return null;
        int midInd = (start + end) / 2;
        BSTNode node = new BSTNode(a[midInd], parent);
        node.Level = level;
        node.LeftChild = generateChildren(a, node, start, midInd - 1, level + 1);
        node.RightChild = generateChildren(a, node, midInd + 1, end, level + 1);
        return node;
    }

    public boolean IsBalanced(BSTNode root_node)
    {
        return checkTreeDepth(root_node) != -1;
    }

    private int checkTreeDepth(BSTNode node) {
        if (node == null) return 0;
        int left = checkTreeDepth(node.LeftChild);
        if (left == -1) return -1;
        int right = checkTreeDepth(node.RightChild);
        if (right == -1) return -1;
        if (Math.abs(left - right) > 1) return -1;
        return Math.max(left, right) + 1;
    }
}



