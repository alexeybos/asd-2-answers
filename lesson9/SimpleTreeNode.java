import java.util.*;

public class SimpleTreeNode<T>
{
    public T NodeValue;
    public SimpleTreeNode<T> Parent;
    public List<SimpleTreeNode<T>> Children;
    public int level;

    public SimpleTreeNode(T val, SimpleTreeNode<T> parent)
    {
        NodeValue = val;
        Parent = parent;
        Children = null;
        level = 0;
    }
}

class SimpleTree<T>
{
    public SimpleTreeNode<T> Root;

    public SimpleTree(SimpleTreeNode<T> root)
    {
        Root = root;
    }

    public void AddChild(SimpleTreeNode<T> ParentNode, SimpleTreeNode<T> NewChild)
    {
        if (ParentNode == null && Root == null) {
            Root = NewChild;
        }
        if (ParentNode != null) {
            NewChild.Parent = ParentNode;
            if (ParentNode.Children == null) ParentNode.Children = new ArrayList<>();
            ParentNode.Children.add(NewChild);
        }
    }

    public void DeleteNode(SimpleTreeNode<T> NodeToDelete)
    {
        NodeToDelete.Parent.Children.remove(NodeToDelete);
        if (NodeToDelete.Parent.Children.isEmpty()) {
            NodeToDelete.Parent.Children = null;
        }
        NodeToDelete.Parent = null;

    }

    public ArrayList<SimpleTreeNode<T>> GetAllNodes()
    {
        if (Root == null) return null;
        ArrayList<SimpleTreeNode<T>> allNodesList = new ArrayList<>();
        getChildren(Root, allNodesList);
        return allNodesList;
    }

    private void getChildren(SimpleTreeNode<T> node, List<SimpleTreeNode<T>> nodesList) {
        nodesList.add(node);
        if (node.Children == null) return;
        for (SimpleTreeNode<T> child: node.Children) {
            getChildren(child, nodesList);
        }
    }

    public List<SimpleTreeNode<T>> FindNodesByValue(T val)
    {
        if (Root == null) return null;
        List<SimpleTreeNode<T>> nodesFound = new ArrayList<>();
        findInChildren(Root, nodesFound, val);
        return nodesFound;
    }

    private void findInChildren(SimpleTreeNode<T> node, List<SimpleTreeNode<T>> foundNodes, T val) {
        if (node.NodeValue == val) foundNodes.add(node);
        if (node.Children == null) return;
        for (SimpleTreeNode<T> child: node.Children) {
            findInChildren(child, foundNodes, val);
        }
    }

    public void MoveNode(SimpleTreeNode<T> OriginalNode, SimpleTreeNode<T> NewParent)
    {
        DeleteNode(OriginalNode);
        AddChild(NewParent, OriginalNode);
    }

    public int Count()
    {
        return leafOrNodeCount(Root, 1);
    }

    public int LeafCount()
    {
        return leafOrNodeCount(Root, 0);
    }

    private int leafOrNodeCount(SimpleTreeNode<T> node, int startCountFrom) {
        if (node == null) return 0;
        if (node.Children == null) return 1;
        int cnt = startCountFrom;
        for (int i = 0; i < node.Children.size(); i++) {
            cnt += leafOrNodeCount(node.Children.get(i), startCountFrom);
        }
        return cnt;
    }

    public void setLevels() {
        if (this.Root == null) return;
        setChildrenLevels(this.Root, 0);
    }

    private void setChildrenLevels(SimpleTreeNode<T> node, int curLevel) {
        node.level = curLevel;
        if (node.Children == null) return;
        for (int i = 0; i < node.Children.size(); i++) {
            setChildrenLevels(node.Children.get(i), curLevel + 1);
        }
    }

    public ArrayList<T> EvenTrees()
    {
        ArrayList<T> toDelete = new ArrayList<>();
        findEvenSubTreesByChildrenCnt(Root, toDelete);
        return toDelete;
    }

    private int findEvenSubTreesByChildrenCnt(SimpleTreeNode<T> root, ArrayList<T> cutPositions) {
        if (root.Children == null) return 1;
        int childrenCnt = 0;
        for (int i = 0; i < root.Children.size(); i++) {
            int chCnt = findEvenSubTreesByChildrenCnt(root.Children.get(i), cutPositions);
            if (chCnt != 0 && chCnt % 2 == 0) cutPositions.addAll(Arrays.asList(root.NodeValue, root.Children.get(i).NodeValue));
            childrenCnt += chCnt;
        }
        childrenCnt++;
        return childrenCnt;
    }
}




