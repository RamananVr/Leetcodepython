"""
LeetCode Problem #705: Design HashSet

Problem Statement:
Design a HashSet without using any built-in hash table libraries.

Implement `MyHashSet` class:
- `MyHashSet()` Initializes the object with an empty set.
- `void add(key)` Inserts the value `key` into the HashSet.
- `bool contains(key)` Returns whether the value `key` exists in the HashSet or not.
- `void remove(key)` Removes the value `key` in the HashSet. If `key` does not exist in the HashSet, do nothing.

Constraints:
- 0 <= key <= 10^6
- At most 10^4 calls will be made to `add`, `remove`, and `contains`.

Example:
    Input:
    ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
    [[], [1], [2], [1], [3], [2], [2], [2], [2]]
    Output:
    [null, null, null, true, false, null, true, null, false]

Explanation:
    MyHashSet myHashSet = new MyHashSet();
    myHashSet.add(1);      // set = [1]
    myHashSet.add(2);      // set = [1, 2]
    myHashSet.contains(1); // return True
    myHashSet.contains(3); // return False, (not found)
    myHashSet.add(2);      // set = [1, 2]
    myHashSet.contains(2); // return True
    myHashSet.remove(2);   // set = [1]
    myHashSet.contains(2); // return False, (already removed)
"""

class MyHashSet:
    def __init__(self):
        """
        Initialize the data structure. We use a boolean array of size 10^6 + 1
        to represent the presence of keys.
        """
        self.size = 10**6 + 1
        self.data = [False] * self.size

    def add(self, key: int) -> None:
        """
        Add the key to the HashSet.
        """
        self.data[key] = True

    def remove(self, key: int) -> None:
        """
        Remove the key from the HashSet.
        """
        self.data[key] = False

    def contains(self, key: int) -> bool:
        """
        Check if the key exists in the HashSet.
        """
        return self.data[key]


# Example Test Cases
if __name__ == "__main__":
    # Initialize the HashSet
    myHashSet = MyHashSet()

    # Test Case 1: Add elements
    myHashSet.add(1)  # Add 1
    myHashSet.add(2)  # Add 2
    assert myHashSet.contains(1) == True  # 1 is in the set
    assert myHashSet.contains(3) == False  # 3 is not in the set

    # Test Case 2: Add duplicate element
    myHashSet.add(2)  # Add 2 again
    assert myHashSet.contains(2) == True  # 2 is still in the set

    # Test Case 3: Remove element
    myHashSet.remove(2)  # Remove 2
    assert myHashSet.contains(2) == False  # 2 is no longer in the set

    print("All test cases passed!")

"""
Time Complexity Analysis:
- `add(key)`: O(1) - Direct access to the index in the array.
- `remove(key)`: O(1) - Direct access to the index in the array.
- `contains(key)`: O(1) - Direct access to the index in the array.

Space Complexity:
- O(U), where U is the universe of keys (10^6 + 1). We use a boolean array of size 10^6 + 1.

Topic: Hashing
"""