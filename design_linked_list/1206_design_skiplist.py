"""
LeetCode Question #1206: Design Skiplist

Problem Statement:
Design a Skiplist without using any built-in libraries.

A Skiplist is a data structure that takes O(log(n)) time for add, erase, and search. 
It can be seen as a linked list with multiple levels. Each level is a sorted linked list, 
and with higher levels, the number of elements decreases. The Skiplist class should have the following methods:

1. __init__(): Initializes the Skiplist object.
2. search(target: int) -> bool: Returns true if the target exists in the Skiplist, otherwise false.
3. add(num: int) -> None: Inserts a number into the Skiplist.
4. erase(num: int) -> bool: Removes a number from the Skiplist. Returns true if the number exists and was removed, otherwise false.

Constraints:
- 0 <= num, target <= 2 * 10^4
- At most 5 * 10^4 calls will be made to search, add, and erase.

Example:
skiplist = Skiplist()
skiplist.add(1)
skiplist.add(2)
skiplist.add(3)
assert skiplist.search(0) == False
skiplist.add(4)
assert skiplist.search(1) == True
assert skiplist.erase(0) == False
assert skiplist.erase(1) == True
assert skiplist.search(1) == False
"""

import random

class Node:
    def __init__(self, val: int, level: int):
        self.val = val
        self.next = [None] * level  # Pointers to the next nodes at each level

class Skiplist:
    def __init__(self):
        self.max_level = 16  # Maximum number of levels
        self.head = Node(-1, self.max_level)  # Head node with dummy value
        self.levels = 1  # Current number of levels in the skiplist

    def _random_level(self) -> int:
        """Generate a random level for a new node."""
        level = 1
        while random.random() < 0.5 and level < self.max_level:
            level += 1
        return level

    def search(self, target: int) -> bool:
        """Search for a target value in the skiplist."""
        curr = self.head
        for i in range(self.levels - 1, -1, -1):  # Start from the highest level
            while curr.next[i] and curr.next[i].val < target:
                curr = curr.next[i]
        curr = curr.next[0]  # Move to the lowest level
        return curr and curr.val == target

    def add(self, num: int) -> None:
        """Add a number to the skiplist."""
        update = [None] * self.max_level
        curr = self.head
        for i in range(self.levels - 1, -1, -1):  # Start from the highest level
            while curr.next[i] and curr.next[i].val < num:
                curr = curr.next[i]
            update[i] = curr  # Store the last node at each level before the insertion point

        level = self._random_level()
        if level > self.levels:  # Increase the number of levels if necessary
            for i in range(self.levels, level):
                update[i] = self.head
            self.levels = level

        new_node = Node(num, level)
        for i in range(level):  # Insert the new node at each level
            new_node.next[i] = update[i].next[i]
            update[i].next[i] = new_node

    def erase(self, num: int) -> bool:
        """Erase a number from the skiplist."""
        update = [None] * self.max_level
        curr = self.head
        for i in range(self.levels - 1, -1, -1):  # Start from the highest level
            while curr.next[i] and curr.next[i].val < num:
                curr = curr.next[i]
            update[i] = curr

        curr = curr.next[0]
        if not curr or curr.val != num:  # If the number is not found
            return False

        for i in range(self.levels):  # Remove the node at each level
            if update[i].next[i] != curr:
                break
            update[i].next[i] = curr.next[i]

        while self.levels > 1 and not self.head.next[self.levels - 1]:  # Adjust levels
            self.levels -= 1

        return True


# Example Test Cases
if __name__ == "__main__":
    skiplist = Skiplist()
    skiplist.add(1)
    skiplist.add(2)
    skiplist.add(3)
    assert skiplist.search(0) == False  # 0 is not in the skiplist
    skiplist.add(4)
    assert skiplist.search(1) == True  # 1 is in the skiplist
    assert skiplist.erase(0) == False  # 0 is not in the skiplist
    assert skiplist.erase(1) == True  # 1 is removed from the skiplist
    assert skiplist.search(1) == False  # 1 is no longer in the skiplist

    print("All test cases passed!")

"""
Time and Space Complexity Analysis:

1. Search:
   - Time Complexity: O(log(n)) on average due to the skiplist structure.
   - Space Complexity: O(1).

2. Add:
   - Time Complexity: O(log(n)) on average due to traversal and insertion.
   - Space Complexity: O(log(n)) for the new node's pointers.

3. Erase:
   - Time Complexity: O(log(n)) on average due to traversal and removal.
   - Space Complexity: O(1).

Topic: Design, Linked List
"""