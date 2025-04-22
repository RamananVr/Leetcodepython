"""
LeetCode Problem #677: Map Sum Pairs

Problem Statement:
Implement the `MapSum` class that supports two operations:

1. `void insert(String key, int val)`:
   - Inserts the key-value pair into the map. If the key already exists, the original key-value pair will be overridden to the new one.

2. `int sum(String prefix)`:
   - Returns the sum of all the values of keys that start with the given prefix.

Example:
MapSum mapSum = new MapSum();
mapSum.insert("apple", 3);
mapSum.sum("ap");           // return 3 (apple = 3)
mapSum.insert("app", 2);
mapSum.sum("ap");           // return 5 (apple + app = 3 + 2 = 5)

Constraints:
- The key consists of only lowercase English letters.
- The total number of calls to `insert` and `sum` will not exceed 3 * 10^4.
- 1 <= key.length, prefix.length <= 100
- 0 <= val <= 1000
"""

# Solution
class MapSum:
    def __init__(self):
        # Initialize a dictionary to store key-value pairs
        self.map = {}
        # Initialize a dictionary to store prefix sums
        self.prefix_map = {}

    def insert(self, key: str, val: int) -> None:
        # If the key already exists, calculate the difference between the new and old value
        delta = val - self.map.get(key, 0)
        # Update the key-value pair in the map
        self.map[key] = val
        # Update the prefix sums
        prefix = ""
        for char in key:
            prefix += char
            self.prefix_map[prefix] = self.prefix_map.get(prefix, 0) + delta

    def sum(self, prefix: str) -> int:
        # Return the sum of all values for the given prefix
        return self.prefix_map.get(prefix, 0)


# Example Test Cases
if __name__ == "__main__":
    # Initialize the MapSum object
    mapSum = MapSum()

    # Test Case 1
    mapSum.insert("apple", 3)
    assert mapSum.sum("ap") == 3  # apple = 3

    # Test Case 2
    mapSum.insert("app", 2)
    assert mapSum.sum("ap") == 5  # apple + app = 3 + 2 = 5

    # Test Case 3
    mapSum.insert("apple", 5)
    assert mapSum.sum("ap") == 7  # apple (updated to 5) + app = 5 + 2 = 7

    # Test Case 4
    mapSum.insert("apricot", 4)
    assert mapSum.sum("ap") == 11  # apple (5) + app (2) + apricot (4) = 11

    # Test Case 5
    assert mapSum.sum("a") == 11  # apple (5) + app (2) + apricot (4) = 11

    # Test Case 6
    assert mapSum.sum("b") == 0  # No keys with prefix "b"

    print("All test cases passed!")

"""
Time and Space Complexity Analysis:

1. `insert` Method:
   - Time Complexity: O(k), where k is the length of the key. This is because we update the prefix sums for each prefix of the key.
   - Space Complexity: O(n * k), where n is the number of keys and k is the average length of the keys. This is due to the storage of prefix sums in the `prefix_map`.

2. `sum` Method:
   - Time Complexity: O(1), as we directly retrieve the sum for the given prefix from the `prefix_map`.
   - Space Complexity: O(1), as no additional space is used during the operation.

Overall:
- Time Complexity: O(k) for `insert` and O(1) for `sum`.
- Space Complexity: O(n * k) for storing the keys and prefix sums.

Topic: Trie (Prefix Tree)
"""