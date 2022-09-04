# Name: Eric Hauschild
# OSU Email: hauschie@oregonstate.edu
# Course:       CS261 - Data Structures
# Assignment: #1
# Due Date: 4/19/2022
# Description: This program was written to attempt different problems at particular time complexities (almost all were
#       O(N) complexity). All of these 10 functions use a class for a static array. The functions were written by me but
#       the StaticArray class and tests were written by my instructor.

import random
from static_array import StaticArray


# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------

def min_max(arr: StaticArray) -> tuple:
    """
    Receives a one-dimensional array of integers and returns a Python
    tuple with two values - the minimum and maximum values of the input array.
    """
    num_of_items_to_test = arr.length()
    max = arr.get(num_of_items_to_test - 1)
    min = arr.get(num_of_items_to_test - 1)
    # iterates through static array object
    while num_of_items_to_test > 0:
        currently_testing = arr.get(num_of_items_to_test - 1)
        # new minimum value
        if currently_testing < min:
            min = currently_testing
        # new maximum value
        if currently_testing > max:
            max = currently_testing
        num_of_items_to_test -= 1
    min_and_max_tuple = (min, max)
    return min_and_max_tuple


# ------------------- PROBLEM 2 - FIZZ_BUZZ ---------------------------------

def fizz_buzz(arr: StaticArray) -> StaticArray:
    """
    Receives a StaticArray of integers and returns a new StaticArray object
    with the content of the original array, modified as follows:

    1) If the number in the original array is divisible by 3, the corresponding element in the
        new array will be the string ‘fizz’.
    2) If the number in the original array is divisible by 5, the corresponding element in the
        new array will be the string ‘buzz’.
    3) If the number in the original array is both a multiple of 3 and a multiple of 5, the
        corresponding element in the new array will be the string ‘fizzbuzz’.
    4) In all other cases, the element in the new array will have the same value as in the
o       original array.
    """
    num_of_items_tested = 0
    new_static_array = StaticArray(arr.length())
    index_new_array = 0
    # iterates through static array object
    while num_of_items_tested != arr.length():
        currently_testing = arr.get(num_of_items_tested)
        # tests if divisible by 3 or 5
        if currently_testing % 3 == 0 and currently_testing % 5 == 0:
            new_static_array.set(index_new_array, "fizzbuzz")
            index_new_array += 1
        elif currently_testing % 3 == 0:
            new_static_array.set(index_new_array, "fizz")
            index_new_array += 1
        elif currently_testing % 5 == 0:
            new_static_array.set(index_new_array, "buzz")
            index_new_array += 1
        # if not divisible, enters in integer value
        else:
            new_static_array.set(index_new_array, currently_testing)
            index_new_array += 1
        num_of_items_tested += 1
    return new_static_array


# ------------------- PROBLEM 3 - REVERSE -----------------------------------

def reverse(arr: StaticArray) -> None:
    """
    Receives a StaticArray and reverses the order of the elements in the
    array. The reversal must be done ‘in place’, meaning that the original input array will be
    modified, and you may not create another array (nor need to). You may assume that the
    input array will contain at least one element. You do not need to check for this condition.
    """
    loop_counter = arr.length() // 2
    current_low_num_index = 0
    current_high_num_index = arr.length() - 1
    # iterates through static array object
    while loop_counter != 0:
        # switches 2 numbers higher and lower in the index
        current_low_num = arr.get(current_low_num_index)
        current_high_num = arr.get(current_high_num_index)
        arr.set(current_low_num_index, current_high_num)
        arr.set(current_high_num_index, current_low_num)
        current_low_num_index += 1
        current_high_num_index -= 1
        loop_counter -= 1


# ------------------- PROBLEM 4 - ROTATE ------------------------------------

