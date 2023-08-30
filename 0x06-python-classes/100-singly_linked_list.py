#!/usr/bin/python3
"""
100-singly_linked_list.py
a class Node that defines a node of a singly linked list by:
    Private instance attribute: data:
        property def data(self): to retrieve it
        property setter def data(self, value): to set it:
            data must be an integer, otherwise raise a TypeError
            exception with the message data must be an integer
    Private instance attribute: next_node:
        property def next_node(self): to retrieve it
        property setter def next_node(self, value): to set it:
            next_node can be None or must be a Node, otherwise raise
            a TypeError exception with the message next_node must
            be a Node object
    Instantiation with data and next_node:
    def __init__(self, data, next_node=None):
"""


class Node:
    """class Node that defines a singly linked list"""
    def __init__(self, data, next_node=None):
        """Instantiation with data and next_node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """get node data"""
        return self.__data

    @data.setter
    def data(self, value):
        """sets node data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """get next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


"""
a class SinglyLinkedList that defines a singly linked list by:
    Private instance attribute: head (no setter or getter)
    Simple instantiation: def __init__(self):
    Should be printable:
        print the entire list in stdout
        one node number by line
    Public instance method: def sorted_insert(self, value):
        that inserts a new Node into the correct sorted position in
        the list (increasing order)
"""


class SinglyLinkedList:
    """class SinglyLinkedList"""
    def __init__(self):
        """Instantiation"""
        self.head = None

    def sorted_insert(self, value):
        """inserts new node"""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        if value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """makes list printable"""
        values = []
        current = self.head
        while current:
            values.append(str(current.data))
            current = current.next_node
        return "\n".join(values)
