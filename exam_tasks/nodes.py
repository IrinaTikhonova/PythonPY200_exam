from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """
        Создаем новый узел для односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        """
        self.value = value
        self.next = next_

    def __repr__(self) -> str:
        return f"Node({self.value}, {None})" if self._next is None \
            else f"Node({self.value}, Node({self._next}))"

    def __str__(self) -> str:
        return str(self.value)

    @staticmethod
    def is_valid(node: Any) -> None:
        if not isinstance(node, (type(None), Node)):
            raise TypeError

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_: Optional["Node"]):
        self.is_valid(next_)
        self._next = next_


class DoubleLinkedNode(Node):
    """ Класс, который описывает узел двусвязного списка. """

    def __init__(self, value, next_: Optional["DoubleLinkedNode"] = None, prev_: Optional["DoubleLinkedNode"] = None):
        """
                Создаем новый узел для односвязного списка
                :param value: Любое значение, которое помещено в узел
                :param next_: следующий узел, если он есть
                :param prev_: предыдущий узел, если он есть
                """
        super().__init__(value, next_)
        self.prev = prev_

    def __repr__(self):
        if self.next is None and self.prev is None:
            return f"({None}, {self.value}, {None})"
        elif self.next is None:
            return f"DoubleLinkedNode(DoubleLinkedNode({self.prev}), {self.value}, {None})"
        elif self.prev is None:
            return f"DoubleLinkedNode({None}, {self.value}, DoubleLinkedNode({self.next})"
        else:
            return f"DoubleLinkedNode(DoubleLinkedNode({self.prev}), {self.value}, DoubleLinkedNode({self.next}))"

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, prev_: Optional["DoubleLinkedNode"] = None):
        self.is_valid(prev_)
        self._prev = prev_

    # todo is_valid либо перегрузить либо переписать в родителе


if __name__ == "__main__":
    dln = DoubleLinkedNode(5)
    dln1 = DoubleLinkedNode(10)
    dln2 = DoubleLinkedNode(15)
    dln.next = dln1
    dln1.prev = dln
    dln1.next = dln2
    dln2.prev = dln1
    print([dln, dln1, dln2])