def rotate(arr: StaticArray, steps: int) -> StaticArray:
    """
    Receives two parameters - a StaticArray and an integer value (called
    steps). The function will create and return a new StaticArray, where all of the elements are
    from the original array, but their position has shifted right or left steps number of times.
    The original array must not be modified.

    If steps is a positive integer, the elements will be rotated to the right. Otherwise, rotation
    will be to the left. Please see the code examples below for additional details. You may
    assume that the input array will contain at least one element. You do not need to check for
    this condition.
    """
    loop_counter = arr.length()
    current_index = 0
    steps = -steps
    # finds the remainder in case it is a number higher than the array's length
    steps_remainder = steps % arr.length()
    new_static_array = StaticArray(arr.length())
    # positive integer, so elements move to the right
    if steps >= 0:
        while loop_counter != 0:
            current_number = arr.get(steps_remainder)
            new_static_array.set(current_index, current_number)
            if steps_remainder == arr.length() - 1:
                steps_remainder = 0
            else:
                steps_remainder += 1
            current_index += 1
            loop_counter -= 1
    # negative integer, so elements move to the left
    elif steps < 0:
        while loop_counter != 0:
            current_number = arr.get(steps_remainder)
            new_static_array.set(current_index, current_number)
            if steps_remainder == arr.length() - 1:
                steps_remainder = 0
            else:
                steps_remainder += 1
            current_index += 1
            loop_counter -= 1
    return new_static_array


# ------------------- PROBLEM 5 - SA_RANGE ----------------------------------

def sa_range(start: int, end: int) -> StaticArray:
    """
    Write a function that receives two integers start and end, and returns a StaticArray that
    contains all the consecutive integers between start and end (inclusive).
    """
    current_number = start
    current_index = 0
    loop_counter = abs(end - start)
    new_static_array = StaticArray(loop_counter + 1)
    while loop_counter >= 0:
        new_static_array.set(current_index, current_number)
        # determines whether to increment down or up
        if end >= start:
            current_number += 1
        else:
            current_number -= 1
        current_index += 1
        loop_counter -= 1
    return new_static_array


# ------------------- PROBLEM 6 - IS_SORTED ---------------------------------

def is_sorted(arr: StaticArray) -> int:
    """
    Receives a StaticArray and returns an integer that describes whether
    the array is sorted. The method must return:
        ● 1 if the array is sorted in strictly ascending order.
        ● -1 if the list is sorted in strictly descending order.
        ● 0 otherwise.

    Arrays consisting of a single element are considered sorted in strictly ascending order.
    """
    current_index = 1
    order = 2
    previous_val = arr.get(0)
    # order is automatically 1
    if arr.length() == 1:
        order = 1
        return order
    else:
        while current_index != arr.length():
            current_val = arr.get(current_index)
            if type(current_val) == type(previous_val):
                # 1 if the array is sorted in strictly ascending order
                if current_val > previous_val and (order == 1 or order == 2):
                    order = 1
                # -1 if the list is sorted in strictly descending order
                elif current_val < previous_val and (order == -1 or order == 2):
                    order = -1
                # 0 otherwise
                else:
                    order = 0
                    break
            else:
                order = 0
                break
            previous_val = current_val
            current_index += 1
        return order

# ------------------- PROBLEM 7 - FIND_MODE -----------------------------------

def find_mode(arr: StaticArray) -> tuple:
    """
    Receives a StaticArray that is sorted in order, either non-descending or
    non-ascending. The function will return, in this order, the mode (most-occurring value) of
    the array, and its frequency (how many times it appears).
    If there is more than one value that has the highest frequency, select the one that occurs
    first in the array.
    """
    current_index = 1
    previous_val = arr.get(0)
    old_repetition_counter = 0
    new_repetition_counter = 0
    current_mode = arr.get(0)
    while current_index != arr.length():
        current_val = arr.get(current_index)
        # if the value repeats at least once
        if previous_val == current_val:
            new_repetition_counter += 1
            # if the value repeats enough to be the new mode, it's recorded
            if new_repetition_counter > old_repetition_counter:
                current_mode = current_val
                old_repetition_counter = new_repetition_counter
        else:
            new_repetition_counter = 0
        previous_val = current_val
        current_index += 1
    return (current_mode, old_repetition_counter + 1)

# ------------------- PROBLEM 8 - REMOVE_DUPLICATES -------------------------

