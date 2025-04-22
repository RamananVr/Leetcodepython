"""
LeetCode Problem #432: All O`one Data Structure

Problem Statement:
Design a data structure to store the strings' counts with the following operations:

1. `inc(String key)` - Increments the count of the string `key` by 1. If `key` does not exist in the data structure, insert it with count 1.
2. `dec(String key)` - Decrements the count of the string `key` by 1. If the count of `key` becomes 0, remove it from the data structure. If `key` does not exist, this operation does nothing.
3. `getMaxKey()` - Returns one of the keys with the maximal count. If no element exists, return an empty string `""`.
4. `getMinKey()` - Returns one of the keys with the minimal count. If no element exists, return an empty string `""`.

Implement the `AllOne` class:
- `AllOne()` Initializes the object of the data structure.
- `void inc(String key)` Increments the count of the string `key` by 1.
- `void dec(String key)` Decrements the count of the string `key` by 1.
- `String getMaxKey()` Returns one of the keys with the maximal count.
- `String getMinKey()` Returns one of the keys with the minimal count.

Constraints:
- `1 <= key.length <= 100`
- `key` consists of lowercase English letters.
- The total number of calls to all functions will not exceed `5 * 10^4`.
"""

from collections import defaultdict

class AllOne:
    def __init__(self):
        # Dictionary to store the count of each key
        self.key_count = defaultdict(int)
        # Dictionary to store keys by their counts
        self.count_keys = defaultdict(set)
        # Track the minimum and maximum counts
        self.min_count = float('inf')
        self.max_count = float('-inf')

    def _update_min_max(self):
        # Update min_count and max_count based on current keys
        if not self.key_count:
            self.min_count = float('inf')
            self.max_count = float('-inf')
        else:
            self.min_count = min(self.count_keys.keys())
            self.max_count = max(self.count_keys.keys())

    def inc(self, key: str) -> None:
        # Increment the count of the key
        current_count = self.key_count[key]
        new_count = current_count + 1
        self.key_count[key] = new_count

        # Update count_keys
        if current_count > 0:
            self.count_keys[current_count].remove(key)
            if not self.count_keys[current_count]:
                del self.count_keys[current_count]
        self.count_keys[new_count].add(key)

        # Update min_count and max_count
        self._update_min_max()

    def dec(self, key: str) -> None:
        # Decrement the count of the key
        if key not in self.key_count:
            return

        current_count = self.key_count[key]
        new_count = current_count - 1

        # Update count_keys
        self.count_keys[current_count].remove(key)
        if not self.count_keys[current_count]:
            del self.count_keys[current_count]

        if new_count > 0:
            self.key_count[key] = new_count
            self.count_keys[new_count].add(key)
        else:
            del self.key_count[key]

        # Update min_count and max_count
        self._update_min_max()

    def getMaxKey(self) -> str:
        # Return one of the keys with the maximum count
        if self.max_count == float('-inf'):
            return ""
        return next(iter(self.count_keys[self.max_count]))

    def getMinKey(self) -> str:
        # Return one of the keys with the minimum count
        if self.min_count == float('inf'):
            return ""
        return next(iter(self.count_keys[self.min_count]))


# Example Test Cases
if __name__ == "__main__":
    obj = AllOne()
    obj.inc("hello")
    obj.inc("hello")
    print(obj.getMaxKey())  # Output: "hello"
    print(obj.getMinKey())  # Output: "hello"
    obj.inc("leet")
    print(obj.getMaxKey())  # Output: "hello"
    print(obj.getMinKey())  # Output: "leet"
    obj.dec("hello")
    print(obj.getMaxKey())  # Output: "hello"
    print(obj.getMinKey())  # Output: "hello"
    obj.dec("hello")
    print(obj.getMaxKey())  # Output: "leet"
    print(obj.getMinKey())  # Output: "leet"

"""
Time Complexity:
- `inc` and `dec`: O(1) on average, as dictionary and set operations (add/remove) are O(1).
- `getMaxKey` and `getMinKey`: O(1), as we directly access the max/min count keys.

Space Complexity:
- O(n), where n is the number of unique keys stored in the data structure.

Topic: Design, Hash Table, Doubly Linked List
"""