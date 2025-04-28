"""
LeetCode Question #1825: Finding MK Average

Problem Statement:
Design a data structure that calculates and maintains the MK Average for a stream of integers.

The MK Average is calculated using the following steps:
1. If the number of elements in the stream is less than `m`, you should return -1.
2. Otherwise, remove the smallest `k` elements and the largest `k` elements from the stream.
3. Calculate the average of the remaining `m - 2k` elements and round down to the nearest integer.

Implement the `MKAverage` class:
- `MKAverage(int m, int k)` Initializes the MKAverage object with parameters `m` and `k`.
- `addElement(int num)` Inserts a new element `num` into the stream.
- `calculateMKAverage()` Returns the MK Average for the current stream or -1 if the number of elements in the stream is less than `m`.

Constraints:
- `3 <= m <= 10^5`
- `1 <= k < m/2`
- `-10^5 <= num <= 10^5`
- At most `10^5` calls will be made to `addElement` and `calculateMKAverage`.

"""

from collections import deque
import bisect

class MKAverage:
    def __init__(self, m: int, k: int):
        """
        Initialize the MKAverage object with parameters m and k.
        """
        self.m = m
        self.k = k
        self.stream = deque()  # To store the last m elements
        self.sorted_stream = []  # To maintain a sorted version of the stream

    def addElement(self, num: int) -> None:
        """
        Inserts a new element num into the stream.
        """
        self.stream.append(num)
        bisect.insort(self.sorted_stream, num)  # Insert num into sorted_stream while maintaining order

        # If the stream exceeds m elements, remove the oldest element
        if len(self.stream) > self.m:
            oldest = self.stream.popleft()
            index = bisect.bisect_left(self.sorted_stream, oldest)
            self.sorted_stream.pop(index)

    def calculateMKAverage(self) -> int:
        """
        Returns the MK Average for the current stream or -1 if the number of elements in the stream is less than m.
        """
        if len(self.stream) < self.m:
            return -1

        # Remove the smallest k and largest k elements
        trimmed_stream = self.sorted_stream[self.k:self.m - self.k]

        # Calculate the average of the remaining elements
        return sum(trimmed_stream) // len(trimmed_stream)


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    mkaverage = MKAverage(3, 1)
    mkaverage.addElement(3)
    mkaverage.addElement(1)
    print(mkaverage.calculateMKAverage())  # Output: -1 (less than m elements)
    mkaverage.addElement(10)
    print(mkaverage.calculateMKAverage())  # Output: 3 (remaining element is [3])

    # Test Case 2
    mkaverage.addElement(5)
    print(mkaverage.calculateMKAverage())  # Output: 5 (remaining elements are [5])

    # Test Case 3
    mkaverage = MKAverage(5, 1)
    mkaverage.addElement(1)
    mkaverage.addElement(2)
    mkaverage.addElement(3)
    mkaverage.addElement(4)
    mkaverage.addElement(5)
    print(mkaverage.calculateMKAverage())  # Output: 3 (remaining elements are [2, 3, 4])

"""
Time and Space Complexity Analysis:

1. `addElement`:
   - Insertion into `sorted_stream` using `bisect.insort` takes O(log m).
   - Removing the oldest element from `sorted_stream` takes O(log m).
   - Total time complexity: O(log m).

2. `calculateMKAverage`:
   - Slicing the sorted list takes O(m).
   - Summing the trimmed list takes O(m).
   - Total time complexity: O(m).

Overall:
- Time complexity per operation: O(m) for `calculateMKAverage`, O(log m) for `addElement`.
- Space complexity: O(m) for storing the stream and sorted_stream.

Topic: Data Structures
"""