"""
LeetCode Question #232: Implement Queue using Stacks

Problem Statement:
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, pop, peek, and empty).

Implement the MyQueue class:
- void push(int x) Pushes element x to the back of the queue.
- int pop() Removes the element from the front of the queue and returns it.
- int peek() Returns the element at the front of the queue.
- boolean empty() Returns true if the queue is empty, false otherwise.

Notes:
- You must use only standard operations of a stack, which means only `push to top`, `peek/pop from top`, `size`, and `is empty` operations are valid.
- Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue), as long as you use only standard stack operations.

Constraints:
- 1 <= x <= 10^9
- At most 100 calls will be made to push, pop, peek, and empty.
"""

# Solution
class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.input_stack = []  # Stack used for push operations
        self.output_stack = []  # Stack used for pop/peek operations

    def push(self, x: int) -> None:
        """
        Push element x to the back of the queue.
        """
        self.input_stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from the front of the queue and returns it.
        """
        self._transfer_if_needed()
        return self.output_stack.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        self._transfer_if_needed()
        return self.output_stack[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.input_stack and not self.output_stack

    def _transfer_if_needed(self) -> None:
        """
        Transfer elements from input_stack to output_stack if output_stack is empty.
        """
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())

# Example Test Cases
if __name__ == "__main__":
    # Initialize the queue
    queue = MyQueue()

    # Test push operation
    queue.push(1)
    queue.push(2)
    queue.push(3)

    # Test peek operation
    assert queue.peek() == 1  # Front element is 1

    # Test pop operation
    assert queue.pop() == 1  # Removes and returns the front element (1)
    assert queue.pop() == 2  # Removes and returns the front element (2)

    # Test empty operation
    assert not queue.empty()  # Queue is not empty

    # Test pop operation again
    assert queue.pop() == 3  # Removes and returns the front element (3)

    # Test empty operation again
    assert queue.empty()  # Queue is now empty

    print("All test cases passed!")

"""
Time and Space Complexity Analysis:

1. push(x):
   - Time Complexity: O(1) - Adding an element to the top of the input stack is a constant-time operation.
   - Space Complexity: O(1) - No additional space is used beyond the input stack.

2. pop():
   - Time Complexity: O(n) in the worst case - If the output stack is empty, all elements from the input stack are transferred to the output stack. Otherwise, popping from the output stack is O(1).
   - Space Complexity: O(1) - No additional space is used beyond the two stacks.

3. peek():
   - Time Complexity: O(n) in the worst case - Similar to pop(), transferring elements from the input stack to the output stack may be required.
   - Space Complexity: O(1) - No additional space is used beyond the two stacks.

4. empty():
   - Time Complexity: O(1) - Checking whether both stacks are empty is a constant-time operation.
   - Space Complexity: O(1) - No additional space is used.

Overall Space Complexity:
- O(n) - The total space used by the two stacks is proportional to the number of elements in the queue.

Topic: Stack
"""