"""
LeetCode Problem #2665: Counter II

Problem Statement:
Write a class `Counter` that simulates a counter with the following methods:
1. `increment()`: Increments the counter by 1 and returns the updated value.
2. `decrement()`: Decrements the counter by 1 and returns the updated value.
3. `reset()`: Resets the counter to its initial value and returns the updated value.

The class should be initialized with an integer `initialValue` which represents the starting value of the counter.

Example:
    counter = Counter(5)  # Initialize the counter with initial value 5
    counter.increment()   # Returns 6
    counter.reset()       # Returns 5
    counter.decrement()   # Returns 4
"""

class Counter:
    def __init__(self, initialValue: int):
        """
        Initialize the counter with the given initial value.
        """
        self.initialValue = initialValue
        self.currentValue = initialValue

    def increment(self) -> int:
        """
        Increment the counter by 1 and return the updated value.
        """
        self.currentValue += 1
        return self.currentValue

    def decrement(self) -> int:
        """
        Decrement the counter by 1 and return the updated value.
        """
        self.currentValue -= 1
        return self.currentValue

    def reset(self) -> int:
        """
        Reset the counter to its initial value and return the updated value.
        """
        self.currentValue = self.initialValue
        return self.currentValue


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    counter = Counter(5)
    print(counter.increment())  # Output: 6
    print(counter.reset())      # Output: 5
    print(counter.decrement())  # Output: 4

    # Test Case 2
    counter = Counter(0)
    print(counter.increment())  # Output: 1
    print(counter.increment())  # Output: 2
    print(counter.reset())      # Output: 0
    print(counter.decrement())  # Output: -1

    # Test Case 3
    counter = Counter(-10)
    print(counter.increment())  # Output: -9
    print(counter.decrement())  # Output: -10
    print(counter.reset())      # Output: -10


"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - All methods (`increment`, `decrement`, `reset`) perform constant-time operations.
   - Therefore, the time complexity for each method is O(1).

2. Space Complexity:
   - The class stores two integer variables (`initialValue` and `currentValue`).
   - The space complexity is O(1).

Topic: Design
"""