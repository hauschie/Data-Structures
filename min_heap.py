# Name: Eric Hauschild
# OSU Email: hauschie@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 5
# Due Date: 5/23/2022
# Description: This file contains the class for a MinHeap with various methods within it.


from dynamic_array import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initialize a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        heap_data = [self._heap[i] for i in range(self._heap.length())]
        return 'HEAP ' + str(heap_data)

    def add(self, node: object) -> None:
        """
        This method adds a new object to the MinHeap while maintaining heap property.
        """
        if self.is_empty() is True:
            self._heap.append(node)
        else:
            child_index = self._heap.length()
            self._heap.append(node)
            parent_index = (child_index - 1) // 2
            child_node = self._heap.get_at_index(child_index)
            parent_node = self._heap.get_at_index(parent_index)
            while child_index != 0:
                if self._heap.get_at_index(child_index) < self._heap.get_at_index(parent_index):
                    child_node = self._heap.get_at_index(child_index)
                    parent_node = self._heap.get_at_index(parent_index)
                    self._heap.set_at_index(child_index, parent_node)
                    self._heap.set_at_index(parent_index, child_node)
                    child_index = parent_index
                    parent_index = (child_index - 1) // 2
                else:
                    break

    def is_empty(self) -> bool:
        """
        This method returns True if the heap is empty; otherwise, it returns False.
        """
        if self._heap.is_empty() is True:
            return True
        else:
            return False

    def get_min(self) -> object:
        """
        This method returns an object with the minimum key, without removing it from the heap. If
        the heap is empty, the method raises a MinHeapException.
        """
        if self.is_empty() is True:
            raise MinHeapException
        else:
            return self._heap.get_at_index(0)

    def remove_min(self) -> object:
        """
        This method returns an object with the minimum key, and removes it from the heap. If the
        heap is empty, the method raises a MinHeapException.
        For the downward percolation of the replacement node: if both children of the node have
        the same value (and are both smaller than the node), swap with the left child.
        """
        if self.is_empty() is True:
            raise MinHeapException
        else:
            min_to_return = self._heap.get_at_index(0)
            self._heap.set_at_index(0, self._heap.get_at_index(self._heap.length() - 1))
            self._heap.remove_at_index(self._heap.length() - 1)
            _percolate_down(self._heap, 0, self._heap.length())
            return min_to_return


    def build_heap(self, da: DynamicArray) -> None:
        """
        This method receives a Dynamic Array with objects in any order, and builds a proper
        MinHeap from them. The current content of the MinHeap is overwritten.
        """
        new_dynamic_array = DynamicArray()
        da_loop_counter = 0
        while da_loop_counter != da.length():
            new_dynamic_array.append(da.get_at_index(da_loop_counter))
            da_loop_counter += 1
        parent_index = (new_dynamic_array.length() - 2) // 2
        while parent_index != -1:
            _percolate_down(new_dynamic_array, parent_index, new_dynamic_array.length())
            parent_index = parent_index - 1
        self._heap = new_dynamic_array

    def size(self) -> int:
        """
        This method returns the number of items currently stored in the heap.
        """
        return self._heap.length()

    def clear(self) -> None:
        """
        This method clears the contents of the heap.
        """
        self._heap = DynamicArray()


def heapsort(da: DynamicArray) -> None:
    """
    Write a function that receives a DynamicArray and sorts its content in non-ascending order,
    using the Heapsort algorithm. You must sort the array in place, without creating a new
    array. This method does not return anything.
    You may assume that the input array will contain at least one element, and that values
    stored in the array are all of the same type (either all numbers, or strings, or custom
    objects, but never a mix of these). You do not need to write checks for these conditions.
    """
    parent_index = (da.length() - 2) // 2
    while parent_index != -1:
        _percolate_down(da, parent_index, da.length())
        parent_index = parent_index - 1
    final_index = da.length() - 1
    while final_index != 0:
        parent = da.get_at_index(0)
        da.set_at_index(0, da.get_at_index(final_index))
        da.set_at_index(final_index, parent)
        final_index -= 1
        _percolate_down(da, 0, final_index + 1)


# It's highly recommended that you implement the following optional          #
# helper function for percolating elements down the MinHeap. You can call    #
# this from inside the MinHeap class. You may edit the function definition.  #

def _percolate_down(da: DynamicArray, pi, length) -> None:
    """
    ensures that the parent value is percolated down so that it is not bigger than its child nodes
    """
    if length <= 1:
        pass
    else:
        parent_index = pi
        parent_node = da.get_at_index(parent_index)
        child_index_1 = (parent_index + 1) * 2 - 1
        child_index_2 = (parent_index + 1) * 2
        while child_index_1 < length:
            if child_index_2 >= length:
                child_index = child_index_1
                child_node = da.get_at_index(child_index)
            else:
                child_node_1 = da.get_at_index(child_index_1)
                child_node_2 = da.get_at_index(child_index_2)
                if child_node_1 > child_node_2:
                    child_node = child_node_2
                    child_index = child_index_2
                else:
                    child_node = child_node_1
                    child_index = child_index_1

            if parent_node > child_node:
                da.set_at_index(child_index, parent_node)
                da.set_at_index(parent_index, child_node)
                parent_index = child_index
                parent_node = da.get_at_index(parent_index)
                child_index_1 = (parent_index + 1) * 2 - 1
                child_index_2 = (parent_index + 1) * 2
            else:
                break




# ------------------- BASIC TESTING -----------------------------------------


if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)

    print("\nPDF - is_empty example 1")
    print("-------------------")
    h = MinHeap([2, 4, 12, 56, 8, 34, 67])
    print(h.is_empty())

    print("\nPDF - is_empty example 2")
    print("-------------------")
    h = MinHeap()
    print(h.is_empty())

    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())

    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty() and h.is_empty() is not None:
        print(h, end=' ')
        print(h.remove_min())

    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)

    print("--------------------------")
    print("Inserting 500 into input DA:")
    da[0] = 500
    print(da)

    print("Your MinHeap:")
    print(h)
    if h.get_min() == 500:
        print("Error: input array and heap's underlying DA reference same object in memory")

    print("\nPDF - heapsort example 1")
    print("------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - heapsort example 2")
    print("------------------------")
    da = DynamicArray(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - size example 1")
    print("--------------------")
    h = MinHeap([100, 20, 6, 200, 90, 150, 300])
    print(h.size())

    print("\nPDF - size example 2")
    print("--------------------")
    h = MinHeap([])
    print(h.size())

    print("\nPDF - clear example 1")
    print("---------------------")
    h = MinHeap(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(h)
    print(h.clear())
    print(h)
