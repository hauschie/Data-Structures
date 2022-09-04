# Name: Eric Hauschild
# OSU Email: hauschie@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3
# Due Date: 5/2/2022
# Description: This program contains the class for a Singly Linked List with methods I created below the dotted line.


from SLNode import *


class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class LinkedList:
    def __init__(self, start_list=None) -> None:
        """
        Initialize new linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = SLNode(None)

        # populate SLL with initial values (if provided)
        # before using this feature, implement insert_back() method
        if start_list is not None:
            for value in start_list:
                self.insert_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'SLL ['
        node = self._head.next
        while node:
            out += str(node.value)
            if node.next:
                out += ' -> '
            node = node.next
        out += ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        length = 0
        node = self._head.next
        while node:
            length += 1
            node = node.next
        return length

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return not self._head.next

    # ------------------------------------------------------------------ #

    def insert_front(self, value: object) -> None:
        """
        This method adds a new node at the beginning of the list (right after the front sentinel).
        """
        # If the SLL is empty
        if self._head.next is None:
            self._head.next = SLNode(value)
        # If the SLL has at least 1 value
        else:
            old_front = self._head.next
            self._head.next = SLNode(value, old_front)


    def insert_back(self, value: object) -> None:
        """
        This method adds a new node at the end of the list.
        """
        node_iterator = self._head
        while node_iterator.next is not None:
            node_iterator = node_iterator.next
        node_iterator.next = SLNode(value)


    def insert_at_index(self, index: int, value: object) -> None:
        """
        This method inserts a new value at the specified index position in the linked list.
        Index 0 refers to the beginning of the list (right after the front sentinel).
        """
        # If index is invalid
        if index > self.length() or index < 0:
            raise SLLException()
        index_iterator = 0
        previous_value = self._head
        node_iterator = self._head.next
        # Locates the node at the specified index
        while index_iterator != index:
            previous_value = node_iterator
            node_iterator = node_iterator.next
            index_iterator += 1
        previous_value.next = SLNode(value, node_iterator)

    def remove_at_index(self, index: int) -> None:
        """
        This method removes the node at the specified index position from the linked list.
        Index 0 refers to the beginning of the list (right after the front sentinel).
        """
        # If index is invalid
        if index >= self.length() or index < 0:
            raise SLLException()
        index_iterator = 0
        previous_value = self._head
        node_iterator = self._head.next
        # Locates the node at the specified index
        while index_iterator != index:
            previous_value = node_iterator
            node_iterator = node_iterator.next
            index_iterator += 1
        previous_value.next = node_iterator.next

    def remove(self, value: object) -> bool:
        """
        This method traverses the list from the beginning to the end and removes the first node that
        matches the provided “value” object. The method returns True if a node was removed from
        the list. Otherwise, it returns False.
        """
        previous_value = self._head
        node_iterator = self._head.next
        # Iterating to search for a match
        while node_iterator is not None:
            if node_iterator.value == value:
                previous_value.next = node_iterator.next
                return True
            previous_value = node_iterator
            node_iterator = node_iterator.next
        return False

    def count(self, value: object) -> int:
        """
        This method counts the number of elements in the list that match the provided “value”
        object. The method then returns this number.
        """
        node_iterator = self._head.next
        number_of_matches = 0
        # Iterating to search for a match
        while node_iterator is not None:
            if node_iterator.value == value:
                number_of_matches += 1
            node_iterator = node_iterator.next
        return number_of_matches

    def find(self, value: object) -> bool:
        """
        This method returns a Boolean value based on whether or not the provided “value” object
        exists in the list.
        """
        node_iterator = self._head.next
        # Iterating to search for a match
        while node_iterator is not None:
            if node_iterator.value == value:
                return True
            node_iterator = node_iterator.next
        return False

    def slice(self, start_index: int, size: int) -> "LinkedList":
        """
        This method returns a new LinkedList object that contains the requested number of nodes
        from the original list, starting with the node located at the requested start index. If the
        original list contains N nodes, a valid start_index is in range [0, N - 1] inclusive. The
        original list cannot be modified. The runtime complexity of your implementation must be
        O(N).

        If the provided start index is invalid, or if there are not enough nodes between the start
        index and the end of the list to make a slice of the requested size, this method raises a
        custom “SLLException”. Code for the exception is provided in the skeleton file.
        """
        index_iterator = 0
        new_linked_list = LinkedList()

        # If index is invalid
        if start_index + size > self.length() or start_index < 0 or size < 0 or start_index >= self.length():
            raise SLLException()
        # special case for a slice size of zero
        if size == 0:
            return new_linked_list

        # Locates the start of the slice
        node_iterator_original = self._head
        while index_iterator != start_index:
            node_iterator_original = node_iterator_original.next
            index_iterator += 1

        # Copies slice into new linked list
        node_iterator_copy = new_linked_list._head
        index_iterator = 0
        while index_iterator != size:
            node_iterator_copy.next = SLNode(node_iterator_original.next.value)
            node_iterator_original = node_iterator_original.next
            node_iterator_copy = node_iterator_copy.next
            index_iterator += 1
        return new_linked_list


if __name__ == '__main__':

    print('\n# insert_front example 1')
    lst = LinkedList()
    print(lst)
    lst.insert_front('A')
    lst.insert_front('B')
    lst.insert_front('C')
    print(lst)

    print('\n# insert_back example 1')
    lst = LinkedList()
    print(lst)
    lst.insert_back('C')
    lst.insert_back('B')
    lst.insert_back('A')
    print(lst)

    print('\n# insert_at_index example 1')
    lst = LinkedList()
    test_cases = [(0, 'A'), (0, 'B'), (1, 'C'), (3, 'D'), (-1, 'E'), (5, 'F')]
    for index, value in test_cases:
        print('Insert of', value, 'at', index, ': ', end='')
        try:
            lst.insert_at_index(index, value)
            print(lst)
        except Exception as e:
            print(type(e))

    print('\n# remove_at_index example 1')
    lst = LinkedList([1, 2, 3, 4, 5, 6])
    print(lst)
    for index in [0, 0, 0, 2, 2, -2]:
        print('Removed at index:', index, ': ', end='')
        try:
            lst.remove_at_index(index)
            print(lst)
        except Exception as e:
            print(type(e))
    print(lst)

    print('\n# remove example 1')
    lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(lst)
    for value in [7, 3, 3, 3, 3]:
        print(lst.remove(value), lst.length(), lst)

    print('\n# remove example 2')
    lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(lst)
    for value in [1, 2, 3, 1, 2, 3, 3, 2, 1]:
        print(lst.remove(value), lst.length(), lst)

    print('\n# count example 1')
    lst = LinkedList([1, 2, 3, 1, 2, 2])
    print(lst, lst.count(1), lst.count(2), lst.count(3), lst.count(4))

    print('\n# find example 1')
    lst = LinkedList(["Waldo", "Clark Kent", "Homer", "Santa Clause"])
    print(lst)
    print(lst.find("Waldo"))
    print(lst.find("Superman"))
    print(lst.find("Santa Clause"))

    print('\n# slice example 1')
    lst = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    ll_slice = lst.slice(1, 3)
    print(lst, ll_slice, sep="\n")
    ll_slice.remove_at_index(0)
    print(lst, ll_slice, sep="\n")

    print('\n# slice example 2')
    lst = LinkedList([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", lst)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    for index, size in slices:
        print("Slice", index, "/", size, end="")
        try:
            print(" --- OK: ", lst.slice(index, size))
        except:
            print(" --- exception occurred.")
