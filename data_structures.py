"""-----------------------------------------------------------------

The library contains common algorithms and data structure examples.
Search algorithms.

Title:          Common Algorithms
Author:         Roman Zajic
Last modified:  2022-12-11

-----------------------------------------------------------------"""


class Node:

    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def __iter__(self):
        current_node = self.head
        while current_node is not None:
            yield current_node.value
            current_node = current_node.next

    def __str__(self):
        current_node = self.head
        if current_node is None:
            return "[]"

        result = "["
        while current_node:
            result = result + str(current_node.value) + "->"
            current_node = current_node.next
        result = result[:-2] + "]"
        return result

    def add_item(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def search_item(self, value):
        index = 0
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return index
            index += 1
            current_node = current_node.next

        return None

    def remove_item(self, value):

        current_node = self.head

        # If item is in head
        if current_node.value == value:
            self.head = current_node.next
            return

        # If item is not in head check if it is in next element
        while current_node.next:
            if current_node.next.value == value:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next
