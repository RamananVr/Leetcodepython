"""
LeetCode Problem #2394: Find Consecutive Integers from a Data Stream

Problem Statement:
You are given a data stream of integers. Implement a class `DataStream` that supports the following operations:

1. `DataStream(value: int, k: int)`: Initializes the object with an integer `value` and an integer `k`.
2. `consec(num: int) -> bool`: This method is called when a new integer `num` is inserted into the data stream. It returns:
   - `True` if the last `k` integers in the data stream are equal to `value`.
   - `False` otherwise.

Note:
- If there are fewer than `k` integers in the data stream, the method should return `False`.

Constraints:
- `1 <= value, num <= 10^9`
- `1 <= k <= 10^5`
- At most `10^5` calls will be made to `consec`.

Example:
Input:
    obj = DataStream(4, 3)
    obj.consec(4) -> False
    obj.consec(4) -> False
    obj.consec(4) -> True
    obj.consec(3) -> False
"""

# Solution
class DataStream:
    def __init__(self, value: int, k: int):
        """
        Initializes the DataStream object with a target value and a window size k.
        """
        self.value = value
        self.k = k
        self.count = 0  # Tracks the count of consecutive `value` occurrences
        self.stream = []  # Tracks the last k elements in the stream

    def consec(self, num: int) -> bool:
        """
        Processes the incoming number and checks if the last k numbers are equal to `value`.
        """
        self.stream.append(num)
        
        # If the number matches the target value, increment the count
        if num == self.value:
            self.count += 1
        else:
            self.count = 0  # Reset count if the number doesn't match
        
        # If the stream size exceeds k, remove the oldest element
        if len(self.stream) > self.k:
            removed = self.stream.pop(0)
            if removed == self.value:
                self.count -= 1
        
        # Return True if the last k numbers are all equal to `value`
        return self.count == self.k


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    obj = DataStream(4, 3)
    print(obj.consec(4))  # Output: False
    print(obj.consec(4))  # Output: False
    print(obj.consec(4))  # Output: True
    print(obj.consec(3))  # Output: False

    # Test Case 2
    obj2 = DataStream(5, 2)
    print(obj2.consec(5))  # Output: False
    print(obj2.consec(5))  # Output: True
    print(obj2.consec(6))  # Output: False
    print(obj2.consec(5))  # Output: False

    # Test Case 3
    obj3 = DataStream(1, 1)
    print(obj3.consec(1))  # Output: True
    print(obj3.consec(2))  # Output: False
    print(obj3.consec(1))  # Output: True


# Time and Space Complexity Analysis
"""
Time Complexity:
- The `consec` method runs in O(1) time for each call. This is because appending to a list and removing the first element
  (when the size exceeds k) are both O(1) operations.

Space Complexity:
- The space complexity is O(k), as we maintain a sliding window of size k in the `stream` list.

Overall:
- Time Complexity: O(1) per `consec` call
- Space Complexity: O(k)
"""

# Topic: Sliding Window, Queue