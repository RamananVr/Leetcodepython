"""
LeetCode Question #716: Max Stack

Problem Statement:
Design a max stack data structure that supports the following operations:

1. `push(x)` - Push element x onto the stack.
2. `pop()` - Remove the element on top of the stack and return it.
3. `top()` - Get the element on the top of the stack.
4. `peekMax()` - Retrieve the maximum element in the stack.
5. `popMax()` - Retrieve the maximum element in the stack, remove it, and return it. If there are multiple elements with the same maximum value, only remove the one closest to the top of the stack.

Implement the MaxStack class:
- `MaxStack()` Initializes the stack object.
- `void push(int x)` Pushes the element x onto the stack.
- `int pop()` Removes the element on the top of the stack and returns it.
- `int top()` Returns the element on the top of the stack.
- `int peekMax()` Retrieves the maximum element in the stack.
- `int popMax()` Retrieves the maximum element in the stack, removes it, and returns it.

Constraints:
- -10^7 <= x <= 10^7
- At most 10^4 calls will be made to `push`, `pop`, `top`, `peekMax`, and `popMax`.
"""

class MaxStack:
    def __init__(self):
        # Stack to store elements
        self.stack = []
        # Stack to store maximums
        self.max_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        # Update max_stack with the new maximum
        if not self.max_stack or x >= self.max_stack[-1]:
            self.max_stack.append(x)

    def pop(self) -> int:
        if not self.stack:
            return None
        top = self.stack.pop()
        # Remove from max_stack if the popped element is the current maximum
        if top == self.max_stack[-1]:
            self.max_stack.pop()
        return top

    def top(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1]

    def peekMax(self) -> int:
        if not self.max_stack:
            return None
        return self.max_stack[-1]

    def popMax(self) -> int:
        if not self.max_stack:
            return None
        max_val = self.max_stack[-1]
        buffer = []
        # Remove elements from stack until we find the max value
        while self.stack[-1] != max_val:
            buffer.append(self.stack.pop())
        # Remove the max value
        self.stack.pop()
        self.max_stack.pop()
        # Push back the elements in the buffer
        while buffer:
            self.push(buffer.pop())
        return max_val


# Example Test Cases
if __name__ == "__main__":
    max_stack = MaxStack()
    
    # Test Case 1: Basic operations
    max_stack.push(5)
    max_stack.push(1)
    max_stack.push(5)
    assert max_stack.top() == 5  # Top element is 5
    assert max_stack.popMax() == 5  # Max element is 5, remove it
    assert max_stack.top() == 1  # Top element is now 1
    assert max_stack.peekMax() == 5  # Max element is 5
    assert max_stack.pop() == 1  # Remove top element
    assert max_stack.top() == 5  # Top element is now 5

    # Test Case 2: Edge case with single element
    max_stack.push(10)
    assert max_stack.peekMax() == 10  # Max element is 10
    assert max_stack.popMax() == 10  # Remove max element
    assert max_stack.top() == None  # Stack is empty

    print("All test cases passed!")

"""
Time and Space Complexity Analysis:

1. `push(x)`:
   - Time Complexity: O(1) (Appending to both stacks is constant time)
   - Space Complexity: O(1) (No additional space used beyond the input)

2. `pop()`:
   - Time Complexity: O(1) (Removing the top element is constant time)
   - Space Complexity: O(1) (No additional space used)

3. `top()`:
   - Time Complexity: O(1) (Accessing the top element is constant time)
   - Space Complexity: O(1) (No additional space used)

4. `peekMax()`:
   - Time Complexity: O(1) (Accessing the top of max_stack is constant time)
   - Space Complexity: O(1) (No additional space used)

5. `popMax()`:
   - Time Complexity: O(n) (In the worst case, we may need to traverse the entire stack to find the max element)
   - Space Complexity: O(n) (Buffer stack may store up to n elements temporarily)

Overall Space Complexity:
- O(n) for the `stack` and `max_stack`, where n is the number of elements in the stack.

Topic: Stack