import java.util.*;

class Heap
{
    public int [] HeapArray;
    private int lastInHeap;

    public Heap() {
        HeapArray = null;
        lastInHeap = -1;
    }

    public void MakeHeap(int[] a, int depth)
    {
        int heapSize = (int) Math.pow(2, depth + 1) - 1;
        HeapArray = new int[heapSize];
        for (int key : a) {
            Add(key);
        }
    }

    public int GetMax()
    {
        if (lastInHeap == -1) return -1;
        int max = HeapArray[0];
        HeapArray[0] = HeapArray[lastInHeap];
        HeapArray[lastInHeap] = 0;
        lastInHeap--;
        checkChildren(0);
        return max;
    }

    private void checkChildren(int i) {
        int childIndex = (2 * i + 1);
        if (childIndex <= lastInHeap && HeapArray[childIndex] > HeapArray[i]) {
            swap(childIndex, i);
            checkChildren(childIndex);
        }
        childIndex++;
        if (childIndex <= lastInHeap && HeapArray[childIndex] > HeapArray[i]) {
            swap(childIndex, i);
            checkChildren(childIndex);
        }
    }

    public boolean Add(int key)
    {
        if (lastInHeap + 1 == HeapArray.length) return false;
        lastInHeap++;
        HeapArray[lastInHeap] = key;
        for (int i = lastInHeap; i > 0; i = (i - 1) / 2) {
            int parentIndex = (i - 1) / 2;
            if (HeapArray[parentIndex] < HeapArray[i]) {
                swap(parentIndex, i);
            } else {
                int childIndex = (2 * i + 1);
                if (childIndex <= lastInHeap && HeapArray[childIndex] > key) {
                    swap(childIndex, i);
                    return true;
                }
                childIndex++;
                if (childIndex <= lastInHeap && HeapArray[childIndex] > key) {
                    swap(childIndex, i);
                    return true;
                }
                return true;
            }
        }
        return true;
    }

    private void swap(int index1, int index2) {
        int tmpForSwap = HeapArray[index2];
        HeapArray[index2] = HeapArray[index1];
        HeapArray[index1] = tmpForSwap;
    }
}



