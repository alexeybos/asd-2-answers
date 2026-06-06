from task08 import Vertex

# 8. Графы
# 8.2.* Реализуйте направленный граф, представленный матрицей смежности, и добавьте метод проверки, будет ли он циклическим.
# сложность (для метода is_cyclic): время O(n**2), т.к. в худшем случае просматриваем всю матрицу смежности. Память O(n) - массив для хранения посещенных вершин
class DirectedGraph:

    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size

    def AddVertex(self, v):
        for i in range(0, self.max_vertex):
            if self.vertex[i] is None:
                self.vertex[i] = Vertex(v)
                return

    def RemoveVertex(self, v):
        self.vertex[v] = None
        for i in range(0, self.max_vertex):
            self.m_adjacency[i][v] = 0
            self.m_adjacency[v][i] = 0

    def IsEdge(self, v1, v2):
        return self.m_adjacency[v1][v2] == 1

    def AddEdge(self, v1, v2):
        self.m_adjacency[v1][v2] = 1

    def RemoveEdge(self, v1, v2):
        self.m_adjacency[v1][v2] = 0

    def is_cyclic(self) -> bool:
        for i in range(0, self.max_vertex):
            if self.vertex[i] is not None:
                visited: list = [0] * self.max_vertex
                return self._path_to_depth(visited, i)
        return False

    def _path_to_depth(self, visited: list, v1: int) -> bool:
        visited[v1] = 1
        for i in range(0, self.max_vertex):
            if self.m_adjacency[v1][i] == 1:
                if visited[i] == 1:
                    return True
                visited[i] = 1
                if self._path_to_depth(visited, i):
                    return True
        return False

    # Рефлексия по задаче 8.2.* Реализуйте направленный граф, представленный матрицей смежности, и добавьте метод проверки, будет ли он циклическим.
    # Ну по основным методам для ориентированного графа все просто - при добавлении/удалении ребра работаем четко с указанным "направлением" v1->v2,
    # т.е. в матрице смежности меняем значение только [v1][v2], а "обратное" [v2][v1] уже не трогаем, пока в вызове нам явно не укажут данное направление.
    # По методу проверки циклов реализованная идея следующая: берем очередную вершину и рекурсивно "бежим" от нее по матрице смежности.
    # В процессе передвижения помечаем каждую посещенную вершину в дополнительном массиве вершин. Если в процессе передвижения мы натыкаемся на уже посещенную вершину,
    # значит мы в нее откуда-то вернулись, а значит в графе есть цикл.

    # Рефлексия по эталонным решениям для занятия 6. Строим сбалансированные двоичные деревья поиска (2)
    # для 6.2.* Добавьте метод проверки, действительно ли дерево получилось правильным.
    # Реализация соответствует рекомендованной, но это и неудивительно, ведь соответствующая подсказка дана в самом заданиии.

    # для 6.3.* Добавьте метод проверки, действительно ли дерево получилось сбалансированным
    # Здесь также, насколько я могу судить, сделано аналогично эталонному решению - рекурсивное сравнение высот левых и правых поддеревьев