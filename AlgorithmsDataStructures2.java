import java.util.*;

public class AlgorithmsDataStructures2
{
    public static int[] GenerateBBSTArray(int[] a)
    {
        Arrays.sort(a);
        int[] resultTree = new int[a.length];
        generateSubTree(a, resultTree, 0, 0, a.length - 1);
        return resultTree;
    }

    private static void generateSubTree(int[] a, int[] resultTree, int rootInd, int start, int end) {
        if (rootInd >= a.length) return;
        if (start > end) return;
        int midInd = (start + end) / 2;
        resultTree[rootInd] = a[midInd];
        generateSubTree(a, resultTree, rootInd * 2 + 1, start, midInd - 1);
        generateSubTree(a, resultTree, rootInd * 2 + 2, midInd + 1, end);
    }
}




