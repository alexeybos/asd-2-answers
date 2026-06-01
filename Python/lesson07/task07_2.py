
class Heap:

    def __init__(self):
        self.HeapArray = []  # хранит неотрицательные числа-ключи

    # 7. Пирамиды
    # 7.3 Добавьте метод проверки, что массив действительно содержит корректную кучу.
    # Сложность по времени: O(n); память - O(h) глубина кучи
    def is_correct(self) -> bool:
        if self.HeapArray[0] is None or len(self.HeapArray) == 1 or self.HeapArray[1] is None:
            return True
        return self._is_children_correct(0)

    def _is_children_correct(self, parent: int) -> bool:
        if parent >= len(self.HeapArray):
            return True
        left: int = 2 * parent + 1
        right: int = left + 1
        if self._is_child_greater(left, self.HeapArray[parent]) or self._is_child_greater(right,
                                                                                          self.HeapArray[parent]):
            return False
        if self._is_children_correct(left):
            return self._is_children_correct(right)
        return False

    def _is_child_greater(self, child: int, key: int) -> bool:
        if child >= len(self.HeapArray) or self.HeapArray[child] is None:
            return False
        return self.HeapArray[child] > key

    # 7. Пирамиды
    # 7.4.* Добавьте метод поиска максимального элемента в заданном диапазоне значений.
    # Сложность по времени: O(n); память - O(h) глубина кучи
    def find_max_in_range(self, start: int, stop: int) -> int | None:
        if self.HeapArray[0] is None or self.HeapArray[0] < start:
            return None
        cur_max: int = self._find_max_in_children(0, start, stop, self.HeapArray[0])
        if cur_max in range(start, stop + 1):
            return cur_max
        return None

    def _find_max_in_children(self, parent: int, start: int, stop: int, cur_max: int) -> int:
        if parent >= len(self.HeapArray) or self.HeapArray[parent] is None or self.HeapArray[parent] < start:
            return cur_max
        internal_max: int = self.HeapArray[parent]
        if internal_max in range(start, stop + 1):
            return internal_max
        left_max: int = self._find_max_in_children((2 * parent) + 1, start, stop, internal_max)
        right_max: int = self._find_max_in_children((2 * parent) + 2, start, stop, internal_max)
        if left_max in range(start, stop + 1) and right_max in range(start, stop + 1):
            return max(left_max, right_max)
        if left_max in range(start, stop + 1) and right_max not in range(start, stop + 1):
            return left_max
        return right_max

    # 7. Пирамиды
    # 7.5* Подумайте над эффективным алгоритмом поиска в куче элемента по заданному условию (например, меньше заданного значения).
    # Основных свойств у кучи два: потомки всегда меньше родителя (рассматриваем max-heap), куча является сбалансированной, т.к. уровень заполняется слева-направо.
    # Исходя из этого, максимальная оптимизация, которая приходит мне на ум - это возможно обрабатывать кучу поуровнево (начиная, например, со среднего уровня) и,
    # в зависимости от условия поиска, далее переходить вверх-вниз по принципам бинарного поиска.
    # Также, при условии, что нам хорошо известны входные данные, можно, например, прекращать поиск, когда мы знаем, что значения в куче сильно больше искомого значения.

    # 7. Пирамиды
    # 7.6.* Добавьте метод объединения текущей кучи с кучей-параметром.
    # Сложность по времени: O(n); память - O(n)
    def union(self, heap: 'Heap') -> 'Heap':
        result_heap: 'Heap' = self.copy()
        second_heap: 'Heap' = heap.copy()
        next_value: int = second_heap.GetMax()
        while next_value > 0:
            result_heap.Add(next_value)
            next_value = second_heap.GetMax()
        assert self.is_correct()
        return result_heap

    def copy(self) -> 'Heap':
        new_heap = Heap()
        new_heap.HeapArray = self.HeapArray.copy()
        return new_heap

    def MakeHeap(self, a, depth):
        self.HeapArray = [None] * ((2 ** (depth + 1)) - 1)
        a.sort(reverse=True)
        for i in range(len(a)):
            self.HeapArray[i] = a[i]

    def GetMax(self):
        if len(self.HeapArray) == 0 or self.HeapArray[0] is None:
            return -1
        max_node: int = self.HeapArray[0]
        last_node: int = self._get_last_node_index()
        self.HeapArray[0], self.HeapArray[last_node] = self.HeapArray[last_node], None
        self._sift_down(0, last_node - 1)
        return max_node

    def _sift_down(self, ind: int, last_node: int) -> None:
        child: int = 2 * ind + 1
        if child > last_node:
            return
        if child + 1 <= last_node and self.HeapArray[child + 1] > self.HeapArray[child]:
            child += 1
        if self.HeapArray[ind] < self.HeapArray[child]:
            self.HeapArray[ind], self.HeapArray[child] = self.HeapArray[child], self.HeapArray[ind]
            self._sift_down(child, last_node)

    def _get_last_node_index(self) -> int:
        for i in range(len(self.HeapArray) - 1, -1, -1):
            if self.HeapArray[i] is not None:
                return i
        return -1

    def Add(self, key):
        last_ind: int = self._get_last_node_index()
        if last_ind == len(self.HeapArray) - 1:
            return False
        self.HeapArray[last_ind + 1] = key
        self._sift_up(last_ind + 1)
        return True

    def _sift_up(self, ind: int) -> None:
        parent: int = int((ind - 1) / 2)
        if parent < 0:
            return
        if self.HeapArray[parent] < self.HeapArray[ind]:
            self.HeapArray[parent], self.HeapArray[ind] = self.HeapArray[ind], self.HeapArray[parent]
            self._sift_up(parent)


    # Рефлексия по 7.3 Добавьте метод проверки, что массив действительно содержит корректную кучу.
    # Задание без звездочки, реализованный алгоритм в принципе простой: проверяю корректность узла с его левым и правым потомком,
    # затем два рекурсивных вызова для каждого из потомков. Проверку, что родитель больше потомка, реализовал отдельным методом,
    # чтобы не загромождать код основной функции.

    # Рефлексия по 7.4.* Добавьте метод поиска максимального элемента в заданном диапазоне значений.
    # В процессе написания несколько раз запутывался, так что наверное из-за этого получилось неидеально.
    # Есть некоторое ощущение тяжеловесности кода - слишком много проверок и условий, плюс некоторое количество дублирующегося кода.
    # Наверное можно где-то немного упростить/улучшить

    # Рефлексия по 7.5* Подумайте над эффективным алгоритмом поиска в куче элемента по заданному условию (например, меньше заданного значения).
    # Тут есть некие подозрения на правильность "вывода" свойств кучи, но вроде бы отметил правильные. Ответ соответственно строился исходя из них.

    # Рефлексия по 7.6.* Добавьте метод объединения текущей кучи с кучей-параметром.
    # Для реализации задачи добавил один дополнительный публичный метод: copy(), создающий копию кучи.
    # В решении делаю копию обеих куч - и исходной кучи и кучи-параметра. Т.е. по итогу метод union не меняет
    # ни исходную кучу, ни кучу-параметр, а создает новую кучу.

    # Рефлексия по эталонным решениям для занятия 5. Строим сбалансированные двоичные деревья поиска
    # для 5.2. Оцените, насколько поиск узла в дереве, представленном в виде массива, эффективнее (или неэффективнее) поиска узла в классическом дереве с указателями.
    # Здесь мой ответ был не до конца полный, т.к. я указал собственно на зависимость эффективности от заполнености массива, но конкретных примеров не привел.

    # Рефлексия по эталонным решениям для занятия 5. Строим сбалансированные двоичные деревья поиска
    # для 5.3.* Реализуйте метод удаления узла из двоичного дерева, заданного в виде массива.
    # Решение получилось неэффективным. "Перебалансировка" дерева в решении производится постоянно, собственно само удаление реализовано через пересоздание дерева,
    # т.к. при решении задачи я посчитал необходимым перебалансировать дерево после любого удаления.

    # Рефлексия по эталонным решениям для занятия 5. Строим сбалансированные двоичные деревья поиска
    # для 5.4.* Подумайте, как ответить на вопрос с картинки (Sort B-tree in O(1) time).
    # Ну тут я правильно воспользовался определением B-tree :)