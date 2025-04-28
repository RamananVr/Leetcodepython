"""
LeetCode Problem #2622: Cache With Time Limit

Problem Statement:
Design a time-limited cache that allows you to store key-value pairs with an expiration time. 
The cache should support the following operations:

1. set(key, value, duration): Stores the key-value pair in the cache with a time-to-live (TTL) of `duration` milliseconds.
2. get(key): Returns the value associated with `key` if the key exists in the cache and has not expired. Otherwise, returns -1.
3. count(): Returns the number of unexpired keys currently in the cache.

Implement the class `TimeLimitedCache` with the following methods:
- `set(key: int, value: int, duration: int) -> bool`: Stores the key-value pair with the given duration. Returns `True` if the key already exists in the cache and has not expired; otherwise, returns `False`.
- `get(key: int) -> int`: Returns the value associated with the key if it exists and has not expired; otherwise, returns -1.
- `count() -> int`: Returns the number of unexpired keys in the cache.

Constraints:
- `key` and `value` are integers.
- `duration` is a positive integer representing milliseconds.
- The cache should handle up to 1000 operations.

Example:
Input:
    cache = TimeLimitedCache()
    cache.set(1, 42, 1000) # Returns False
    cache.get(1)          # Returns 42
    cache.count()         # Returns 1
    sleep(1)              # Wait for 1 second
    cache.get(1)          # Returns -1
    cache.count()         # Returns 0
"""

import time

class TimeLimitedCache:
    def __init__(self):
        # Dictionary to store key-value pairs along with their expiration time
        self.cache = {}

    def set(self, key: int, value: int, duration: int) -> bool:
        """
        Stores the key-value pair with a time-to-live (TTL) of `duration` milliseconds.
        Returns True if the key already exists and has not expired; otherwise, returns False.
        """
        current_time = time.time() * 1000  # Current time in milliseconds
        is_existing_and_unexpired = key in self.cache and self.cache[key][1] > current_time
        self.cache[key] = (value, current_time + duration)  # Update the cache with new value and expiration time
        return is_existing_and_unexpired

    def get(self, key: int) -> int:
        """
        Returns the value associated with `key` if the key exists and has not expired; otherwise, returns -1.
        """
        current_time = time.time() * 1000  # Current time in milliseconds
        if key in self.cache and self.cache[key][1] > current_time:
            return self.cache[key][0]  # Return the value
        return -1  # Key does not exist or has expired

    def count(self) -> int:
        """
        Returns the number of unexpired keys currently in the cache.
        """
        current_time = time.time() * 1000  # Current time in milliseconds
        return sum(1 for _, expiration in self.cache.values() if expiration > current_time)


# Example Test Cases
if __name__ == "__main__":
    cache = TimeLimitedCache()
    
    # Test Case 1: Setting a key-value pair
    print(cache.set(1, 42, 1000))  # Expected: False (key does not exist yet)
    
    # Test Case 2: Getting the value of an unexpired key
    print(cache.get(1))  # Expected: 42 (key exists and has not expired)
    
    # Test Case 3: Counting unexpired keys
    print(cache.count())  # Expected: 1 (only one key is unexpired)
    
    # Test Case 4: Waiting for the key to expire
    time.sleep(1)  # Wait for 1 second
    print(cache.get(1))  # Expected: -1 (key has expired)
    print(cache.count())  # Expected: 0 (no unexpired keys)

    # Test Case 5: Overwriting an existing key before expiration
    cache.set(2, 100, 2000)  # Add a new key
    print(cache.set(2, 200, 3000))  # Expected: True (key exists and has not expired)
    print(cache.get(2))  # Expected: 200 (updated value)
    print(cache.count())  # Expected: 1 (key 2 is unexpired)

"""
Time and Space Complexity Analysis:

1. `set` Method:
   - Time Complexity: O(1) (dictionary insertion/update is O(1)).
   - Space Complexity: O(1) (constant space for storing the key-value pair).

2. `get` Method:
   - Time Complexity: O(1) (dictionary lookup is O(1)).
   - Space Complexity: O(1) (constant space for returning the value).

3. `count` Method:
   - Time Complexity: O(n), where n is the number of keys in the cache (iterates over all keys to check expiration).
   - Space Complexity: O(1) (constant space for counting).

Overall Space Complexity:
- O(n), where n is the number of keys stored in the cache.

Topic: HashMap / Dictionary
"""