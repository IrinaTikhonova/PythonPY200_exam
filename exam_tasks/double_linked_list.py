from typing import Optional, Any

from exam_tasks.nodes import DoubleLinkedNode
from exam_tasks.linked_list import LinkedList


class DoubleLinkedList(LinkedList):
    # todo перегрузить атрибут класса

    def append(self, value: Any):
        """ Добавление элемента в конец двусвязного списка. """
        append_node = DoubleLinkedNode(value)

        if self._head is None:
            self._head = self._tail = append_node
        else:
            self.double_linked_nodes(self._tail, append_node)
            self._tail = append_node

        self._len += 1

    @staticmethod
    def double_linked_nodes(left_node: Optional[DoubleLinkedNode] = None,
                            right_node: Optional[DoubleLinkedNode] = None) -> None:
        """
        Функция, которая связывает между собой два узла.

        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел
        """
        left_node.next = right_node
        right_node.prev = left_node

    def insert(self, index: int, value: Any) -> None:
        if not isinstance(index, int):
            raise TypeError()

        insert_node = DoubleLinkedNode(value)
        if index == 0:
            insert_node.next = self._head
            self._head.prev = insert_node
            self._head = insert_node
            self._len += 1

        elif index >= self.len - 1:
            self.append(value)
        else:
            prev_node = self.step_by_step_on_nodes(index - 1)
            next_node = prev_node.next

            self.double_linked_nodes(prev_node, insert_node)
            self.double_linked_nodes(insert_node, next_node)

            self._len += 1

    def __delitem__(self, index: int):
        """Удаляет элемент по указанному индексу"""

        if self.index_validaton(index):

            if index == 0:
                self._head = self.head.next
            elif index == self.len - 1:
                self._tail = self._tail.prev
                self.tail.next = None
            else:
                del_node = self.step_by_step_on_nodes(index)
                prev_node = del_node.prev
                next_node = del_node.next

                self.double_linked_nodes(prev_node, next_node)

            self._len -= 1


if __name__ == "__main__":
    dll = DoubleLinkedList([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(dll)
    print(dll.pop(3))
    print(dll.len)
    dll.insert(3, 3)
    print(dll)
    dll.extend([10, 11, 12])
    print(dll)
    print(dll.head)
    print(dll.tail.prev)
