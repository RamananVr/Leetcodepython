"""
LeetCode Question #1381: Design a Stack With Increment Operation

Problem Statement:
Design a stack which supports the following operations.

Implement the `CustomStack` class:
- `CustomStack(int maxSize)` Initializes the object with `maxSize` which is the maximum number of elements in the stack or do nothing if the stack reached the `maxSize`.
- `void push(int x)` Adds `x` to the top of the stack if the stack hasn't reached the `maxSize`.
- `int pop()` Removes and returns the top of the stack or `-1` if the stack is empty.
- `void increment(int k, int val)` Increments the bottom `k` elements of the stack by `val`. If there are less than `k` elements in the stack, increment all the elements in the stack.

Constraints:
- `1 <= maxSize <= 1000`
- `1 <= x <= 1000`
- `0 <= k <= 1000`
- `0 <= val <= 1000`
- At most `1000` calls will be made to each method.
"""

# Solution
class CustomStack:
    def __init__(self, maxSize: int):
        """
        Initialize the stack with a maximum size.
        """
        self.stack = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        """
        Push an element onto the stack if it hasn't reached the maximum size.
        """
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        """
        Pop the top element from the stack. Return -1 if the stack is empty.
        """
        if self.stack:
            return self.stack.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        """
        Increment the bottom k elements of the stack by val.
        """
        for i in range(min(k, len(self.stack))):
            self.stack[i] += val


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    customStack = CustomStack(3)  # Stack is Empty, maxSize = 3
    customStack.push(1)           # Stack becomes [1]
    customStack.push(2)           # Stack becomes [1, 2]
    print(customStack.pop())      # Returns 2, Stack becomes [1]
    customStack.push(2)           # Stack becomes [1, 2]
    customStack.push(3)           # Stack becomes [1, 2, 3]
    customStack.push(4)           # Stack is full, no operation performed
    customStack.increment(5, 100) # Increment all elements by 100, Stack becomes [101, 102, 103]
    customStack.increment(2, 50)  # Increment bottom 2 elements by 50, Stack becomes [151, 152, 103]
    print(customStack.pop())      # Returns 103, Stack becomes [151, 152]
    print(customStack.pop())      # Returns 152, Stack becomes [151]
    print(customStack.pop())      # Returns 151, Stack becomes []
    print(customStack.pop())      # Returns -1, Stack is empty

    # Test Case 2
    customStack2 = CustomStack(1)  # Stack is Empty, maxSize = 1
    customStack2.push(10)          # Stack becomes [10]
    customStack2.push(20)          # Stack is full, no operation performed
    customStack2.increment(1, 5)   # Increment bottom 1 element by 5, Stack becomes [15]
    print(customStack2.pop())      # Returns 15, Stack becomes []
    print(customStack2.pop())      # Returns -1, Stack is empty


# Time and Space Complexity Analysis
"""
Time Complexity:
- `push`: O(1) - Adding an element to the stack takes constant time.
- `pop`: O(1) - Removing the top element from the stack takes constant time.
- `increment`: O(k) - Incrementing the bottom k elements takes linear time proportional to k.

Space Complexity:
- O(n) - The stack can store up to `maxSize` elements, where n = maxSize.

Overall, the solution is efficient given the constraints.
"""

# Topic: Stack