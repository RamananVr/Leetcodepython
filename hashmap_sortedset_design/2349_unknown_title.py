"""
LeetCode Problem #2349: Design a Number Container System

Problem Statement:
Design a number container system that can do the following:
1. Insert or Replace a number at a given index in the system.
2. Return the smallest index for a given number in the system.

Implement the NumberContainers class:
- `__init__()` Initializes the number container system.
- `change(index: int, number: int) -> None` Changes the number at the given index to `number`. If there is already a number at that index, it will be replaced.
- `find(number: int) -> int` Returns the smallest index for the given `number` in the system. If no index is associated with the number, return `-1`.

Constraints:
- `1 <= index, number <= 10^9`
- At most `10^5` calls will be made to `change` and `find`.

Example:
    Input:
    ["NumberContainers", "change", "change", "change", "find", "change", "find"]
    [[], [1, 10], [2, 20], [3, 10], [10], [1, 20], [10]]
    Output:
    [None, None, None, None, 1, None, 3]

    Explanation:
    NumberContainers nc = new NumberContainers();
    nc.change(1, 10); // Add number 10 at index 1.
    nc.change(2, 20); // Add number 20 at index 2.
    nc.change(3, 10); // Add number 10 at index 3.
    nc.find(10);      // Return 1, as the smallest index with number 10 is 1.
    nc.change(1, 20); // Replace the number at index 1 with 20.
    nc.find(10);      // Return 3, as the smallest index with number 10 is now 3.
"""

from sortedcontainers import SortedSet

class NumberContainers:
    def __init__(self):
        # Maps index to the number stored at that index
        self.index_to_number = {}
        # Maps a number to a sorted set of indices where the number is stored
        self.number_to_indices = {}

    def change(self, index: int, number: int) -> None:
        # If the index already has a number, remove it from the old number's set
        if index in self.index_to_number:
            old_number = self.index_to_number[index]
            if old_number in self.number_to_indices:
                self.number_to_indices[old_number].discard(index)
                # Clean up if the set becomes empty
                if not self.number_to_indices[old_number]:
                    del self.number_to_indices[old_number]

        # Update the index with the new number
        self.index_to_number[index] = number
        if number not in self.number_to_indices:
            self.number_to_indices[number] = SortedSet()
        self.number_to_indices[number].add(index)

    def find(self, number: int) -> int:
        # If the number exists in the system, return the smallest index
        if number in self.number_to_indices and self.number_to_indices[number]:
            return self.number_to_indices[number][0]
        # Otherwise, return -1
        return -1


# Example Test Cases
if __name__ == "__main__":
    # Initialize the NumberContainers system
    nc = NumberContainers()
    
    # Test case 1
    nc.change(1, 10)  # Add number 10 at index 1
    nc.change(2, 20)  # Add number 20 at index 2
    nc.change(3, 10)  # Add number 10 at index 3
    assert nc.find(10) == 1  # Smallest index with number 10 is 1
    nc.change(1, 20)  # Replace the number at index 1 with 20
    assert nc.find(10) == 3  # Smallest index with number 10 is now 3
    assert nc.find(20) == 1  # Smallest index with number 20 is 1
    nc.change(3, 30)  # Replace the number at index 3 with 30
    assert nc.find(10) == -1  # No index with number 10 exists anymore

    print("All test cases passed!")

"""
Time Complexity:
- `change`: O(log(n)) where n is the number of indices associated with the number being updated. This is due to the use of a SortedSet for maintaining indices.
- `find`: O(1) for checking existence and retrieving the smallest index from the SortedSet.

Space Complexity:
- O(k) where k is the total number of unique indices and numbers stored in the system.

Topic: HashMap, SortedSet, Design
"""