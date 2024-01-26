#!/usr/bin/python3

"""Constructs a node, and a linked list of nodes"""


class Node:
    """Represents a node of a linked list"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Returns the data stored in this node"""
        return self._data

    @data.setter
    def data(self, value):
        """Sets the data to be stored in this node"""
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self._data = value

    @property
    def next_node(self):
        """Retrieves this node's next node"""
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        """Sets this node's next node"""
        if not (isinstance(value, Node) or (value is None)):
            raise TypeError('next_node must be a Node object')
        self._next_node = value


class SinglyLinkedList:
    """Represents a singly-linked list"""

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new node into the correct sorted position in the list
        (in increasing order)
        """
        current = self.__head
        new_node = Node(value)

        if self.__head is None:  # make this the first node
            self.__head = new_node
        elif self.__head.data >= value:  # place the new node before
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            while current.next_node and current.next_node.data < value:
                current = current.next_node
            # current node is greater then new one
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Prints the entire list, one node number on every line"""
        print_all = []
        current = self.__head
        while not (current is None):
            print_all.append(str(current.data))
            if current.next_node:  # have a newline between node values
                print_all.append('\n')
            current = current.next_node
        return ''.join(print_all)
