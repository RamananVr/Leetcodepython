"""
LeetCode Problem #380: Insert Delete GetRandom O(1)

Problem Statement:
Implement the RandomizedSet class:

1. `RandomizedSet()` Initializes the RandomizedSet object.
2. `bool insert(int val)` Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
3. `bool remove(int val)` Removes an item val from the set if present. Returns true if the item was present, false otherwise.
4. `int getRandom()` Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.

You must implement the functions of the class such that each function works in average O(1) time complexity.

Constraints:
- `-2^31 <= val <= 2^31 - 1`
- At most `2 * 10^5` calls will be made to `insert`, `remove`, and `getRandom`.

"""

import random

class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []  # List to store elements
        self.index_map = {}  # Dictionary to store element -> index mapping

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.index_map:
            return False
        self.data.append(val)
        self.index_map[val] = len(self.data) - 1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.index_map:
            return False
        # Swap the element to remove with the last element
        last_element = self.data[-1]
        idx_to_remove = self.index_map[val]
        self.data[idx_to_remove] = last_element
        self.index_map[last_element] = idx_to_remove
        # Remove the last element
        self.data.pop()
        del self.index_map[val]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.data)


# Example Test Cases
if __name__ == "__main__":
    # Initialize the RandomizedSet
    randomized_set = RandomizedSet()

    # Test insert
    print(randomized_set.insert(1))  # True (1 is inserted)
    print(randomized_set.insert(2))  # True (2 is inserted)
    print(randomized_set.insert(1))  # False (1 already exists)

    # Test remove
    print(randomized_set.remove(1))  # True (1 is removed)
    print(randomized_set.remove(3))  # False (3 does not exist)

    # Test getRandom
    print(randomized_set.getRandom())  # Randomly returns 2 (only element left)
    randomized_set.insert(3)
    print(randomized_set.getRandom())  # Randomly returns 2 or 3

"""
Time and Space Complexity Analysis:

1. `insert(val)`:
   - Time Complexity: O(1) on average, as dictionary operations (insert and lookup) are O(1).
   - Space Complexity: O(1) additional space for storing the new element.

2. `remove(val)`:
   - Time Complexity: O(1) on average, as dictionary operations and list operations (swap and pop) are O(1).
   - Space Complexity: O(1) additional space.

3. `getRandom()`:
   - Time Complexity: O(1), as `random.choice()` on a list is O(1).
   - Space Complexity: O(1).

Overall:
- Time Complexity: O(1) for all operations on average.
- Space Complexity: O(n), where n is the number of elements in the set.

Topic: Hash Table, Design
"""