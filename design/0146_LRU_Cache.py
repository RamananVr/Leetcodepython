"""
LeetCode Problem #146: LRU Cache

Problem Statement:
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:
- LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
- int get(int key) Return the value of the key if the key exists, otherwise return -1.
- void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. 
  If the number of keys exceeds the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.

Constraints:
- 1 <= capacity <= 3000
- 0 <= key <= 10^4
- 0 <= value <= 10^5
- At most 2 * 10^5 calls will be made to get and put.
"""

from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        """
        Initialize the LRUCache with a given capacity.
        """
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        """
        Retrieve the value of the key if it exists in the cache.
        If the key exists, it is marked as recently used.
        """
        if key in self.cache:
            # Move the accessed key to the end to mark it as recently used
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        """
        Add a key-value pair to the cache. If the key already exists, update its value
        and mark it as recently used. If the cache exceeds its capacity, evict the least
        recently used key.
        """
        if key in self.cache:
            # Update the value and mark as recently used
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            # Pop the least recently used item (first item in OrderedDict)
            self.cache.popitem(last=False)

# Example Test Cases
if __name__ == "__main__":
    # Initialize the cache with a capacity of 2
    lru_cache = LRUCache(2)

    # Test Case 1: Add key-value pairs
    lru_cache.put(1, 1)  # Cache: {1: 1}
    lru_cache.put(2, 2)  # Cache: {1: 1, 2: 2}

    # Test Case 2: Access key 1
    print(lru_cache.get(1))  # Output: 1, Cache: {2: 2, 1: 1}

    # Test Case 3: Add another key-value pair, causing eviction
    lru_cache.put(3, 3)  # Cache: {1: 1, 3: 3} (key 2 is evicted)

    # Test Case 4: Access key 2 (which was evicted)
    print(lru_cache.get(2))  # Output: -1

    # Test Case 5: Add another key-value pair, causing eviction
    lru_cache.put(4, 4)  # Cache: {3: 3, 4: 4} (key 1 is evicted)

    # Test Case 6: Access key 1 (which was evicted)
    print(lru_cache.get(1))  # Output: -1

    # Test Case 7: Access key 3
    print(lru_cache.get(3))  # Output: 3, Cache: {4: 4, 3: 3}

    # Test Case 8: Access key 4
    print(lru_cache.get(4))  # Output: 4, Cache: {3: 3, 4: 4}

"""
Time Complexity Analysis:
- The `get` operation takes O(1) on average because accessing a key in an OrderedDict is O(1), 
  and moving it to the end is also O(1).
- The `put` operation takes O(1) on average because inserting a key-value pair and evicting the 
  least recently used item (if necessary) are O(1) operations.

Space Complexity Analysis:
- The space complexity is O(capacity), where `capacity` is the maximum number of key-value pairs 
  the cache can hold. This is because the OrderedDict stores up to `capacity` items.

Topic: Design
"""