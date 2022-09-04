# Name: Eric Hauschild
# OSU Email: hauschie@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3
# Due Date: 5/2/2022
# Description: This program contains the class for a Queue implemented using static arrays with methods I created
#       below the dotted line.


from static_array import StaticArray


class QueueException(Exception):
    """
    Custom exception to be used by Queue class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Queue:
    def __init__(self) -> None:
        """
        Initialize new queue based on Static Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._sa = StaticArray(4)
        self._front = 0
        self._back = -1
        self._current_size = 0

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        size = self._current_size
        out = "QUEUE: " + str(size) + " element(s). ["

        front_index = self._front
        for _ in range(size - 1):
            out += str(self._sa[front_index]) + ', '
            front_index = self._increment(front_index)

        if size > 0:
            out += str(self._sa[front_index])

        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the queue is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._current_size == 0

    def size(self) -> int:
        """
        Return number of elements currently in the queue
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._current_size

    def _increment(self, index: int) -> int:
        """
        Move index to next position
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """

        # employ wraparound if needed
        index += 1
        if index == self._sa.length():
            index = 0

        return index

    # -----------------------------------------------------------------------

    def enqueue(self, value: object) -> None:
        """
        This method adds a new value to the end of the queue. It must be implemented with O(1)
        amortized runtime complexity.
        """
        # If the list has reached its capacity
        if self.size() >= self._sa.length():
            new_array = StaticArray(self.size() * 2)
            index_counter = 0
            while index_counter < self.size():
                value_to_enter = self._sa.get(index_counter)
                new_array.set(index_counter, value_to_enter)
                index_counter += 1
            self._sa = new_array
        # If list is empty
        if self.is_empty() is True:
            self._sa.set(0, value)
        # entering in data in standard situation
        else:
            self._sa.set(self.size(), value)
        self._current_size += 1


    def dequeue(self) -> object:
        """
        This method removes and returns the value at the beginning of the queue. It must be
        implemented with O(1) runtime complexity. If the queue is empty, the method raises a
        custom “QueueException”. Code for the exception is provided in the skeleton file.
        """
        if self.is_empty() is True:
            raise QueueException()
        else:
            object_to_return = self._sa.get(self._front)
            self._front += 1
            self._current_size -= 1
            return object_to_return

    def front(self) -> object:
        """
        This method returns the value of the front element of the queue without removing it. It
        must be implemented with O(1) runtime complexity. If the queue is empty, the method
        raises a custom “QueueException”. Code for the exception is provided in the skeleton file.
        """
        if self.is_empty() is True:
            raise QueueException()
        else:
            object_to_return = self._sa.get(self._front)
            self._front += 1
            self._current_size -= 1
            return object_to_return

    # The method below is optional, but recommended, to implement. #
    # You may alter it in any way you see fit.                     #

    def _double_queue(self) -> None:
        """
        TODO: Write this implementation
        """
        pass


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
    for i in range(q.size() + 1):
        try:
            print(q.dequeue())
        except Exception as e:
            print("No elements in queue", type(e))
    for value in [6, 7, 8, 111, 222, 3333, 4444]:
        q.enqueue(value)
    print(q)

    print('\n# front example 1')
    q = Queue()
    print(q)
    for value in ['A', 'B', 'C', 'D']:
        try:
            print(q.front())
        except Exception as e:
            print("No elements in queue", type(e))
        q.enqueue(value)
    print(q)
