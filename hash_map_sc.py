# Name: Eric Hauschild
# OSU Email: hauschie@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 6
# Due Date: 6/4/2022
# Description: This program contains a hash map which uses the  separate chaining method.


from a6_include import (DynamicArray, LinkedList,
                        hash_function_1, hash_function_2)


class HashMap:
    def __init__(self, capacity: int, function) -> None:
        """
        Initialize new HashMap that uses
        separate chaining for collision resolution
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._buckets = DynamicArray()
        for _ in range(capacity):
            self._buckets.append(LinkedList())

        self._capacity = capacity
        self._hash_function = function
        self._size = 0

    def __str__(self) -> str:
        """
        Override string method to provide more readable output
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = ''
        for i in range(self._buckets.length()):
            out += str(i) + ': ' + str(self._buckets[i]) + '\n'
        return out

    def get_size(self) -> int:
        """
        Return size of map
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return capacity of map
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._capacity

    # ------------------------------------------------------------------ #

    def put(self, key: str, value: object) -> None:
        """
        This method updates the key / value pair in the hash map. If the given key already exists in
        the hash map, its associated value must be replaced with the new value. If the given key is
        not in the hash map, a key / value pair must be added.
        """
        hash_value = self._hash_function(key)
        index_value = hash_value % self._capacity
        link_1 = self._buckets[index_value]
        if link_1.contains(key) is not None:
            link_1.remove(key)
            link_1.insert(key, value)
        else:
            if link_1 is None:
                link_1.insert(key, value)
            else:
                link_1.insert(key, value)
                self._size += 1

    def put_for_mode(self, key: str, value: object) -> None:
        """
        **For Mode**
        This method updates the key / value pair in the hash map. If the given key already exists in
        the hash map, its associated value must be replaced with the new value. If the given key is
        not in the hash map, a key / value pair must be added.
        """
        hash_value = self._hash_function(key)
        index_value = hash_value % self._capacity
        link_1 = self._buckets[index_value]
        if link_1.contains(key) is not None:
            val_1 = link_1.contains(key).value
            link_1.remove(key)
            link_1.insert(key, val_1 + 1)
        else:
            if link_1 is None:
                link_1.insert(key, value)
            else:
                link_1.insert(key, value)
                self._size += 1

    def empty_buckets(self) -> int:
        """
        This method returns the number of empty buckets in the hash table.
        """
        index_counter = 0
        number_of_empty_buckets = 0
        while index_counter != self._capacity:
            current_value = self._buckets.get_at_index(index_counter)
            if current_value.length() == 0:
                number_of_empty_buckets += 1
            index_counter += 1
        return number_of_empty_buckets


    def table_load(self) -> float:
        """
        This method returns the current hash table load factor.
        """
        load_factor = self.get_size() / self._capacity
        return load_factor

    def clear(self) -> None:
        """
        This method clears the contents of the hash map. It does not change the underlying hash
        table capacity.
        """
        self._buckets = DynamicArray()
        for _ in range(self._capacity):
            self._buckets.append(LinkedList())
        self._size = 0


    def resize_table(self, new_capacity: int) -> None:
        """
        This method changes the capacity of the internal hash table. All existing key / value pairs
        must remain in the new hash map, and all hash table links must be rehashed. If
        new_capacity is less than 1, the method does nothing.
        """
        if new_capacity < 1:
            pass
        else:
            new_array = DynamicArray()
            for _ in range(new_capacity):
                new_array.append(LinkedList())
            array_counter = 0
            while array_counter < self._capacity:
                linked_list_val = self._buckets.get_at_index(array_counter)
                if linked_list_val is not None:
                    for node_1 in linked_list_val:
                        key_1 = node_1.key
                        hash_value = self._hash_function(key_1)
                        index_value = hash_value % new_capacity
                        link_1 = new_array[index_value]
                        link_1.insert(node_1.key, node_1.value)
                array_counter += 1
            self._buckets = new_array
            self._capacity = new_capacity

    def get(self, key: str) -> object:
        """
        This method returns the value associated with the given key. If the key is not in the hash
        map, the method returns None.
        """
        index_counter = 0
        while index_counter != self._capacity:
            current_value = self._buckets.get_at_index(index_counter)
            if self.contains_key(key) is True:
                node_value = current_value.contains(key)
                if node_value is not None:
                    return node_value.value
            index_counter += 1
        return None

    def contains_key(self, key: str) -> bool:
        """
        This method returns True if the given key is in the hash map, otherwise it returns False. An
        empty hash map does not contain any keys.
        """
        index_counter = 0
        while index_counter != self._capacity:
            current_value = self._buckets.get_at_index(index_counter)
            if current_value.contains(key) is not None:
                return True
            index_counter += 1
        return False

    def remove(self, key: str) -> None:
        """
        This method removes the given key and its associated value from the hash map. If the key
        is not in the hash map, the method does nothing (no exception needs to be raised).
        """
        index_counter = 0
        while index_counter != self._capacity:
            current_value = self._buckets.get_at_index(index_counter)
            if current_value.contains(key) is not None:
                current_value.remove(key)
                self._size -= 1
            index_counter += 1

    def get_keys(self) -> DynamicArray:
        """
        This method returns a DynamicArray that contains all the keys stored in the hash map. The
        order of the keys in the DA does not matter.
        """
        new_array = DynamicArray()
        array_counter = 0
        while array_counter < self._capacity:
            linked_list_val = self._buckets.get_at_index(array_counter)
            if linked_list_val is not None:
                for node_1 in linked_list_val:
                    key_1 = node_1.key
                    new_array.append(key_1)
            array_counter += 1
        return new_array


def find_mode(da: DynamicArray) -> (DynamicArray, int):
    """
    Write a standalone function outside of the HashMap class that receives a DynamicArray
    (that is not guaranteed to be sorted). This function will return a tuple containing, in this
    order, a DynamicArray comprising the mode (most occurring) value/s of the array, and an
    integer that represents the highest frequency (how many times they appear).
    If there is more than one value with the highest frequency, all values at that frequency
    should be included in the array being returned (the order does not matter). If there is only
    one mode, return a DynamicArray comprised of only that value.
    You may assume that the input array will contain at least one element, and that all values
    stored in the array will be strings. You do not need to write checks for these conditions.
    For full credit, the function must be implemented with O(N) time complexity. For best
    results, we recommend using the separate chaining HashMap provided for you in the
    function’s skeleton code.
    """
    # if you'd like to use a hash map,
    # use this instance of your Separate Chaining HashMap
    map = HashMap(da.length(), hash_function_1)
    array_counter = 0
    while array_counter < da.length():
        current_val = da.get_at_index(array_counter)
        map.put_for_mode(current_val, 1)
        array_counter += 1
    da_of_all_keys = map.get_keys()
    new_array = DynamicArray()
    array_counter = -1
    current_highest_node = 0
    amount_of_repeats = 0
    while array_counter < da_of_all_keys.length() - 1:
        array_counter += 1
        current_arr_val = da_of_all_keys.get_at_index(array_counter)
        if current_arr_val is not None:
            current_node = map.get(current_arr_val)
            if current_node is not None:
                if current_node > current_highest_node:
                    new_array = DynamicArray()
                    amount_of_repeats = current_node
                    new_array.append(current_arr_val)
                    current_highest_node = current_node
                elif current_node == amount_of_repeats:
                    new_array.append(current_arr_val)
    return (new_array, amount_of_repeats)


# ------------------- BASIC TESTING ---------------------------------------- #

if __name__ == "__main__":

    print("\nPDF - put example 1")
    print("-------------------")
    m = HashMap(50, hash_function_1)
    for i in range(150):
        m.put('str' + str(i), i * 100)
        if i % 25 == 24:
            print(m.empty_buckets(), m.table_load(), m.get_size(), m.get_capacity())

    print("\nPDF - put example 2")
    print("-------------------")
    m = HashMap(40, hash_function_2)
    for i in range(50):
        m.put('str' + str(i // 3), i * 100)
        if i % 10 == 9:
            print(m.empty_buckets(), m.table_load(), m.get_size(), m.get_capacity())

    print("\nPDF - empty_buckets example 1")
    print("-----------------------------")
    m = HashMap(100, hash_function_1)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key1', 10)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key2', 20)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key1', 30)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key4', 40)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())

    print("\nPDF - empty_buckets example 2")
    print("-----------------------------")
    m = HashMap(50, hash_function_1)
    for i in range(150):
        m.put('key' + str(i), i * 100)
        if i % 30 == 0:
            print(m.empty_buckets(), m.get_size(), m.get_capacity())

    print("\nPDF - table_load example 1")
    print("--------------------------")
    m = HashMap(100, hash_function_1)
    print(m.table_load())
    m.put('key1', 10)
    print(m.table_load())
    m.put('key2', 20)
    print(m.table_load())
    m.put('key1', 30)
    print(m.table_load())

    print("\nPDF - table_load example 2")
    print("--------------------------")
    m = HashMap(50, hash_function_1)
    for i in range(50):
        m.put('key' + str(i), i * 100)
        if i % 10 == 0:
            print(m.table_load(), m.get_size(), m.get_capacity())

    print("\nPDF - clear example 1")
    print("---------------------")
    m = HashMap(100, hash_function_1)
    print(m.get_size(), m.get_capacity())
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key1', 30)
    print(m.get_size(), m.get_capacity())
    m.clear()
    print(m.get_size(), m.get_capacity())

    print("\nPDF - clear example 2")
    print("---------------------")
    m = HashMap(50, hash_function_1)
    print(m.get_size(), m.get_capacity())
    m.put('key1', 10)
    print(m.get_size(), m.get_capacity())
    m.put('key2', 20)
    print(m.get_size(), m.get_capacity())
    m.resize_table(100)
    print(m.get_size(), m.get_capacity())
    m.clear()
    print(m.get_size(), m.get_capacity())

    print("\nPDF - resize example 1")
    print("----------------------")
    m = HashMap(20, hash_function_1)
    m.put('key1', 10)
    print(m.get_size(), m.get_capacity(), m.get('key1'), m.contains_key('key1'))
    m.resize_table(30)
    print(m.get_size(), m.get_capacity(), m.get('key1'), m.contains_key('key1'))

    print("\nPDF - resize example 2")
    print("----------------------")
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(1, 1000, 13)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.get_size(), m.get_capacity())

    for capacity in range(111, 1000, 117):
        m.resize_table(capacity)

        m.put('some key', 'some value')
        result = m.contains_key('some key')
        m.remove('some key')

        for key in keys:
            # all inserted keys must be present
            result &= m.contains_key(str(key))
            # NOT inserted keys must be absent
            result &= not m.contains_key(str(key + 1))
        print(capacity, result, m.get_size(), m.get_capacity(), round(m.table_load(), 2))

    print("\nPDF - get example 1")
    print("-------------------")
    m = HashMap(30, hash_function_1)
    print(m.get('key'))
    m.put('key1', 10)
    print(m.get('key1'))

    print("\nPDF - get example 2")
    print("-------------------")
    m = HashMap(150, hash_function_2)
    for i in range(200, 300, 7):
        m.put(str(i), i * 10)
    print(m.get_size(), m.get_capacity())
    for i in range(200, 300, 21):
        print(i, m.get(str(i)), m.get(str(i)) == i * 10)
        print(i + 1, m.get(str(i + 1)), m.get(str(i + 1)) == (i + 1) * 10)

    print("\nPDF - contains_key example 1")
    print("----------------------------")
    m = HashMap(10, hash_function_1)
    print(m.contains_key('key1'))
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key3', 30)
    print(m.contains_key('key1'))
    print(m.contains_key('key4'))
    print(m.contains_key('key2'))
    print(m.contains_key('key3'))
    m.remove('key3')
    print(m.contains_key('key3'))

    print("\nPDF - contains_key example 2")
    print("----------------------------")
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(1, 1000, 20)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.get_size(), m.get_capacity())
    result = True
    for key in keys:
        # all inserted keys must be present
        result &= m.contains_key(str(key))
        # NOT inserted keys must be absent
        result &= not m.contains_key(str(key + 1))
    print(result)

    print("\nPDF - remove example 1")
    print("----------------------")
    m = HashMap(50, hash_function_1)
    print(m.get('key1'))
    m.put('key1', 10)
    print(m.get('key1'))
    m.remove('key1')
    print(m.get('key1'))
    m.remove('key4')

    print("\nPDF - get_keys example 1")
    print("------------------------")
    m = HashMap(10, hash_function_2)
    for i in range(100, 200, 10):
        m.put(str(i), str(i * 10))
    print(m.get_keys())

    m.resize_table(1)
    print(m.get_keys())

    m.put('200', '2000')
    m.remove('100')
    m.resize_table(2)
    print(m.get_keys())

    print("\nPDF - find_mode example 1")
    print("-----------------------------")
    da = DynamicArray(["apple", "apple", "grape", "melon", "melon", "peach"])
    map = HashMap(da.length() // 3, hash_function_1)
    mode, frequency = find_mode(da)
    print(f"Input: {da}\nMode: {mode}, Frequency: {frequency}")

    print("\nPDF - find_mode example 2")
    print("-----------------------------")
    test_cases = (
        ["Arch", "Manjaro", "Manjaro", "Mint", "Mint", "Mint", "Ubuntu", "Ubuntu", "Ubuntu", "Ubuntu"],
        ["one", "two", "three", "four", "five"],
        ["2", "4", "2", "6", "8", "4", "1", "3", "4", "5", "7", "3", "3", "2"]
    )

    for case in test_cases:
        da = DynamicArray(case)
        map = HashMap(da.length() // 3, hash_function_2)
        mode, frequency = find_mode(da)
        print(f"Input: {da}\nMode: {mode}, Frequency: {frequency}\n")