def remove_duplicates(arr: StaticArray) -> StaticArray:
    """
    Receives a StaticArray where the elements are already in sorted order,
    and returns a new StaticArray with all duplicate values removed. The original array must not
    be modified.
    """
    current_index = 1
    previous_val = arr.get(0)
    length_of_final_array = 1
    new_static_array = StaticArray(arr.length())
    first_value = arr.get(0)
    new_static_array.set(0, first_value)
    while current_index < arr.length():
        current_val = arr.get(current_index)
        # if there's a duplicate
        if previous_val == current_val:
            previous_val = current_val
            current_index += 1
        # otherwise the data is recorded in the new array
        else:
            new_static_array.set(length_of_final_array, current_val)
            length_of_final_array += 1
            previous_val = current_val
            current_index += 1
    if length_of_final_array == 0:
        final_static_array = StaticArray(1)
    else:
        final_static_array = StaticArray(length_of_final_array)
    current_index = 0
    previous_val = new_static_array.get(0)
    # second loop is necessary because the length of final array is now known, so it can be properly initialized
    while current_index <= length_of_final_array - 1:
        current_val = new_static_array.get(current_index)
        final_static_array.set(current_index, current_val)
        previous_val = current_val
        current_index += 1
    return final_static_array


# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------

def count_sort(arr: StaticArray) -> StaticArray:
    """
    Receives a StaticArray and returns a new StaticArray with the same
    content sorted in non-ascending order, using the count sort algorithm. The original array
    must not be modified.
    """
    min_and_max = min_max(arr)
    loop_counter = 0
    min = min_and_max[0]
    max = min_and_max[1]
    max_minus_min = abs(max - min) + 1
    array_of_entire_range = StaticArray(max_minus_min)
    new_static_array = StaticArray(arr.length())
    current_index = 0
    # creates a preliminary array for counting the number of times each integer appears in the unsorted array
    while current_index < arr.length():
        current_value = arr.get(current_index)
        other_index = current_value - min
        repeated_instances = array_of_entire_range.get(other_index)
        if type(repeated_instances) is not int:
            repeated_instances = 0
        repeated_instances += 1
        array_of_entire_range.set(other_index, repeated_instances)
        current_index += 1
    current_index = 0
    index_for_new_array = arr.length() - 1
    # filling in the final array using the array_of_entire_range
    while current_index < array_of_entire_range.length():
        current_value = array_of_entire_range.get(current_index)
        if type(current_value) is int and current_value > 0:
            new_value = min + current_index
            new_static_array.set(index_for_new_array, new_value)
            array_of_entire_range.set(current_index, current_value - 1)
            index_for_new_array -= 1
        else:
            current_index += 1
    return new_static_array


# ------------------- PROBLEM 10 - SORTED SQUARES ---------------------------

def sorted_squares(arr: StaticArray) -> StaticArray:
    """
    Receives a StaticArray where the elements are in sorted order, and
    returns a new StaticArray with squares of the values from the original array, sorted in
    non-descending order. The original array should not be modified.
    """
