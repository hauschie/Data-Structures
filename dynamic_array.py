# Name: Eric Hauschild
# OSU Email: hauschie@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 2
# Due Date: 4/26/2022 (1 day extension)
# Description: This file contains a class for a dynamic array, including several methods provided by my instructor,
#       along with methods created by me. The methods created by me are below the first line and include resize(),
#       append(), insert_at_index(), remove_at_index(), slice(), merge(), map(), filter(), reduce(), and find_mode()
#       (find_mode is a seperate class that is not a part of DynamicArray).


from static_array import StaticArray


class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._size = 0
        self._capacity = 4
        self._data = StaticArray(self._capacity)

        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self._size) + "/" + str(self._capacity) + ' ['
        out += ', '.join([str(self._data[_]) for _ in range(self._size)])
        return out + ']'

    def get_at_index(self, index: int) -> object:
        """
        Return value from given index position
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        return self._data[index]

    def set_at_index(self, index: int, value: object) -> None:
        """
        Store value at given index in the array
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        self._data[index] = value

    def __getitem__(self, index) -> object:
        """
        Same functionality as get_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.get_at_index(index)

    def __setitem__(self, index, value) -> None:
        """
        Same functionality as set_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.set_at_index(index, value)

    def is_empty(self) -> bool:
        """
        Return True is array is empty / False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size == 0

    def length(self) -> int:
        """
        Return number of elements stored in array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return the capacity of the array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._capacity

    def print_da_variables(self) -> None:
        """
        Print information contained in the dynamic array.
        Used for testing purposes.
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        print(f"Length: {self._size}, Capacity: {self._capacity}, {self._data}")

    # -----------------------------------------------------------------------

    def resize(self, new_capacity: int) -> None:
        """
        This method changes the capacity of the underlying storage for the array elements. It does
        not change the values or the order of any elements currently stored in the dynamic array.

        The method should only accept positive integers for new_capacity. Additionally,
        new_capacity cannot be smaller than the number of elements currently stored in the
        dynamic array (which is tracked by the self._size variable). If new_capacity is not a
        positive integer or if new_capacity < self._size, this method should not do any work and
        immediately exit.
        """
        if type(new_capacity) is int and new_capacity > 0 and new_capacity >= self._size:
            # if array begins empty
            if self._size == 0:
                self._capacity = new_capacity
                self._data = StaticArray(self._capacity)
            new_static_array = StaticArray(new_capacity)
            loop_counter = 0
            # create blank new static array with the proper size
            while loop_counter != self._size:
                new_static_array.set(loop_counter, self._data.get(loop_counter))
                loop_counter += 1
            self._capacity = new_capacity
            self._data = new_static_array

    def append(self, value: object) -> None:
        """
        This method adds a new value at the end of the dynamic array.

        If the internal storage associated with the dynamic array is already full, you need to
        DOUBLE its capacity before adding a new value.
        """
        # if the array has reached it capacity, it must be doubled
        if self._size == self._capacity:
            length_of_old_array = self._capacity
            self._capacity = self._capacity * 2
            loop_counter = 0
            new_static_array = StaticArray(self._capacity)
            # fills in a temporary static array with the proper capacity
            while loop_counter < length_of_old_array:
                current_value = self._data.get(loop_counter)
                new_static_array.set(loop_counter, current_value)
                loop_counter += 1
            self._data = new_static_array
            self._size += 1
            self.set_at_index(self._size - 1, value)
        # if the array has not reached its limit
        else:
            self._size += 1
            self.set_at_index(self._size - 1, value)

    def insert_at_index(self, index: int, value: object) -> None:
        """
        This method adds a new value at the specified index in the dynamic array. Index 0 refers to
        the beginning of the array. If the provided index is invalid, the method raises a custom
        “DynamicArrayException”. Code for the exception is provided in the skeleton file. If the array
        contains N elements, valid indices for this method are [0, N] inclusive.
        If the internal storage associated with the dynamic array is already full, you need to
        DOUBLE its capacity before adding a new value (hint: you can use your already written
        resize() function for this).
        """
        # if the new value is at the end of the array
        if type(index) is int and index == self._size:
            self.append(value)
        # if the new value is somewhere within the list but not at the end
        elif type(index) is int and self._size - 1 >= index >= 0:
            if self._capacity == self._size:
                self.resize(self._capacity * 2)
            self._size += 1
            to_insert = value
            # pushing other values to the right
            while index < self._size:
                to_push_right = self._data.get(index)
                self._data.set(index, to_insert)
                index += 1
                to_insert = to_push_right
        else:
            raise DynamicArrayException()

    def remove_at_index(self, index: int) -> None:
        """
        This method removes the element at the specified index in the dynamic array. Index 0
        refers to the beginning of the array. If the provided index is invalid, the method raises a
        custom “DynamicArrayException”. Code for the exception is provided in the skeleton file. If
        the array contains N elements, valid indices for this method are [0, N - 1] inclusive.

        When the number of elements stored in the array (before removal) is STRICTLY LESS than
        ¼ of its current capacity, the capacity must be reduced to TWICE the number of current
        elements. This check / capacity adjustment must happen BEFORE removal of the element.

        If the current capacity (before reduction) is 10 elements or less, reduction should not occur
        at all. If the current capacity (before reduction) is greater than 10 elements, the reduced
        capacity cannot become less than 10 elements. Please see the examples below, especially
        example #3, for clarification.
        """
        # if removing an item necessitates lowering the capacity
        if self._size < 0.25 * self._capacity:
            new_capacity = self._size * 2
            if self._capacity >= 10:
                if new_capacity < 10:
                    self.resize(10)
                else:
                    self.resize(new_capacity)
        # If the last value in the array is being removed
        # FOR STACK POP
        if index == self.length() - 1:
            self._size -= 1
        # checks if index is valid
        elif type(index) is int and self._size - 1 >= index >= 0:
            self._size -= 1
            # pushes values to the left
            while index < self._size:
                to_push_left = self._data.get(index + 1)
                self._data.set(index, to_push_left)
                index += 1
        else:
            raise DynamicArrayException()

    def slice(self, start_index: int, size: int) -> "DynamicArray":
        """
        This method returns a new Dynamic Array object that contains the requested number of
        elements from the original array, starting with the element located at the requested start
        index. If the array contains N elements, a valid start_index is in range [0, N - 1] inclusive.
        A valid size is a non-negative integer.

        If the provided start index or size is invalid, or if there are not enough elements between
        the start index and the end of the array to make the slice of the requested size, this method
        raises a custom “DynamicArrayException”. Code for the exception is provided in the skeleton
        file.
        """
        # if the values are both valid indexes
        if type(start_index) is int and type(size) is int and start_index >= 0 and size >= 0 \
                and start_index + size <= self._size and start_index < self._size:
            new_dynamic_array = DynamicArray()
            loop_counter = 0
            # loops through the slice adding the values to a new array
            while loop_counter != size:
                value_to_add = self._data.get(start_index)
                new_dynamic_array.append(value_to_add)
                start_index += 1
                loop_counter += 1
            return new_dynamic_array
        else:
            raise DynamicArrayException

    def merge(self, second_da: "DynamicArray") -> None:
        """
        This method takes another Dynamic Array object as a parameter, and appends all elements
        from this other array onto the current one, in the same order as they are stored in the array
        parameter.
        """
        loop_counter = 0
        while loop_counter < second_da._size:
            current_value = second_da._data.get(loop_counter)
            self.append(current_value)
            loop_counter += 1

    def map(self, map_func) -> "DynamicArray":
        """
        This method creates a new Dynamic Array where the value of each element is derived by
        applying a given map_func to the corresponding value from the original array.
        """
        loop_counter = 0
        new_dynamic_array = DynamicArray()
        while loop_counter < self._size:
            original_value = self._data.get(loop_counter)
            calculated_value = map_func(original_value)
            new_dynamic_array.append(calculated_value)
            loop_counter += 1
        return new_dynamic_array

    def filter(self, filter_func) -> "DynamicArray":
        """
        This method creates a new Dynamic Array populated only with those elements from the
        original array for which filter_func returns True.
        """
        loop_counter = 0
        new_dynamic_array = DynamicArray()
        while loop_counter < self._size:
            current_value = self._data.get(loop_counter)
            if filter_func(current_value) is True:
                new_dynamic_array.append(current_value)
            loop_counter += 1
        return new_dynamic_array

    def reduce(self, reduce_func, initializer=None) -> object:
        """
        This method sequentially applies the reduce_func to all elements of the Dynamic Array, and
        returns the resulting value. It takes an optional initializer parameter. If this parameter is not
        provided, the first value in the array is used as the initializer. If the Dynamic Array is empty,
        the method returns the value of the initializer (or None, if one was not provided).
        """
        if self.is_empty() is True:
            return initializer
        # adds the first value as the initializer
        loop_counter = 0
        if initializer is None:
            initializer = self._data.get(0)
            loop_counter += 1
        # loops through calculating each value in the array
        calculated_value = initializer
        while loop_counter < self._size:
            next_value = self._data.get(loop_counter)
            calculated_value = reduce_func(calculated_value, next_value)
            loop_counter += 1
        return calculated_value

    def magic(self) -> None:
        for i in range(self._size - 1, -1, -1):
            self.append(self._data[i])
            self.remove_at_index(i)
        return





def find_mode(arr: DynamicArray) -> (DynamicArray, int):
    """
    Receives a DynamicArray that is sorted in order, either non-descending or non-ascending. The function
    will return a tuple containing (in this order) a DynamicArray comprising the mode
    (most-occurring) value/s in the array, and an integer that represents the highest frequency
    (how many times they appear).

    If there is more than one value that has the highest frequency, all values at that frequency
    should be included in the array being returned, in the order in which they appear in the
    array parameter. If there is only one mode, return a DynamicArray comprised of only that
    value.
    """
    current_index = 0
    previous_val = None
    old_repetition_counter = 0
    new_repetition_counter = 0
    new_dynamic_array = DynamicArray()
    while current_index < arr.length():
        current_val = arr.get_at_index(current_index)
        # if the value repeats at least once
        if previous_val == current_val:
            new_repetition_counter += 1
            # if the value repeats enough to be the new mode, it's recorded
            if new_repetition_counter > old_repetition_counter:
                new_dynamic_array = DynamicArray()
                new_dynamic_array.append(current_val)
                old_repetition_counter = new_repetition_counter
            elif new_repetition_counter == old_repetition_counter:
                new_dynamic_array.append(current_val)
                old_repetition_counter = new_repetition_counter
        else:
            new_repetition_counter = 0
        previous_val = current_val
        current_index += 1

    if old_repetition_counter + 1 == 1:
        new_dynamic_array = arr

    return new_dynamic_array, old_repetition_counter + 1


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# resize - example 1")
    da = DynamicArray()

    # print dynamic array's size, capacity and the contents
    # of the underlying static array (data)
    da.print_da_variables()
    da.resize(8)
    da.print_da_variables()
    da.resize(2)
    da.print_da_variables()
    da.resize(0)
    da.print_da_variables()

    print("\n# resize - example 2")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
    print(da)
    da.resize(20)
    print(da)
    da.resize(4)
    print(da)

    print("\n# append - example 1")
    da = DynamicArray()
    da.print_da_variables()
    da.append(1)
    da.print_da_variables()
    print(da)

    print("\n# append - example 2")
    da = DynamicArray()
    for i in range(9):
        da.append(i + 101)
        print(da)

    print("\n# append - example 3")
    da = DynamicArray()
    for i in range(600):
        da.append(i)
    print(da.length())
    print(da.get_capacity())

    print("\n# insert_at_index - example 1")
    da = DynamicArray([100])
    print(da)
    da.insert_at_index(0, 200)
    da.insert_at_index(0, 300)
    da.insert_at_index(0, 400)
    print(da)
    da.insert_at_index(3, 500)
    print(da)
    da.insert_at_index(1, 600)
    print(da)

    print("\n# insert_at_index example 2")
    da = DynamicArray()
    try:
        da.insert_at_index(-1, 100)
    except Exception as e:
        print("Exception raised:", type(e))
    da.insert_at_index(0, 200)
    try:
        da.insert_at_index(2, 300)
    except Exception as e:
        print("Exception raised:", type(e))
    print(da)

    print("\n# insert at index example 3")
    da = DynamicArray()
    for i in range(1, 10):
        index, value = i - 4, i * 10
        try:
            da.insert_at_index(index, value)
        except Exception as e:
            print("Cannot insert value", value, "at index", index)
    print(da)

    print("\n# remove_at_index - example 1")
    da = DynamicArray([10, 20, 30, 40, 50, 60, 70, 80])
    print(da)
    da.remove_at_index(0)
    print(da)
    da.remove_at_index(6)
    print(da)
    da.remove_at_index(2)
    print(da)

    print("\n# remove_at_index - example 2")
    da = DynamicArray([1024])
    print(da)
    for i in range(17):
        da.insert_at_index(i, i)
    print(da.length(), da.get_capacity())
    for i in range(16, -1, -1):
        da.remove_at_index(0)
    print(da)

    print("\n# remove_at_index - example 3")
    da = DynamicArray()
    print(da.length(), da.get_capacity())
    [da.append(1) for i in range(100)]  # step 1 - add 100 elements
    print(da.length(), da.get_capacity())
    [da.remove_at_index(0) for i in range(68)]  # step 2 - remove 68 elements
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 3 - remove 1 element
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 4 - remove 1 element
    print(da.length(), da.get_capacity())
    [da.remove_at_index(0) for i in range(14)]  # step 5 - remove 14 elements
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 6 - remove 1 element
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 7 - remove 1 element
    print(da.length(), da.get_capacity())

    for i in range(14):
        print("Before remove_at_index(): ", da.length(), da.get_capacity(), end="")
        da.remove_at_index(0)
        print(" After remove_at_index(): ", da.length(), da.get_capacity())

    print("\n# remove at index - example 4")
    da = DynamicArray([1, 2, 3, 4, 5])
    print(da)
    for _ in range(5):
        da.remove_at_index(0)
        print(da)

    print("\n# slice example 1")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
    da_slice = da.slice(1, 3)
    print(da, da_slice, sep="\n")
    da_slice.remove_at_index(0)
    print(da, da_slice, sep="\n")

    print("\n# slice example 2")
    da = DynamicArray([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", da)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1), (6, -1)]
    for i, cnt in slices:
        print("Slice", i, "/", cnt, end="")
        try:
            print(" --- OK: ", da.slice(i, cnt))
        except:
            print(" --- exception occurred.")

    print("\n# merge example 1")
    da = DynamicArray([1, 2, 3, 4, 5])
    da2 = DynamicArray([10, 11, 12, 13])
    print(da)
    da.merge(da2)
    print(da)

    print("\n# merge example 2")
    da = DynamicArray([1, 2, 3])
    da2 = DynamicArray()
    da3 = DynamicArray()
    da.merge(da2)
    print(da)
    da2.merge(da3)
    print(da2)
    da3.merge(da)
    print(da3)

    print("\n# map example 1")
    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    print(da.map(lambda x: x ** 2))

    print("\n# map example 2")


    def double(value):
        return value * 2


    def square(value):
        return value ** 2


    def cube(value):
        return value ** 3


    def plus_one(value):
        return value + 1


    da = DynamicArray([plus_one, double, square, cube])
    for value in [1, 10, 20]:
        print(da.map(lambda x: x(value)))

    print("\n# filter example 1")


    def filter_a(e):
        return e > 10


    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    result = da.filter(filter_a)
    print(result)
    print(da.filter(lambda x: (10 <= x <= 20)))

    print("\n# filter example 2")


    def is_long_word(word, length):
        return len(word) > length


    da = DynamicArray("This is a sentence with some long words".split())
    print(da)
    for length in [3, 4, 7]:
        print(da.filter(lambda word: is_long_word(word, length)))

    print("\n# reduce example 1")
    values = [100, 5, 10, 15, 20, 25]
    da = DynamicArray(values)
    print(da)
    print(da.reduce(lambda x, y: (x // 5 + y ** 2)))
    print(da.reduce(lambda x, y: (x + y ** 2), -1))

    print("\n# reduce example 2")
    da = DynamicArray([100])
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))
    da.remove_at_index(0)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))

    print("\n# find_mode - example 1")
    test_cases = (
        [1, 1, 2, 3, 3, 4],
        [1, 2, 3, 4, 5],
        ["Apple", "Banana", "Banana", "Carrot", "Carrot",
         "Date", "Date", "Date", "Eggplant", "Eggplant", "Eggplant",
         "Fig", "Fig", "Grape"]
    )

    for case in test_cases:
        da = DynamicArray(case)
        mode, frequency = find_mode(da)
        print(f"{da}\nMode: {mode}, Frequency: {frequency}\n")

    case = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    da = DynamicArray()
    for x in range(len(case)):
        da.append(case[x])
        mode, frequency = find_mode(da)
        print(f"{da}\nMode: {mode}, Frequency: {frequency}")
