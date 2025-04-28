"""
LeetCode Question #1172: Dinner Plate Stacks

Problem Statement:
You have an infinite number of stacks arranged in a row and numbered (0, 1, 2, ...). You can perform the following operations:

1. `push(val)`:
   Push the given integer `val` onto the leftmost stack with size less than `capacity`.

2. `pop()`:
   Remove the top element from the rightmost non-empty stack and return it. If all stacks are empty, return -1.

3. `popAtStack(index)`:
   Remove the top element from the stack with the given index and return it. If the stack with the given index is empty, return -1.

Implement the `DinnerPlates` class:
- `DinnerPlates(int capacity)` Initializes the object with the maximum capacity of each stack.
- `void push(int val)` Pushes the given integer `val` onto the leftmost stack with size less than `capacity`.
- `int pop()` Removes the top element from the rightmost non-empty stack and returns it. If all stacks are empty, return -1.
- `int popAtStack(int index)` Removes the top element from the stack with the given index and returns it. If the stack with the given index is empty, return -1.

Constraints:
- 1 <= capacity <= 2 * 10^4
- 1 <= val <= 2 * 10^4
- 0 <= index <= 10^5
- At most 2 * 10^4 calls will be made to `push`, `pop`, and `popAtStack`.

"""

from sortedcontainers import SortedSet

class DinnerPlates:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacks = []
        self.available = SortedSet()  # Tracks indices of stacks with space available

    def push(self, val: int) -> None:
        # If no stack has space, create a new stack
        if not self.available:
            self.stacks.append([])
            self.available.add(len(self.stacks) - 1)
        
        # Push the value onto the leftmost stack with space
        index = self.available[0]
        self.stacks[index].append(val)
        
        # If the stack is now full, remove it from the available set
        if len(self.stacks[index]) == self.capacity:
            self.available.remove(index)

    def pop(self) -> int:
        # Remove from the rightmost non-empty stack
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()
        
        if not self.stacks:
            return -1
        
        val = self.stacks[-1].pop()
        
        # If the stack is not full, add it to the available set
        if len(self.stacks[-1]) < self.capacity:
            self.available.add(len(self.stacks) - 1)
        
        return val

    def popAtStack(self, index: int) -> int:
        # If the index is out of bounds or the stack is empty, return -1
        if index >= len(self.stacks) or not self.stacks[index]:
            return -1
        
        val = self.stacks[index].pop()
        
        # If the stack is not full, add it to the available set
        if len(self.stacks[index]) < self.capacity:
            self.available.add(index)
        
        return val


# Example Test Cases
if __name__ == "__main__":
    # Initialize DinnerPlates with capacity 2
    dp = DinnerPlates(2)
    
    # Push values
    dp.push(1)
    dp.push(2)
    dp.push(3)
    dp.push(4)
    dp.push(5)
    
    # PopAtStack
    print(dp.popAtStack(0))  # Output: 2
    print(dp.popAtStack(0))  # Output: 1
    print(dp.popAtStack(0))  # Output: -1
    
    # Pop
    print(dp.pop())  # Output: 5
    print(dp.pop())  # Output: 4
    print(dp.pop())  # Output: 3
    print(dp.pop())  # Output: -1


"""
Time and Space Complexity Analysis:

1. `push(val)`:
   - Time Complexity: O(log N), where N is the number of stacks, due to the use of SortedSet for tracking available stacks.
   - Space Complexity: O(N), where N is the number of stacks.

2. `pop()`:
   - Time Complexity: O(1) amortized, as we directly access the last stack.
   - Space Complexity: O(1).

3. `popAtStack(index)`:
   - Time Complexity: O(log N), where N is the number of stacks, due to the use of SortedSet for tracking available stacks.
   - Space Complexity: O(1).

Overall Space Complexity:
- O(N * capacity), where N is the number of stacks and `capacity` is the maximum size of each stack.

Topic: Data Structures (Stacks, SortedSet)
"""