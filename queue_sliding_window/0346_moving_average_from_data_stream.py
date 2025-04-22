"""
LeetCode Question #346: Moving Average from Data Stream

Problem Statement:
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Implement the MovingAverage class:
- MovingAverage(int size) Initializes the object with the size of the window size.
- double next(int val) Returns the moving average of the last size values of the stream.

Example:
MovingAverage m = new MovingAverage(3);
m.next(1); // return 1.0 = 1 / 1
m.next(10); // return 5.5 = (1 + 10) / 2
m.next(3); // return 4.66667 = (1 + 10 + 3) / 3
m.next(5); // return 6.0 = (10 + 3 + 5) / 3

Constraints:
- 1 <= size <= 1000
- -10^5 <= val <= 10^5
- At most 10^4 calls will be made to next.
"""

from collections import deque

class MovingAverage:
    def __init__(self, size: int):
        """
        Initialize the MovingAverage object with a fixed window size.
        """
        self.size = size
        self.window = deque()
        self.window_sum = 0

    def next(self, val: int) -> float:
        """
        Add a new value to the stream and calculate the moving average.
        """
        # Add the new value to the window
        self.window.append(val)
        self.window_sum += val

        # If the window exceeds the size, remove the oldest value
        if len(self.window) > self.size:
            self.window_sum -= self.window.popleft()

        # Calculate and return the moving average
        return self.window_sum / len(self.window)


# Example Test Cases
if __name__ == "__main__":
    m = MovingAverage(3)
    print(m.next(1))  # Output: 1.0
    print(m.next(10)) # Output: 5.5
    print(m.next(3))  # Output: 4.666666666666667
    print(m.next(5))  # Output: 6.0

"""
Time and Space Complexity Analysis:

Time Complexity:
- The `next` method performs O(1) operations for adding a value, updating the sum, and removing the oldest value if necessary.
- Therefore, the time complexity for each call to `next` is O(1).

Space Complexity:
- The space complexity is O(size), where `size` is the maximum number of elements in the sliding window.
- The `deque` stores at most `size` elements, and the integer `window_sum` uses constant space.

Topic: Queue, Sliding Window
"""