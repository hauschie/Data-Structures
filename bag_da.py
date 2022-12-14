# Name: Eric Hauschild
# OSU Email: hauschie@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 2
# Due Date: 4/26/2022 (1 day extension)
# Description: This file contains a class for a bag, including several methods provided by my instructor, along with
#       methods created by me. The methods created by me are below the first line and include add(), remove(), count(),
#       clear(), equal(), __iter__(), and __next__().


from dynamic_array import *


class Bag:
    def __init__(self, start_bag=None):
        """
        Init new bag based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._da = DynamicArray()

        # populate bag with initial values (if provided)
        # before using this feature, implement add() method
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "BAG: " + str(self._da.length()) + " elements. ["
        out += ', '.join([str(self._da.get_at_index(_))
                          for _ in range(self._da.length())])
        return out + ']'

    def size(self) -> int:
        """
        Return total number of items currently in the bag
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da.length()

    # -----------------------------------------------------------------------

    def add(self, value: object) -> None:
        """
        This method adds a new element to the bag. It must be implemented with O(1) amortized
        runtime complexity.
        """
        self._da.append(value)

    def remove(self, value: object) -> bool:
        """
        This method removes any one element from the bag that matches the provided value
        object. It returns True if some object was actually removed from the bag. Otherwise, it
        returns False. This method must be implemented with O(N) runtime complexity.
        """
        current_index = 0
        while current_index < self._da.length():
            if self._da.get_at_index(current_index) == value:
                self._da.remove_at_index(current_index)
                return True
            current_index += 1
        return False

    def count(self, value: object) -> int:
        """
        This method returns the number of elements in the bag that match the provided value
        object. It must be implemented with O(N) runtime complexity.
        """
        current_index = 0
        number_of_matches = 0
        while current_index < self._da.length():
            if self._da.get_at_index(current_index) == value:
                number_of_matches += 1
            current_index += 1
        return number_of_matches

    def clear(self) -> None:
        """
        This method clears the contents of the bag. It must be implemented with O(1) runtime
        complexity.
        """
        self._da = DynamicArray()

    def equal(self, second_bag: "Bag") -> bool:
        """
        This method compares the contents of a bag with the contents of a second bag provided as
        a parameter. The method returns True if the bags are equal (contain the same number of
        elements, and also contain the same elements without regard to the order of elements).
        Otherwise, it returns False. An empty bag is only considered equal to another empty bag.
        """
        if self._da.length() != second_bag._da.length():
            return False
        else:
            current_index_first = 0
            while current_index_first < self._da.length():
                current_value = self._da.get_at_index(current_index_first) # 10
                first_bag_repeats = self.count(current_value)
                second_bag_repeats = second_bag.count(current_value)
                if second_bag_repeats != first_bag_repeats:
                    return False
                current_index_first += 1
            return True

    def __iter__(self):
        """
        This method enables the Bag to iterate across itself. Implement this method in a similar way
        to the example in Exploration: Encapsulation and Iterators.
        """
        self._index = 0
        return self

    def __next__(self):
        """
        This method will return the next item in the Bag, based on the current location of the
        iterator.  Implement this method in a similar way to the example in Exploration:
        Encapsulation and Iterators.
        """
        try:
            new_index = self._index
            value = self._da.get_at_index(new_index)
        except DynamicArrayException:
            raise StopIteration

        self._index = self._index + 1
        return value


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# add example 1")
    bag = Bag()
    print(bag)
    values = [10, 20, 30, 10, 20, 30]
    for value in values:
        bag.add(value)
    print(bag)

    print("\n# remove example 1")
    bag = Bag([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(bag)
    print(bag.remove(7), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)

    print("\n# count example 1")
    bag = Bag([1, 2, 3, 1, 2, 2])
    print(bag, bag.count(1), bag.count(2), bag.count(3), bag.count(4))

    print("\n# clear example 1")
    bag = Bag([1, 2, 3, 1, 2, 3])
    print(bag)
    bag.clear()
    print(bag)

    print("\n# equal example 1")
    bag1 = Bag([10, 20, 30, 40, 50, 60])
    bag2 = Bag([60, 50, 40, 30, 20, 10])
    bag3 = Bag([10, 20, 30, 40, 50])
    bag_empty = Bag()

    print(bag1, bag2, bag3, bag_empty, sep="\n")
    print(bag1.equal(bag2), bag2.equal(bag1))
    print(bag1.equal(bag3), bag3.equal(bag1))
    print(bag2.equal(bag3), bag3.equal(bag2))
    print(bag1.equal(bag_empty), bag_empty.equal(bag1))
    print(bag_empty.equal(bag_empty))
    print(bag1, bag2, bag3, bag_empty, sep="\n")

    bag1 = Bag([100, 200, 300, 200])
    bag2 = Bag([100, 200, 30, 100])
    print(bag1.equal(bag2))

    print("\n# __iter__(), __next__() example 1")
    bag = Bag([5, 4, -8, 7, 10])
    print(bag)
    for item in bag:
        print(item)

    print("\n# __iter__(), __next__() example 2")
    bag = Bag(["orange", "apple", "pizza", "ice cream"])
    print(bag)
    for item in bag:
        print(item)
