"""
LeetCode Problem #2590: Design a Stack With Increment Operation

Problem Statement:
Design a stack that supports increment operations on its elements.

Implement the `CustomStack` class:
- `CustomStack(int maxSize)` Initializes the object with `maxSize` which is the maximum number of elements in the stack or do nothing if the stack reached the `maxSize`.
- `void push(int x)` Adds `x` to the top of the stack if the stack hasn't reached the `maxSize`.
- `int pop()` Removes and returns the element on the top of the stack or returns `-1` if the stack is empty.
- `void increment(int k, int val)` Increments the bottom `k` elements of the stack by `val`. If there are fewer than `k` elements in the stack, increment all the elements in the stack.

Constraints:
- `1 <= maxSize <= 1000`
- `1 <= x <= 100`
- `1 <= k <= 1000`
- `0 <= val <= 100`
- At most `1000` calls will be made to each of `push`, `pop`, and `increment`.

"""

class CustomStack:
    def __init__(self, maxSize: int):
        """
        Initialize the stack with a maximum size.
        """
        self.stack = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        """
        Push an element onto the stack if it hasn't reached the max size.
        """
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        """
        Pop the top element from the stack. Return -1 if the stack is empty.
        """
        if not self.stack:
            return -1
        return self.stack.pop()

    def increment(self, k: int, val: int) -> None:
        """
        Increment the bottom k elements of the stack by val.
        """
        for i in range(min(k, len(self.stack))):
            self.stack[i] += val


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    customStack = CustomStack(3)  # Stack is Empty []
    customStack.push(1)           # Stack becomes [1]
    customStack.push(2)           # Stack becomes [1, 2]
    assert customStack.pop() == 2 # Returns 2, Stack becomes [1]
    customStack.push(2)           # Stack becomes [1, 2]
    customStack.push(3)           # Stack becomes [1, 2, 3]
    customStack.push(4)           # Stack still [1, 2, 3], maxSize is 3
    customStack.increment(5, 100) # Stack becomes [101, 102, 103]
    customStack.increment(2, 100) # Stack becomes [201, 202, 103]
    assert customStack.pop() == 103 # Returns 103, Stack becomes [201, 202]
    assert customStack.pop() == 202 # Returns 202, Stack becomes [201]
    assert customStack.pop() == 201 # Returns 201, Stack becomes []
    assert customStack.pop() == -1  # Returns -1, Stack is empty

    # Test Case 2
    customStack = CustomStack(1)  # Stack is Empty []
    customStack.push(10)          # Stack becomes [10]
    customStack.push(20)          # Stack still [10], maxSize is 1
    customStack.increment(1, 5)   # Stack becomes [15]
    assert customStack.pop() == 15 # Returns 15, Stack becomes []
    assert customStack.pop() == -1 # Returns -1, Stack is empty

    print("All test cases passed!")

"""
Time Complexity Analysis:
- `push`: O(1) - Appending to the stack is an O(1) operation.
- `pop`: O(1) - Removing the last element from the stack is an O(1) operation.
- `increment`: O(k) - Incrementing the bottom `k` elements requires iterating over up to `k` elements.

Space Complexity:
- O(n) - The stack can hold up to `maxSize` elements, where `n = maxSize`.

Topic: Stack
"""