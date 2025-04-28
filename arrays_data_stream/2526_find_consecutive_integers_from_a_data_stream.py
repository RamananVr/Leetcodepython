"""
LeetCode Question #2526: Find Consecutive Integers from a Data Stream

Problem Statement:
You are given a data stream represented as an integer array `nums`. Each integer in the stream is processed sequentially. 
Implement a class `DataStream` that supports the following two methods:

1. `__init__(self, value: int, k: int)`:
   - Initializes the object with an integer `value` and an integer `k`.

2. `consec(self, num: int) -> bool`:
   - Processes the integer `num` from the data stream.
   - Returns `True` if `num` equals `value` and there have been exactly `k` consecutive occurrences of `value` in the stream (including the current `num`).
   - Otherwise, returns `False`.

Constraints:
- `1 <= k <= 10^5`
- `value` and `num` are integers in the range `[0, 10^9]`.
- At most `10^5` calls will be made to `consec`.

Example:
Input:
["DataStream", "consec", "consec", "consec", "consec"]
[[4, 3], [4], [4], [4], [3]]

Output:
[None, False, False, True, False]

Explanation:
DataStream dataStream = new DataStream(4, 3); // Initialize the object with value = 4 and k = 3.
dataStream.consec(4); // Consecutive occurrences: [4]. Returns False.
dataStream.consec(4); // Consecutive occurrences: [4, 4]. Returns False.
dataStream.consec(4); // Consecutive occurrences: [4, 4, 4]. Returns True.
dataStream.consec(3); // Consecutive occurrences: [4, 4, 4, 3]. Returns False.
"""

# Python Solution
class DataStream:
    def __init__(self, value: int, k: int):
        """
        Initializes the DataStream object with the target value and the required consecutive count.
        """
        self.value = value
        self.k = k
        self.count = 0  # Tracks the current consecutive occurrences of `value`

    def consec(self, num: int) -> bool:
        """
        Processes the integer `num` and checks if there are exactly `k` consecutive occurrences of `value`.
        """
        if num == self.value:
            self.count += 1
        else:
            self.count = 0  # Reset the count if the number is not equal to `value`

        return self.count >= self.k


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    dataStream = DataStream(4, 3)
    print(dataStream.consec(4))  # Output: False
    print(dataStream.consec(4))  # Output: False
    print(dataStream.consec(4))  # Output: True
    print(dataStream.consec(3))  # Output: False

    # Test Case 2
    dataStream = DataStream(5, 2)
    print(dataStream.consec(5))  # Output: False
    print(dataStream.consec(5))  # Output: True
    print(dataStream.consec(5))  # Output: True
    print(dataStream.consec(6))  # Output: False

    # Test Case 3
    dataStream = DataStream(1, 1)
    print(dataStream.consec(1))  # Output: True
    print(dataStream.consec(2))  # Output: False
    print(dataStream.consec(1))  # Output: True


# Time and Space Complexity Analysis
"""
Time Complexity:
- The `consec` method runs in O(1) time since it only involves a few comparisons and updates to the `count` variable.

Space Complexity:
- The space complexity is O(1) since we are only storing a few variables (`value`, `k`, and `count`) and no additional data structures are used.

Overall, the solution is efficient and scales well with the constraints.
"""

# Topic: Arrays / Data Stream