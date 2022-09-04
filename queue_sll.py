# Name: Eric Hauschild
# OSU Email: hauschie@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3
# Due Date: 5/2/2022
# Description: This program contains the class for a queue implemented using nodes with methods I created below the
#       dotted line.


from SLNode import SLNode


class QueueException(Exception):
    """
    Custom exception to be used by Queue class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Queue:
    def __init__(self):
        """
        Initialize new queue with head and tail nodes
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = None
        self._tail = None

    def __str__(self):
        """
        Return content of queue in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'QUEUE ['
        if not self.is_empty():
            node = self._head
            out = out + str(node.value)
            node = node.next
            while node:
                out = out + ' -> ' + str(node.value)
                node = node.next
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the queue is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._head is None

    def size(self) -> int:
        """
        Return number of elements currently in the queue
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        node = self._head
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    # -----------------------------------------------------------------------

    def enqueue(self, value: object) -> None:
        """
        This method adds a new value to the end of the queue. It must be implemented with O(1)
        runtime complexity.
        """
        if self.is_empty() is True:
            first_value = SLNode(value)
            self._head = first_value
            self._tail = first_value
        else:
            old_tail = self._tail
            new_tail = SLNode(value)
            self._tail = new_tail
            old_tail.next = new_tail

    def dequeue(self) -> object:
        """
        This method removes and returns the value from the beginning of the queue. It must be
        implemented with O(1) runtime complexity. If the queue is empty, the method raises a
        custom “QueueException”. Code for the exception is provided in the skeleton file.
        """
        if self.is_empty() is True:
            raise QueueException()
        else:
            old_head = self._head
            future_head = old_head.next
            self._head = future_head
            return old_head.value

    def front(self) -> object:
        """
        This method returns the value of the front element of the queue without removing it. It
        must be implemented with O(1) runtime complexity. If the queue is empty, the method
        raises a custom “QueueException”. Code for the exception is provided in the skeleton file.
        """
        if self.is_empty() is True:
            raise QueueException()
        else:
            old_head = self._head
            return old_head.value


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# enqueue example 1")
    q = Queue()
    print(q)
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)

    print("\n# dequeue example 1")
    q = Queue()
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)
    for i in range(6):
        try:
            print(q.dequeue())
        except Exception as e:
            print("No elements in queue", type(e))

    print('\n#front example 1')
    q = Queue()
    print(q)
    for value in ['A', 'B', 'C', 'D']:
        try:
            print(q.front())
        except Exception as e:
            print("No elements in queue", type(e))
        q.enqueue(value)
    print(q)
