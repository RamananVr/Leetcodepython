"""
LeetCode Question #225: Implement Stack using Queues

Problem Statement:
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:
- `void push(int x)` Pushes element x to the top of the stack.
- `int pop()` Removes the element on the top of the stack and returns it.
- `int top()` Returns the element on the top of the stack.
- `boolean empty()` Returns true if the stack is empty, false otherwise.

Notes:
- You must use only standard operations of a queue, which means only `push to back`, `peek/pop from front`, `size`, and `is empty` operations are valid.
- Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
- You may assume that all operations are valid (e.g., no calls to `pop` or `top` on an empty stack).

Constraints:
- 1 <= x <= 100
- At most 100 calls will be made to `push`, `pop`, `top`, and `empty`.
- All the calls to `pop` and `top` are valid.

"""

from collections import deque

class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.append(x)
        # Rotate the queue to make the last element the front
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queue.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.queue


# Example Test Cases
if __name__ == "__main__":
    # Initialize stack
    stack = MyStack()

    # Test push operation
    stack.push(1)
    stack.push(2)
    print(stack.top())  # Output: 2 (top element is 2)

    # Test pop operation
    print(stack.pop())  # Output: 2 (removes and returns the top element)
    print(stack.top())  # Output: 1 (top element is now 1)

    # Test empty operation
    print(stack.empty())  # Output: False (stack is not empty)
    stack.pop()           # Remove the last element
    print(stack.empty())  # Output: True (stack is now empty)


"""
Time and Space Complexity Analysis:

1. `push(x)`:
   - Time Complexity: O(n), where n is the number of elements in the queue. This is because we rotate the queue to ensure the last pushed element is at the front.
   - Space Complexity: O(1), as we are not using any additional data structures.

2. `pop()`:
   - Time Complexity: O(1), as we simply remove the front element of the queue.
   - Space Complexity: O(1), as no additional space is used.

3. `top()`:
   - Time Complexity: O(1), as we directly access the front element of the queue.
   - Space Complexity: O(1), as no additional space is used.

4. `empty()`:
   - Time Complexity: O(1), as we simply check if the queue is empty.
   - Space Complexity: O(1), as no additional space is used.

Overall:
- Time Complexity: O(n) for `push`, O(1) for `pop`, `top`, and `empty`.
- Space Complexity: O(n), where n is the number of elements in the stack (stored in the queue).

Topic: Stack, Queue
"""