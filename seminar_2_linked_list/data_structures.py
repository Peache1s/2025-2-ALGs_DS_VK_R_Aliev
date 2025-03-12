"""
Модуль со структурами данных с 2 лекции
"""


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append_front(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.size += 1
            return

        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def append_back(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.size += 1
            return

        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
        cur_node.next = new_node
        self.size += 1

    def insert(self, after, n):
        search = self.head

        while search is not None:
            if search.data == after:
                break
            search = search.next

        if search is not None:
            node = Node(n)
            node.next = search.next
            search.next = node
        self.size += 1

    def display(self):
        cur_node = self.head
        output = ""

        while cur_node is not None:
            output += str(cur_node.data)
            if cur_node.next:
                output += " -> "
            cur_node = cur_node.next
        print(output)

    def __len__(self):
        return self.size

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)

        if not self.top:
            self.top = new_node
            return

        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.top:
            return None

        top = self.top
        if self.top.next is not None:
            self.top = self.top.next
        else:
            self.top = None

        return top.data

    def display(self):
        cur_node = self.top
        output = ""

        while cur_node is not None:
            output += str(cur_node.data)
            if cur_node.next:
                output += " -> "
            cur_node = cur_node.next
        print(output)


class Node2:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class Queue:
    def __init__(self):
        self.head = Node2()
        self.tail = Node2()

        self.head.next = self.tail
        self.head.prev = self.head

        self.size = 0

    def push(self, value):
        new_node = Node2(value)

        new_node.next = self.head.next
        new_node.prev = self.head

        self.head.next.prev = new_node
        self.head.next = new_node
        self.size += 1

    def pop(self):
        if self.head.next == self.tail:
            return None

        pop_result = self.tail.prev
        self.tail.prev = pop_result.prev
        pop_result.prev.next = pop_result.next

        pop_result.next = None
        pop_result.prev = None

        self.size -= 1
        return pop_result.data

    def peek(self):
        return self.tail.prev.data

    def display(self):
        cur_node = self.head.next
        output = ""

        while cur_node is not self.tail:
            output += str(cur_node.data)
            if cur_node.next is not self.tail:
                output += " <-> "
            cur_node = cur_node.next
        print(output)

    def __len__(self):
        return self.size


class Deque:
    def __init__(self):
        self.head = Node2()
        self.tail = Node2()

        self.head.next = self.tail
        self.tail.prev = self.head

        self.size = 0

    def push_front(self, value):
        new_node = Node2(value)

        new_node.next = self.head.next
        new_node.prev = self.head

        self.head.next.prev = new_node
        self.head.next = new_node
        self.size += 1

    def push_back(self, value):
        new_node = Node2(value)

        new_node.prev = self.tail.prev
        self.tail.prev.next = new_node
        self.tail.prev = new_node
        new_node.next = self.tail

        self.size += 1

    def pop_back(self):
        if self.head.next == self.tail:
            return None

        pop_result = self.tail.prev
        self.tail.prev = pop_result.prev
        pop_result.prev.next = pop_result.next

        pop_result.next = None
        pop_result.prev = None

        self.size -= 1
        return pop_result.data

    def pop_front(self):
        if self.head.next == self.tail:
            return None

        pop_result = self.head.next
        self.head.next = pop_result.next
        pop_result.next.prev = pop_result.prev

        pop_result.next = None
        pop_result.prev = None

        self.size -= 1
        return pop_result.data

    def display(self):
        cur_node = self.head.next
        output = ""

        while cur_node is not self.tail:
            output += str(cur_node.data)
            if cur_node.next is not self.tail:
                output += " <-> "
            cur_node = cur_node.next
        print(output)

    def __len__(self):
        return self.size
