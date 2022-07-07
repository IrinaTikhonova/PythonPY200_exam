from typing import Optional, Any, Iterable

from exam_tasks.nodes import Node

from collections.abc import MutableSequence


class LinkedList(MutableSequence):
    def __init__(self, data: Iterable = None):
        """Инициализация односвязного списка"""
        self._len = 0
        self._head: Optional[Node] = None
        self._tail = self._head

        if data is not None:
            for value in data:
                self.append(value)

    def append(self, value: Any):
        """ Добавление элемента в конец связного списка. """
        append_node = Node(value)

        if self._head is None:
            self._head = self._tail = append_node
        else:
            self.linked_nodes(self._tail, append_node)
            self._tail = append_node

        self._len += 1

    def index_validaton(self, index):

        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self.len:
            raise IndexError()

        else:
            return True

    def step_by_step_on_nodes(self, index: int):
        """ Функция выполняет перемещение по узлам до указанного индекса. И возвращает узел. """

        if self.index_validaton(index):

            current_node = self._head
            for _ in range(index):
                current_node = current_node.next

            return current_node

    @staticmethod
    def linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        """
        Функция, которая связывает между собой два узла.

        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел
        """
        left_node.next = right_node

    def __getitem__(self, index: int) -> Any:
        """ Метод возвращает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        return node.value

    def __setitem__(self, index: int, value: Any) -> None:
        """ Метод устанавливает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        node.value = value

    def to_list(self) -> list:
        return [linked_list_value for linked_list_value in self]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.to_list()})"

    def __str__(self) -> str:
        return f"{self.to_list()}"

    @property
    def head(self):
        return self._head

    @property
    def tail(self):
        return self._tail

    @property
    def len(self):
        return self._len

    def __len__(self):
        return self._len

    def insert(self, index: int, value: Any) -> None:
        """Метод для добавления в связный список элемента слева от указанного индекса"""

        if not isinstance(index, int):
            raise TypeError()

        insert_node = Node(value)
        if index == 0:
            insert_node.next = self.head
            self._head = insert_node
            self._len += 1

        elif index >= self.len - 1:
            self.append(value)
        else:
            prev_node = self.step_by_step_on_nodes(index - 1)
            next_node = prev_node.next

            self.linked_nodes(prev_node, insert_node)
            self.linked_nodes(insert_node, next_node)

            self._len += 1

    def __delitem__(self, index: int):
        """Метод удаляет элемент по указанному индексу"""

        if self.index_validaton(index):

            if index == 0:
                self._head = self.head.next
            elif index == self.len - 1:
                tail = self.step_by_step_on_nodes(index - 1)
                tail.next = None
            else:
                prev_node = self.step_by_step_on_nodes(index - 1)
                del_node = prev_node.next
                next_node = del_node.next

                self.linked_nodes(prev_node, next_node)

            self._len -= 1

    def count(self, value, start=0, stop=None):
        """ Данный метод считает количество вхождений значения в односвязный список """

        cnt = 0
        if stop is None:
            for index in range(start, self.len):
                node = self.step_by_step_on_nodes(index)
                if node.value == value:
                    cnt += 1
        else:
            for index in range(start, stop + 1):
                node = self.step_by_step_on_nodes(index)
                if node.value == value:
                    cnt += 1

        return f"Значение {value} повторяется {cnt} раз"

    def extend(self, list_):
        """ Метод для добавления в связный список сразу нескольких элементов """

        for i in range(0, len(list_)):
            self.append(list_[i])

    def pop(self, index=None):
        """Метод удаляет элемент по указанному индексу и возвращает его значение.
        Если индекс не указан, удаляется последний элемент с конца """

        if index is None:
            deleted = self.__getitem__(self.len - 1)
            self.__delitem__(self.len - 1)
        else:
            deleted = self.__getitem__(index)
            self.__delitem__(index)

        return deleted


if __name__ == "__main__":
    ll = LinkedList([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(repr(ll))
    print(ll.pop(3))
    print(ll.len)
    ll.insert(3, 3)
    print(ll)
    ll.extend([10, 11, 12])
    print(ll)
    print(ll.head)
    print(ll.tail)

