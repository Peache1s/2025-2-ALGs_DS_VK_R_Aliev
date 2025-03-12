"""
Модуль со скриптами со 2-ого семинара
"""
from data_structures import *


def has_cycle(lst):
    """
    Понять является ли односвязный список lst циклическим

    :param lst: односвязный список
    :return: индикатор цикличности: 1 - циклический, 0 - нет
    """
    head = lst.head
    if head is None or head.next is None:
        return False

    slow = head
    fast = head.next

    while slow != fast:
        if fast is None or fast.next is None:
            return False

        slow.next
        fast = fast.next.next
    return True


def reverse_linked_list(lst):
    """
    Разворачиввает односвязный список

    :param lst: односвязный список
    :return: развернутый список
    """
    prev = None
    curr = lst.head

    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    lst.head = prev
    return lst


def middle_val(lst):
    """
    Находит середину односвязного списка lst за O(n) без аллокаций памяти

    :param lst: односвязный список
    :return: узел посередине
    """
    slow = fast = lst.head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow.data


def remove_element(lst, val):
    """
    Удаление элемента val из односвязного списка lst

    :param lst: односвязный список
    :param val: удаляемое значение
    :return: список без val
    """

    head = lst.head

    dummy = Node()
    dummy.next = head
    prev = dummy
    curr = head

    while curr is not None:
        if curr.data == val:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next

    lst.head = dummy.next
    return lst


def is_subsequence_queue(a, b):
    """
    Проверить является ли строка a исхоной для строки b с использованием очереди

    :param a: исходная строка a
    :param b: итоговая строка b
    :return: bool, 1 - является, 0 - нет
    """

    q = Queue()
    for elem in a:
        q.push(elem)

    for elem in b:
        if q.peek() == elem:
            q.pop()

    return len(q) == 0


def is_subsequence_two_pointers(a, b):
    """
    Проверить является ли строка a исхоной для строки b с использованием 2х указателей

    :param a: исходная строка a
    :param b: итоговая строка b
    :return: bool, 1 - является, 0 - нет
    """
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            i += 1
        j += 1
    return i == len(a)


def is_palindrome_stack(str):
    """
    Проверка является ли строка палиндромом c использованием стека

    :param str: строка для проверки
    :return: bool: True - является, False - нет
    """
    stack = Stack()
    for char in str:
        stack.push(char)

    for char in str:
        if char != stack.pop():
            return False
    return True


def is_palindrome_deque(str):
    """
    Проверка является ли строка палиндромом c использованием деки

    :param str: строка для проверки
    :return: bool: True - является, False - нет
    """
    deque = Deque()
    for char in str:
        deque.push_front(char)

    for _ in str:
        if len(deque) == 1:
            return True
        elif deque.pop_front() != deque.pop_back():
            return False

    return True


def is_palindrome_two_pointers(str):
    """
    Проверка является ли строка палиндромом c использованием двух указателей

    :param str: строка для проверки
    :return: bool: True - является, False - нет
    """
    left = 0
    right = len(str) - 1
    while left < right:
        if str[left] != str[right]:
            return False
        left += 1
        right -= 1
    return True


def merge_linked_lists(lst1, lst2):
    """
    Объединяет два отсортированных односвязных списка lst1, lst2 в один res_list

    :param lst1: первый отсортированный односвязный список
    :param lst2: второй отсортированный односвязный список
    :return: объединение спиское
    """
    curr1 = lst1.head
    curr2 = lst2.head
    res_list = LinkedList()

    counter = 0
    while curr1 is not None and curr2 is not None:
        if curr1.data < curr2.data:
            res_list.append_back(curr1.data)
            curr1 = curr1.next

        else:
            res_list.append_back(curr2.data)
            curr2 = curr2.next

        counter += 1
        if counter == 1:
            curr_res_list = res_list.head
        else:
            curr_res_list = curr_res_list.next

    if curr1 is not None and counter > 0:
        curr_res_list.next = curr1

    elif curr2 is not None and counter > 0:
        curr_res_list.next = curr2

    elif curr2 is not None and counter == 0:
        return lst2

    elif curr1 is not None and counter == 0:
        return lst1
    else:
        return LinkedList()

    return res_list
