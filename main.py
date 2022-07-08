from exam_tasks.double_linked_list import DoubleLinkedList


if __name__ == '__main__':
    list_of_commits = DoubleLinkedList(["init"])
    list_of_commits.extend(["nodes", "double_linked_list"])
    list_of_commits.append("additional_methods")
    list_of_commits.insert(2, "linked_list")
    print(list_of_commits)
    print(list_of_commits.head)
    print(list_of_commits.tail)
    print(list_of_commits.tail.prev)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
