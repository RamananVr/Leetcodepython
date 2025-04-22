"""
LeetCode Problem #981: Time Based Key-Value Store

Problem Statement:
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps 
and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:
- TimeMap() Initializes the object of the data structure.
- void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
- String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. 
  If there are multiple such values, it returns the value associated with the largest timestamp_prev. 
  If there are no values, it returns "".

Example:
Input:
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]

Output:
[null, null, "bar", "bar", null, "bar2", "bar2"]

Explanation:
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1); // store the key "foo" and value "bar" along with timestamp = 1.
timeMap.get("foo", 1);        // return "bar"
timeMap.get("foo", 3);        // return "bar", since there is no value corresponding to timestamp 3 and timestamp 1 is the closest.
timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
timeMap.get("foo", 4);        // return "bar2"
timeMap.get("foo", 5);        // return "bar2", since timestamp 4 is the closest to 5.

Constraints:
- 1 <= key.length, value.length <= 100
- key and value consist of lowercase English letters and digits.
- 1 <= timestamp <= 10^7
- All the timestamps timestamp of set are strictly increasing.
- At most 2 * 10^4 calls will be made to set and get.
"""

# Solution
class TimeMap:
    def __init__(self):
        # Dictionary to store key -> list of (timestamp, value) pairs
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        # Binary search to find the largest timestamp <= given timestamp
        values = self.store[key]
        left, right = 0, len(values) - 1
        result = ""
        
        while left <= right:
            mid = (left + right) // 2
            if values[mid][0] <= timestamp:
                result = values[mid][1]  # Update result to the current value
                left = mid + 1          # Search in the right half
            else:
                right = mid - 1         # Search in the left half
        
        return result

# Example Test Cases
if __name__ == "__main__":
    # Initialize TimeMap object
    timeMap = TimeMap()
    
    # Test Case 1
    timeMap.set("foo", "bar", 1)
    assert timeMap.get("foo", 1) == "bar"  # Expected: "bar"
    assert timeMap.get("foo", 3) == "bar"  # Expected: "bar"
    
    # Test Case 2
    timeMap.set("foo", "bar2", 4)
    assert timeMap.get("foo", 4) == "bar2"  # Expected: "bar2"
    assert timeMap.get("foo", 5) == "bar2"  # Expected: "bar2"
    
    # Test Case 3
    assert timeMap.get("baz", 1) == ""  # Expected: ""

    print("All test cases passed!")

"""
Time and Space Complexity Analysis:

1. set(key, value, timestamp):
   - Time Complexity: O(1), as appending to a list is an O(1) operation.
   - Space Complexity: O(1) for each call, but overall space usage is O(n), where n is the total number of (timestamp, value) pairs stored.

2. get(key, timestamp):
   - Time Complexity: O(log m), where m is the number of timestamps stored for the given key. This is due to binary search.
   - Space Complexity: O(1), as no additional space is used.

Overall Complexity:
- Time Complexity: O(log m) for get and O(1) for set.
- Space Complexity: O(n), where n is the total number of (timestamp, value) pairs stored.

Topic: Hash Table, Binary Search
"""