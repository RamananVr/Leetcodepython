"""
LeetCode Problem #155: Min Stack

Problem Statement:
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:
- MinStack() initializes the stack object.
- void push(int val) pushes the element val onto the stack.
- void pop() removes the element on the top of the stack.
- int top() gets the top element of the stack.
- int getMin() retrieves the minimum element in the stack.

Constraints:
- Methods pop, top, and getMin operations will always be called on non-empty stacks.
- -2^31 <= val <= 2^31 - 1
"""

class MinStack:
    def __init__(self):
        """
        Initialize the stack and a helper stack to track the minimum values.
        """
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        """
        Push the value onto the stack and update the min_stack.
        """
        self.stack.append(val)
        # Update the min_stack with the new minimum value
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        """
        Remove the top element from the stack and update the min_stack.
        """
        if self.stack:
            top = self.stack.pop()
            if top == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        """
        Get the top element of the stack.
        """
        return self.stack[-1]

    def getMin(self) -> int:
        """
        Retrieve the minimum element in the stack.
        """
        return self.min_stack[-1]


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    assert min_stack.getMin() == -3  # Minimum is -3
    min_stack.pop()
    assert min_stack.top() == 0     # Top is 0
    assert min_stack.getMin() == -2 # Minimum is -2

    # Test Case 2
    min_stack = MinStack()
    min_stack.push(5)
    min_stack.push(3)
    min_stack.push(7)
    assert min_stack.getMin() == 3  # Minimum is 3
    min_stack.pop()
    assert min_stack.getMin() == 3  # Minimum is still 3
    min_stack.pop()
    assert min_stack.getMin() == 5  # Minimum is now 5

    print("All test cases passed!")

"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - push(val): O(1) - Adding an element to the stack and updating the min_stack is constant time.
   - pop(): O(1) - Removing the top element and updating the min_stack is constant time.
   - top(): O(1) - Accessing the top element is constant time.
   - getMin(): O(1) - Accessing the minimum element is constant time.

2. Space Complexity:
   - The space complexity is O(n), where n is the number of elements in the stack. This is because we maintain two stacks: 
     one for the actual elements and another for tracking the minimum values.

Topic: Stack
"""