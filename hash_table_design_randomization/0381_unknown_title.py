"""
LeetCode Problem #381: Insert Delete GetRandom O(1) - Duplicates allowed

Problem Statement:
Design a data structure that supports all following operations in average O(1) time.

1. `insert(val)`: Inserts an item val to the collection. Returns true if the collection did not already contain the specified element.
2. `remove(val)`: Removes an item val from the collection if present. Returns true if the collection contained the specified element.
3. `getRandom()`: Returns a random element from the current collection of elements. The probability of each element being returned is linearly related to the number of same elements in the collection.

Note:
- You may assume the collection contains only integers.
- Duplicates are allowed.

Example:
```
Input:
["RandomizedCollection", "insert", "insert", "insert", "getRandom", "remove", "getRandom"]
[[], [1], [1], [2], [], [1], []]

Output:
[null, true, false, true, 1, true, 1]

Explanation:
RandomizedCollection randomizedCollection = new RandomizedCollection();
randomizedCollection.insert(1);   // Inserts 1 to the collection. Returns true as the collection did not contain 1.
randomizedCollection.insert(1);   // Inserts another 1 to the collection. Returns false as the collection contained 1. Collection now contains [1,1].
randomizedCollection.insert(2);   // Inserts 2 to the collection, returns true. Collection now contains [1,1,2].
randomizedCollection.getRandom(); // getRandom should return 1 with the probability 2/3, and 2 with the probability 1/3.
randomizedCollection.remove(1);   // Removes 1 from the collection, returns true. Collection now contains [1,2].
randomizedCollection.getRandom(); // getRandom should return 1 and 2 both equally likely.
```
"""

import random
from collections import defaultdict

class RandomizedCollection:
    def __init__(self):
        # Dictionary to store the indices of each value
        self.val_to_indices = defaultdict(set)
        # List to store the values
        self.values = []

    def insert(self, val: int) -> bool:
        # Add the value to the list
        self.values.append(val)
        # Add the index of the value to the dictionary
        self.val_to_indices[val].add(len(self.values) - 1)
        # Return True if this is the first occurrence of the value
        return len(self.val_to_indices[val]) == 1

    def remove(self, val: int) -> bool:
        if val not in self.val_to_indices or not self.val_to_indices[val]:
            return False
        
        # Get an arbitrary index of the value to remove
        remove_idx = self.val_to_indices[val].pop()
        # Get the last value in the list
        last_val = self.values[-1]
        
        # Replace the value to be removed with the last value
        self.values[remove_idx] = last_val
        # Update the index of the last value in the dictionary
        self.val_to_indices[last_val].add(remove_idx)
        self.val_to_indices[last_val].discard(len(self.values) - 1)
        
        # Remove the last value from the list
        self.values.pop()
        
        # Clean up the dictionary if no indices are left for the value
        if not self.val_to_indices[val]:
            del self.val_to_indices[val]
        
        return True

    def getRandom(self) -> int:
        # Return a random value from the list
        return random.choice(self.values)


# Example Test Cases
if __name__ == "__main__":
    randomizedCollection = RandomizedCollection()
    
    # Test case 1
    print(randomizedCollection.insert(1))  # True
    print(randomizedCollection.insert(1))  # False
    print(randomizedCollection.insert(2))  # True
    print(randomizedCollection.getRandom())  # 1 or 2 (1 with 2/3 probability, 2 with 1/3 probability)
    print(randomizedCollection.remove(1))  # True
    print(randomizedCollection.getRandom())  # 1 or 2 (equal probability)

    # Test case 2
    print(randomizedCollection.insert(3))  # True
    print(randomizedCollection.insert(3))  # False
    print(randomizedCollection.remove(2))  # True
    print(randomizedCollection.getRandom())  # 1 or 3 (equal probability)


"""
Time and Space Complexity Analysis:

1. `insert(val)`:
   - Time Complexity: O(1) on average. Appending to the list and updating the dictionary are O(1) operations.
   - Space Complexity: O(1) additional space per insertion.

2. `remove(val)`:
   - Time Complexity: O(1) on average. Removing an element from the dictionary and updating the list are O(1) operations.
   - Space Complexity: O(1) additional space.

3. `getRandom()`:
   - Time Complexity: O(1). Accessing a random element from the list is O(1).
   - Space Complexity: O(1).

Overall Space Complexity:
- O(n), where n is the number of elements in the collection. This accounts for the space used by the list and the dictionary.

Topic: Hash Table, Design, Randomization
"""