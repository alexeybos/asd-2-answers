import java.util.*;

class Vertex
{
    public int Value;
    public boolean Hit;
    public Vertex(int val)
    {
        Value = val;
        Hit = false;
    }
}

class SimpleGraph
{
    Vertex [] vertex;
    int [][] m_adjacency;
    int max_vertex;

    public SimpleGraph(int size)
    {
        max_vertex = size;
        m_adjacency = new int [size][size];
        vertex = new Vertex[size];
    }

    public void AddVertex(int value)
    {
        int emptySlot = 0;
        for (; vertex[emptySlot] != null; emptySlot++) {
        }
        vertex[emptySlot] = new Vertex(value);
    }

    public void RemoveVertex(int v)
    {
        vertex[v] = null;
        for (int i = 0; i < max_vertex; i++) {
            m_adjacency[v][i] = 0;
            m_adjacency[i][v] = 0;
        }
    }

    public boolean IsEdge(int v1, int v2)
    {
        return m_adjacency[v1][v2] == 1;
    }

    public void AddEdge(int v1, int v2)
    {
        m_adjacency[v1][v2] = 1;
        m_adjacency[v2][v1] = 1;
    }

    public void RemoveEdge(int v1, int v2)
    {
        m_adjacency[v1][v2] = 0;
        m_adjacency[v2][v1] = 0;
    }

    public ArrayList<Vertex> DepthFirstSearch(int VFrom, int VTo)
    {
        int vCnt = markVertexUnHitAndCount();
        if (vCnt == 0 || vertex[VFrom] == null || vertex[VTo] == null) return new ArrayList<>();

        Stack<Vertex> path = new Stack<>();
        dfsFromVertex(VFrom, path, VTo);
        return new ArrayList<>(path);
    }

    private boolean dfsFromVertex(Integer vInd, Stack<Vertex> savedPath, int VTo) {
        if (vertex[vInd] == null || vertex[vInd].Hit) return false;
        vertex[vInd].Hit = true;
        savedPath.push(vertex[vInd]);
        if (m_adjacency[vInd][VTo] == 1) {
            savedPath.push(vertex[VTo]);
            return true;
        }
        for (int i = 0; i < vertex.length; i++) {
            boolean endProcess = false;
            if (m_adjacency[vInd][i] == 1 && !vertex[i].Hit) endProcess = dfsFromVertex(i, savedPath, VTo);
            if (endProcess) return true;
        }
        savedPath.pop();
        return false;
    }

    private int markVertexUnHitAndCount() {
        int vCnt = 0;
        for (Vertex value : vertex) {
            if (value != null) {
                vCnt++;
                value.Hit = false;
            }
        }
        return vCnt;
    }

    public ArrayList<Vertex> BreadthFirstSearch(int VFrom, int VTo)
    {
        int vCnt = markVertexUnHitAndCount();
        if (vCnt == 0 || vertex[VFrom] == null || vertex[VTo] == null) return new ArrayList<>();
        int[] pathByParents = bfsFromVertex(VFrom, VTo);
        return makeResultPath(pathByParents, VTo);
    }

    private int[] bfsFromVertex(Integer VFrom, int VTo) {
        Queue<Integer> vertexesQ = new LinkedList<>();
        int[] lastParents = new int[max_vertex];
        Arrays.fill(lastParents, -1);
        vertexesQ.add(VFrom);
        for (; !vertexesQ.isEmpty();) {
            int vInd = vertexesQ.remove();
            if (m_adjacency[vInd][VTo] == 1) {
                lastParents[VTo] = vInd;
                return lastParents;
            }
            vertex[vInd].Hit = true;
            for (int i = 0; i < vertex.length; i++) {
                if (m_adjacency[vInd][i] == 1 && !vertex[i].Hit) {
                    vertex[i].Hit = true;
                    vertexesQ.add(i);
                    lastParents[i] = vInd;
                }
            }
        }
        return null;
    }

    private ArrayList<Vertex> makeResultPath(int[] pathByParents, int VTo) {
        ArrayList<Vertex> result = new ArrayList<>();
        if (pathByParents == null) return result;
        result.add(vertex[VTo]);
        for (int i = VTo; pathByParents[i] != -1; i = pathByParents[i]) {
            result.add(vertex[pathByParents[i]]);
        }
        return new ArrayList<>(result.reversed());
    }
}
