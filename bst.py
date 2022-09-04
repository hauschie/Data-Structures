# Name: Eric Hauschild
# OSU Email: hauschie@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 4
# Due Date: 5/19/2022
# Description: This program contains the class for a binary search tree with methods that I created.


import random
from queue_and_stack import Queue, Stack


class BSTNode:
    """
    Binary Search Tree Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, value: object) -> None:
        """
        Initialize a new BST node
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.value = value   # to store node's data
        self.left = None     # pointer to root of left subtree
        self.right = None    # pointer to root of right subtree

    def __str__(self) -> str:
        """
        Override string method
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'BST Node: {}'.format(self.value)


class BST:
    """
    Binary Search Tree class
    """

    def __init__(self, start_tree=None) -> None:
        """
        Initialize new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._root = None

        # populate BST with initial values (if provided)
        # before using this feature, implement add() method
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of BST in human-readable form using pre-order traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        self._str_helper(self._root, values)
        return "BST pre-order { " + ", ".join(values) + " }"

    def _str_helper(self, node: BSTNode, values: []) -> None:
        """
        Helper method for __str__. Does pre-order tree traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if not node:
            return
        values.append(str(node.value))
        self._str_helper(node.left, values)
        self._str_helper(node.right, values)

    def get_root(self) -> BSTNode:
        """
        Return root of tree, or None if empty
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._root

    def is_valid_bst(self) -> bool:
        """
        Perform pre-order traversal of the tree.
        Return False if nodes don't adhere to the bst ordering property.
        This is intended to be a troubleshooting 'helper' method to help
        find any inconsistencies in the tree after the add() or remove()
        operations. Review the code to understand what this method is
        checking and how it determines whether the BST tree is correct.
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        stack = Stack()
        stack.push(self._root)
        while not stack.is_empty():
            node = stack.pop()
            if node:
                if node.left and node.left.value >= node.value:
                    return False
                if node.right and node.right.value < node.value:
                    return False
                stack.push(node.right)
                stack.push(node.left)
        return True

    # ------------------------------------------------------------------ #

    def add(self, value: object) -> None:
        """
        This method adds a new value to the tree. Duplicate values are allowed. If a node with
        that value is already in the tree, the new value should be added to the right
        subtree of that node. It must be implemented with O(N) runtime complexity.
        """
        if self._root is None:
            self._root = BSTNode(value)
        else:
            current_node = self._root
            last_current_node = self._root
            while current_node is not None:
                last_current_node = current_node
                if value < current_node.value:
                    current_node = current_node.left
                else:
                    current_node = current_node.right
            if value < last_current_node.value:
                last_current_node.left = BSTNode(value)
            else:
                last_current_node.right = BSTNode(value)


    def remove(self, value: object) -> bool:
        """
        This method removes a value from the tree. The method returns True if the value is
        removed; otherwise, it returns False. It must be implemented with O(N) runtime complexity.
        """
        if self._root is None:
            return False
        else:
            current_node = self._root
            last_current_node = self._root
            if self._root.value != value:
                if value < current_node.value:
                    current_node = current_node.left
                    direction_down = "left"
                else:
                    current_node = current_node.right
                    direction_down = "right"
            # locate the current node
            while current_node.value != value:
                last_current_node = current_node
                if value < current_node.value:
                    current_node = current_node.left
                    direction_down = "left"
                else:
                    current_node = current_node.right
                    direction_down = "right"
                if current_node is None:
                    return False
            if current_node.value == value:
                if current_node.left is None and current_node.right is None:
                    if current_node == self._root:
                        self._root = None
                    elif direction_down == "right":
                        last_current_node.right = None
                    else:
                        last_current_node.left = None
                elif current_node.left is not None and current_node.right is None:
                    if current_node == self._root:
                        self._root = current_node.left
                    elif direction_down == "right":
                        last_current_node.right = current_node.left
                    else:
                        last_current_node.left = current_node.left
                elif current_node.left is None and current_node.right is not None:
                    if current_node == self._root:
                        self._root = current_node.right
                    elif direction_down == "right":
                        last_current_node.right = current_node.right
                    else:
                        last_current_node.left = current_node.right
                else:
                    secondary_current_node = current_node.right
                    last_secondary_current_node = current_node.right
                    while secondary_current_node is not None:
                        last_secondary_current_node = secondary_current_node
                        secondary_current_node = secondary_current_node.left
                    if secondary_current_node is not None:
                        if direction_down == "right":
                            last_current_node.right = BSTNode(secondary_current_node.value)
                            last_current_node.right.left = secondary_current_node.left
                            last_current_node.right.right = secondary_current_node.right
                        else:
                            last_current_node.left = BSTNode(secondary_current_node.value)
                            last_current_node.left.left = secondary_current_node.left
                            last_current_node.left.right = secondary_current_node.right
                    last_secondary_current_node.left = None
                return True


    # Consider implementing methods that handle different removal scenarios. #
    # Remove these comments.                                                 #
    # Remove these method stubs if you decide not to use them.               #
    # Change these methods in any way you'd like.                            #

    def _remove_no_subtrees(self, parent: BSTNode, node: BSTNode) -> None:
        """
        TODO: Write your implementation
        """
        # remove node that has no subtrees (no left or right nodes)
        pass

    def _remove_one_subtree(self, parent: BSTNode, node: BSTNode) -> None:
        """
        TODO: Write your implementation
        """
        # remove node that has a left or right subtree (only)
        pass

    def _remove_two_subtrees(self, parent: BSTNode, node: BSTNode) -> None:
        """
        TODO: Write your implementation
        """
        # remove node that has two subtrees
        # need to find inorder successor and its parent (make a method!)
        pass

    def contains(self, value: object) -> bool:
        """
        This method returns True if the value is in the tree; otherwise, it returns False. If the tree is
        empty, the method should return False. It must be implemented with O(N) runtime
        complexity.
        """
        current_node = self._root
        while current_node is not None and current_node.value != value:
            if value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        if current_node is not None and current_node.value == value:
            return True
        else:
            return False

    def inorder_traversal(self) -> Queue:
        """
        This method will perform an inorder traversal of the tree, and return a Queue object that
        contains the values of the visited nodes, in the order they were visited. If the tree is empty,
        the method returns an empty Queue. It must be implemented with O(N) runtime
        complexity.
        """
        queue_to_return = Queue()
        stack_of_values_to_check = Stack()
        if self.is_empty() is True:
            return queue_to_return
        else:
            current_node = self._root
            stack_of_values_to_check.push(current_node)
            root_added = False
            while stack_of_values_to_check.is_empty() is False:
                if current_node is not None:
                    stack_of_values_to_check.push(current_node)
                    current_node = current_node.left
                else:
                    take_from_stack = stack_of_values_to_check.pop()
                    if take_from_stack is self._root:
                        if root_added is False:
                            queue_to_return.enqueue(take_from_stack.value)
                            root_added = True
                    else:
                        queue_to_return.enqueue(take_from_stack.value)
                    current_node = take_from_stack
                    if current_node.right is not None:
                        current_node = take_from_stack.right
                    else:
                        current_node = None
            return queue_to_return


    def find_min(self) -> object:
        """
        This method returns the lowest value in the tree. If the tree is empty, the method should
        return None. It must be implemented with O(N) runtime complexity.
        """
        if self.is_empty() is True:
            return None
        else:
            current_node = self._root
            last_current_node = self._root
            while current_node is not None:
                last_current_node = current_node
                current_node = current_node.left
            return last_current_node.value

    def find_max(self) -> object:
        """
        This method returns the highest value in the tree. If the tree is empty, the method should
        return None. It must be implemented with O(N) runtime complexity.
        """
        if self.is_empty() is True:
            return None
        else:
            current_node = self._root
            last_current_node = self._root
            while current_node is not None:
                last_current_node = current_node
                current_node = current_node.right
            return last_current_node.value

    def is_empty(self) -> bool:
        """
        This method returns True if the tree is empty; otherwise, it returns False. It must be
        implemented with O(1) runtime complexity.
        """
        if self._root is None:
            return True
        else:
            return False

    def make_empty(self) -> None:
        """
        This method removes all of the nodes from the tree. It must be implemented with O(1)
        runtime complexity.
        """
        self._root = None


# ------------------- BASIC TESTING -----------------------------------------

if __name__ == '__main__':

    print("\nPDF - method add() example 1")
    print("----------------------------")
    test_cases = (
        (1, 2, 3),
        (3, 2, 1),
        (1, 3, 2),
        (3, 1, 2),
    )
    for case in test_cases:
        tree = BST(case)
        print(tree)

    print("\nPDF - method add() example 2")
    print("----------------------------")
    test_cases = (
        (10, 20, 30, 40, 50),
        (10, 20, 30, 50, 40),
        (30, 20, 10, 5, 1),
        (30, 20, 10, 1, 5),
        (5, 4, 6, 3, 7, 2, 8),
        (range(0, 30, 3)),
        (range(0, 31, 3)),
        (range(0, 34, 3)),
        (range(10, -10, -2)),
        ('A', 'B', 'C', 'D', 'E'),
        (1, 1, 1, 1),
    )
    for case in test_cases:
        tree = BST(case)
        print('INPUT  :', case)
        print('RESULT :', tree)

    print("\nPDF - method add() example 3")
    print("----------------------------")
    for _ in range(100):
        case = list(set(random.randrange(1, 20000) for _ in range(900)))
        tree = BST()
        for value in case:
            tree.add(value)
        if not tree.is_valid_bst():
            raise Exception("PROBLEM WITH ADD OPERATION")
    print('add() stress test finished')

    print("\nPDF - method remove() example 1")
    print("-------------------------------")
    test_cases = (
        ((1, 2, 3), 1),
        ((1, 2, 3), 2),
        ((1, 2, 3), 3),
        ((50, 40, 60, 30, 70, 20, 80, 45), 0),
        ((50, 40, 60, 30, 70, 20, 80, 45), 45),
        ((50, 40, 60, 30, 70, 20, 80, 45), 40),
        ((50, 40, 60, 30, 70, 20, 80, 45), 30),
    )
    for case, del_value in test_cases:
        tree = BST(case)
        print('INPUT  :', tree, "DEL:", del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 2")
    print("-------------------------------")
    test_cases = (
        ((50, 40, 60, 30, 70, 20, 80, 45), 20),
        ((50, 40, 60, 30, 70, 20, 80, 15), 40),
        ((50, 40, 60, 30, 70, 20, 80, 35), 20),
        ((50, 40, 60, 30, 70, 20, 80, 25), 40),
    )
    for case, del_value in test_cases:
        tree = BST(case)
        print('INPUT  :', tree, "DEL:", del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 3")
    print("-------------------------------")
    case = range(-9, 16, 2)
    tree = BST(case)
    for del_value in case:
        print('INPUT  :', tree, del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 4")
    print("-------------------------------")
    case = range(0, 34, 3)
    tree = BST(case)
    for _ in case[:-2]:
        root_value = tree.get_root().value
        print('INPUT  :', tree, root_value)
        tree.remove(root_value)
        if not tree.is_valid_bst():
            raise Exception("PROBLEM WITH REMOVE OPERATION")
        print('RESULT :', tree)

    print("\nPDF - method contains() example 1")
    print("---------------------------------")
    tree = BST([10, 5, 15])
    print(tree.contains(15))
    print(tree.contains(-10))
    print(tree.contains(15))

    print("\nPDF - method contains() example 2")
    print("---------------------------------")
    tree = BST()
    print(tree.contains(0))

    print("\nPDF - method inorder_traversal() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree.inorder_traversal())

    print("\nPDF - method inorder_traversal() example 2")
    print("---------------------------------")
    tree = BST([8, 10, -4, 5, -1])
    print(tree.inorder_traversal())

    print("\nPDF - method find_min() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_min() example 2")
    print("---------------------------------")
    tree = BST([8, 10, -4, 5, -1])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_max() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method find_max() example 2")
    print("---------------------------------")
    tree = BST([8, 10, -4, 5, -1])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method is_empty() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method is_empty() example 2")
    print("---------------------------------")
    tree = BST()
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method make_empty() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)

    print("\nPDF - method make_empty() example 2")
    print("---------------------------------")
    tree = BST()
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)