#    loop_counter = arr.length() - 1
#    new_squared_array = StaticArray(arr.length())
#    first_negative = -1
#    while loop_counter >= 0:
#        current_num = arr.get(loop_counter)
#        if current_num <= 0:
#            first_negative = loop_counter
#            break
#        loop_counter -= 1
#    pos_loop_counter = 1
#    loop_counter = arr.length() - 1
#    if first_negative == -1:
#        loop_counter = 0
#        while loop_counter < arr.length():
#            current_num = arr.get(loop_counter)
#            value_to_add = current_num ** 2
#            new_squared_array.set(loop_counter, value_to_add)
#    while first_negative >= 0:
#        if pos_loop_counter + first_negative != arr.length:
#            current_neg_number = arr.get(first_negative)
#            current_pos_number = arr.get(first_negative + pos_loop_counter)
#            if abs(current_neg_number) >= current_pos_number:
#                value_to_add = current_neg_number ** 2
#                new_squared_array.set(first_negative, value_to_add)
#                loop_counter -= 1
#            else:
#                value_to_add = current_pos_number ** 2
#                new_squared_array.set(pos_loop_counter, value_to_add)
#                pos_loop_counter += 1
#    return new_squared_array


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print('\n# min_max example 1')
    arr = StaticArray(5)
    for i, value in enumerate([7, 8, 6, -5, 4]):
        arr[i] = value
    print(arr)
    result = min_max(arr)
    print(f"Min: {result[0]: 3}, Max: {result[1]: 3}")

    print('\n# min_max example 2')
    arr = StaticArray(1)
    arr[0] = 100
    print(arr)
    result = min_max(arr)
    print(f"Min: {result[0]}, Max: {result[1]}")

    print('\n# min_max example 3')
    test_cases = (
        [3, 3, 3],
        [-10, -30, -5, 0, -10],
        [25, 50, 0, 10],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        result = min_max(arr)
        print(f"Min: {result[0]: 3}, Max: {result[1]}")

    print('\n# fizz_buzz example 1')
    source = [_ for _ in range(-5, 20, 4)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(fizz_buzz(arr))
    print(arr)

    print('\n# reverse example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    reverse(arr)
    print(arr)
    reverse(arr)
    print(arr)

    print('\n# rotate example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    for steps in [1, 2, 0, -1, -2, 28, -100, 2 ** 28, -2 ** 31]:
        space = " " if steps >= 0 else ""
        print(f"{rotate(arr, steps)} {space}{steps}")
    print(arr)

    print('\n# rotate example 2')
    array_size = 1_000_000
    source = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(f'Started rotating large array of {array_size} elements')
    rotate(arr, 3 ** 14)
    rotate(arr, -3 ** 15)
    print(f'Finished rotating large array of {array_size} elements')

    print('\n# sa_range example 1')
    cases = [
        (1, 3), (-1, 2), (0, 0), (0, -3),
        (-95, -89), (-89, -95)]
    for start, end in cases:
        print(f"Start: {start: 4}, End: {end: 4}, {sa_range(start, end)}")

    print('\n# is_sorted example 1')
    test_cases = (
        [-100, -8, 0, 2, 3, 10, 20, 100],
        ['A', 'B', 'Z', 'a', 'z'],
        ['Z', 'T', 'K', 'A', '5'],
        [1, 3, -10, 20, -30, 0],
        [-10, 0, 0, 10, 20, 30],
        [100, 90, 0, -90, -200],
        ['apple']
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        result = is_sorted(arr)
        space = "  " if result >= 0 else " "
        print(f"Result:{space}{result}, {arr}")

    print('\n# find_mode example 1')
    test_cases = (
        [1, 20, 30, 40, 500, 500, 500],
        [2, 2, 2, 2, 1, 1, 1, 1],
        ["zebra", "sloth", "otter", "otter", "moose", "koala"],
        ["Albania", "Belgium", "Chile", "Denmark", "Egypt", "Fiji"]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value

        mode, frequency = find_mode(arr)
        print(f"{arr}\nMode: {mode}, Frequency: {frequency}\n")

    print('# remove_duplicates example 1')
    test_cases = (
        [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
        [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        print(remove_duplicates(arr))
    print(arr)

    print('\n# count_sort example 1')
    test_cases = (
        [1, 2, 4, 3, 5], [5, 4, 3, 2, 1], [0, -5, -3, -4, -2, -1, 0],
        [-3, -2, -1, 0, 1, 2, 3], [1, 2, 3, 4, 3, 2, 1, 5, 5, 2, 3, 1],
        [10100, 10721, 10320, 10998], [-100320, -100450, -100999, -100001],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        before = arr if len(case) < 50 else 'Started sorting large array'
        print(f"Before: {before}")
        result = count_sort(arr)
        after = result if len(case) < 50 else 'Finished sorting large array'
        print(f"After : {after}")

    print('\n# count_sort example 2')
    array_size = 5_000_000
    min_val = random.randint(-1_000_000_000, 1_000_000_000 - 998)
    max_val = min_val + 998
    case = [random.randint(min_val, max_val) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(case):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = count_sort(arr)
    print(f'Finished sorting large array of {array_size} elements')

    print('\n# sorted_squares example 1')
    test_cases = (
        [1, 2, 3, 4, 5],
        [-5, -4, -3, -2, -1, 0],
        [-3, -2, -2, 0, 1, 2, 3],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(sorted(case)):
            arr[i] = value
        print(arr)
        result = sorted_squares(arr)
        print(result)

    print('\n# sorted_squares example 2')
    array_size = 5_000_000
    case = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(sorted(case)):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = sorted_squares(arr)
    print(f'Finished sorting large array of {array_size} elements')
