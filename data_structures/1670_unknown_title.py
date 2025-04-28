"""
LeetCode Problem #1670: Design Front Middle Back Queue

Problem Statement:
Design a queue that supports push and pop operations in the front, middle, and back.

Implement the FrontMiddleBackQueue class:
- FrontMiddleBackQueue() Initializes the queue.
- void pushFront(int val) Adds val to the front of the queue.
- void pushMiddle(int val) Adds val to the middle of the queue.
- void pushBack(int val) Adds val to the back of the queue.
- int popFront() Removes the front element of the queue and returns it. If the queue is empty, return -1.
- int popMiddle() Removes the middle element of the queue and returns it. If the queue is empty, return -1.
- int popBack() Removes the back element of the queue and returns it. If the queue is empty, return -1.

Note:
- When there are two middle elements, the operation is performed on the first middle element.

Constraints:
- 1 <= val <= 10^9
- At most 1000 calls will be made to pushFront, pushMiddle, pushBack, popFront, popMiddle, and popBack.
"""

# Solution
class FrontMiddleBackQueue:
    def __init__(self):
        self.queue = []

    def pushFront(self, val: int) -> None:
        self.queue.insert(0, val)

    def pushMiddle(self, val: int) -> None:
        middle = len(self.queue) // 2
        self.queue.insert(middle, val)

    def pushBack(self, val: int) -> None:
        self.queue.append(val)

    def popFront(self) -> int:
        if not self.queue:
            return -1
        return self.queue.pop(0)

    def popMiddle(self) -> int:
        if not self.queue:
            return -1
        middle = (len(self.queue) - 1) // 2
        return self.queue.pop(middle)

    def popBack(self) -> int:
        if not self.queue:
            return -1
        return self.queue.pop()

# Example Test Cases
if __name__ == "__main__":
    # Initialize the queue
    q = FrontMiddleBackQueue()

    # Test push operations
    q.pushFront(1)  # Queue: [1]
    q.pushBack(2)   # Queue: [1, 2]
    q.pushMiddle(3) # Queue: [1, 3, 2]
    q.pushMiddle(4) # Queue: [1, 4, 3, 2]

    # Test pop operations
    print(q.popFront())  # Output: 1, Queue: [4, 3, 2]
    print(q.popMiddle()) # Output: 4, Queue: [3, 2]
    print(q.popMiddle()) # Output: 3, Queue: [2]
    print(q.popBack())   # Output: 2, Queue: []
    print(q.popFront())  # Output: -1, Queue is empty

"""
Time and Space Complexity Analysis:
1. pushFront(val): 
   - Time Complexity: O(n) (due to list insertion at index 0)
   - Space Complexity: O(1)

2. pushMiddle(val): 
   - Time Complexity: O(n) (due to list insertion at the middle index)
   - Space Complexity: O(1)

3. pushBack(val): 
   - Time Complexity: O(1) (appending to the end of the list)
   - Space Complexity: O(1)

4. popFront(): 
   - Time Complexity: O(n) (due to list removal at index 0)
   - Space Complexity: O(1)

5. popMiddle(): 
   - Time Complexity: O(n) (due to list removal at the middle index)
   - Space Complexity: O(1)

6. popBack(): 
   - Time Complexity: O(1) (removing the last element of the list)
   - Space Complexity: O(1)

Overall Space Complexity: O(n), where n is the number of elements in the queue.

Topic: Data Structures
"""