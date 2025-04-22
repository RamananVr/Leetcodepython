"""
LeetCode Question #460: LFU Cache

Problem Statement:
Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the LFUCache class:
- LFUCache(int capacity) Initializes the object with the capacity of the data structure.
- int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
- void put(int key, int value) Updates the value of the key if the key exists. Otherwise, adds the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least frequently used key. If there is a tie, the least recently used key is evicted.

The functions get and put must each run in O(1) average time complexity.

Constraints:
- 0 <= capacity <= 10^4
- 0 <= key <= 10^4
- 0 <= value <= 10^5
- At most 2 * 10^5 calls will be made to get and put.
"""

from collections import defaultdict, OrderedDict

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_to_val_freq = {}  # Maps key -> (value, frequency)
        self.freq_to_keys = defaultdict(OrderedDict)  # Maps frequency -> OrderedDict of keys

    def _update_frequency(self, key: int):
        value, freq = self.key_to_val_freq[key]
        # Remove key from current frequency list
        del self.freq_to_keys[freq][key]
        if not self.freq_to_keys[freq]:
            del self.freq_to_keys[freq]
            if self.min_freq == freq:
                self.min_freq += 1
        # Add key to next frequency list
        self.key_to_val_freq[key] = (value, freq + 1)
        self.freq_to_keys[freq + 1][key] = None

    def get(self, key: int) -> int:
        if key not in self.key_to_val_freq:
            return -1
        self._update_frequency(key)
        return self.key_to_val_freq[key][0]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.key_to_val_freq:
            self.key_to_val_freq[key] = (value, self.key_to_val_freq[key][1])
            self._update_frequency(key)
        else:
            if len(self.key_to_val_freq) >= self.capacity:
                # Evict the least frequently used key
                evict_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
                del self.key_to_val_freq[evict_key]
            # Add new key
            self.key_to_val_freq[key] = (value, 1)
            self.freq_to_keys[1][key] = None
            self.min_freq = 1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    lfu = LFUCache(2)
    lfu.put(1, 1)
    lfu.put(2, 2)
    assert lfu.get(1) == 1  # Key 1 exists, return 1
    lfu.put(3, 3)  # Evicts key 2 (least frequently used)
    assert lfu.get(2) == -1  # Key 2 was evicted
    assert lfu.get(3) == 3  # Key 3 exists, return 3
    lfu.put(4, 4)  # Evicts key 1 (least frequently used)
    assert lfu.get(1) == -1  # Key 1 was evicted
    assert lfu.get(3) == 3  # Key 3 exists, return 3
    assert lfu.get(4) == 4  # Key 4 exists, return 4

    # Test Case 2
    lfu = LFUCache(0)
    lfu.put(1, 1)  # No operation since capacity is 0
    assert lfu.get(1) == -1  # Key 1 does not exist

    print("All test cases passed!")

"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - `get`: O(1) average time complexity. Updating the frequency and accessing the value are constant-time operations.
   - `put`: O(1) average time complexity. Adding a new key or updating an existing key involves constant-time operations, including eviction.

2. Space Complexity:
   - The space complexity is O(capacity + F), where `capacity` is the maximum number of keys stored and `F` is the number of frequency levels. Each frequency level uses an OrderedDict to store keys.

Topic: Design, Hash Table, OrderedDict
"""