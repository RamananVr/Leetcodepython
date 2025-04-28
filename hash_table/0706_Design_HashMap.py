"""
LeetCode Problem #706: Design HashMap

Problem Statement:
Design a HashMap without using any built-in hash table libraries.

Implement the `MyHashMap` class:
- `MyHashMap()` initializes the object with an empty map.
- `void put(int key, int value)` inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
- `int get(int key)` returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
- `void remove(int key)` removes the key and its corresponding value if the map contains the mapping for the key.

Constraints:
- 0 <= key, value <= 10^6
- At most 10^4 calls will be made to `put`, `get`, and `remove`.

Follow-up:
Can you solve the problem with a time complexity of O(1) for each function on average?

"""

class MyHashMap:
    def __init__(self):
        """
        Initialize the data structure.
        We use a list of buckets, where each bucket is a list of (key, value) pairs.
        """
        self.size = 1000  # Number of buckets
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key: int) -> int:
        """
        Hash function to determine the bucket index for a given key.
        """
        return key % self.size

    def put(self, key: int, value: int) -> None:
        """
        Insert a (key, value) pair into the HashMap. If the key already exists, update its value.
        """
        bucket_index = self._hash(key)
        bucket = self.buckets[bucket_index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # Update the value
                return
        bucket.append((key, value))  # Add new key-value pair

    def get(self, key: int) -> int:
        """
        Retrieve the value associated with the given key, or -1 if the key does not exist.
        """
        bucket_index = self._hash(key)
        bucket = self.buckets[bucket_index]
        for k, v in bucket:
            if k == key:
                return v
        return -1  # Key not found

    def remove(self, key: int) -> None:
        """
        Remove the key and its associated value from the HashMap, if it exists.
        """
        bucket_index = self._hash(key)
        bucket = self.buckets[bucket_index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]  # Remove the key-value pair
                return


# Example Test Cases
if __name__ == "__main__":
    # Initialize the HashMap
    hashMap = MyHashMap()

    # Test put() and get()
    hashMap.put(1, 1)  # Add key=1, value=1
    hashMap.put(2, 2)  # Add key=2, value=2
    assert hashMap.get(1) == 1  # Returns 1
    assert hashMap.get(3) == -1  # Returns -1 (key 3 does not exist)

    # Test update
    hashMap.put(2, 1)  # Update key=2 to value=1
    assert hashMap.get(2) == 1  # Returns 1

    # Test remove()
    hashMap.remove(2)  # Remove key=2
    assert hashMap.get(2) == -1  # Returns -1 (key 2 has been removed)

    print("All test cases passed!")

"""
Time and Space Complexity Analysis:

1. put(key, value):
   - Time Complexity: O(N / B) on average, where N is the number of keys and B is the number of buckets.
     In the best case, the hash function distributes keys uniformly, so each bucket has O(1) elements.
   - Space Complexity: O(N), where N is the number of keys stored in the HashMap.

2. get(key):
   - Time Complexity: O(N / B) on average, for the same reasons as `put`.
   - Space Complexity: O(1).

3. remove(key):
   - Time Complexity: O(N / B) on average, for the same reasons as `put`.
   - Space Complexity: O(1).

Topic: Hash Table
"""