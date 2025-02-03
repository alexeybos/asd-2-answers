import java.util.*;

class aBST
{
    public Integer Tree [];

    public aBST(int depth)
    {
        int tree_size = (int) Math.pow(2, depth + 1) - 1;
        Tree = new Integer[ tree_size ];
        for(int i=0; i<tree_size; i++) Tree[i] = null;
    }

    public Integer FindKeyIndex(int key)
    {
        return findKeyIndex(key, 0);
    }

    private Integer findKeyIndex(int key, int currentNode) {
        if (currentNode > Tree.length - 1) return null;
        if (Tree[currentNode] == null) return -currentNode;
        if (Tree[currentNode] == key) return currentNode;
        if (Tree[currentNode] > key) return findKeyIndex(key, 2 * currentNode + 1);
        return findKeyIndex(key, 2 * currentNode + 2);
    }

    public int AddKey(int key)
    {
        Integer indexToAdd = FindKeyIndex(key);
        if (indexToAdd == null) return -1;
        indexToAdd = Math.abs(indexToAdd);
        Tree[indexToAdd] = key;
        return indexToAdd;
    }
}



