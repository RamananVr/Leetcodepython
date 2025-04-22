"""
LeetCode Question #641: Design Circular Deque

Problem Statement:
Design your implementation of the circular double-ended queue (deque).

Implement the MyCircularDeque class:
- MyCircularDeque(int k) Initializes the deque with a maximum size of k.
- boolean insertFront() Adds an item at the front of the deque. Returns true if the operation is successful, or false if the deque is full.
- boolean insertLast() Adds an item at the rear of the deque. Returns true if the operation is successful, or false if the deque is full.
- boolean deleteFront() Deletes an item from the front of the deque. Returns true if the operation is successful, or false if the deque is empty.
- boolean deleteLast() Deletes an item from the rear of the deque. Returns true if the operation is successful, or false if the deque is empty.
- int getFront() Returns the front item from the deque. Returns -1 if the deque is empty.
- int getRear() Returns the last item from the deque. Returns -1 if the deque is empty.
- boolean isEmpty() Returns true if the deque is empty, or false otherwise.
- boolean isFull() Returns true if the deque is full, or false otherwise.

Constraints:
- 1 <= k <= 1000
- 0 <= value <= 1000
- At most 2000 calls will be made to insertFront, insertLast, deleteFront, deleteLast, getFront, getRear, isEmpty, isFull.
"""

class MyCircularDeque:
    def __init__(self, k: int):
        """
        Initialize the deque with a maximum size of k.
        """
        self.capacity = k
        self.deque = [None] * k
        self.front = -1
        self.rear = -1
        self.size = 0

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of the deque.
        """
        if self.isFull():
            return False
        if self.isEmpty():
            self.front = self.rear = 0
        else:
            self.front = (self.front - 1) % self.capacity
        self.deque[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of the deque.
        """
        if self.isFull():
            return False
        if self.isEmpty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity
        self.deque[self.rear] = value
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of the deque.
        """
        if self.isEmpty():
            return False
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of the deque.
        """
        if self.isEmpty():
            return False
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.rear = (self.rear - 1) % self.capacity
        self.size -= 1
        return True

    def getFront(self) -> int:
        """
        Returns the front item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.deque[self.front]

    def getRear(self) -> int:
        """
        Returns the last item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.deque[self.rear]

    def isEmpty(self) -> bool:
        """
        Returns true if the deque is empty.
        """
        return self.size == 0

    def isFull(self) -> bool:
        """
        Returns true if the deque is full.
        """
        return self.size == self.capacity


# Example Test Cases
if __name__ == "__main__":
    # Initialize deque with capacity 3
    circularDeque = MyCircularDeque(3)
    
    # Test insertLast
    assert circularDeque.insertLast(1) == True  # [1]
    assert circularDeque.insertLast(2) == True  # [1, 2]
    assert circularDeque.insertLast(3) == True  # [1, 2, 3]
    assert circularDeque.insertLast(4) == False # Deque is full
    
    # Test getRear
    assert circularDeque.getRear() == 3
    
    # Test isFull
    assert circularDeque.isFull() == True
    
    # Test deleteLast
    assert circularDeque.deleteLast() == True  # [1, 2]
    
    # Test insertFront
    assert circularDeque.insertFront(4) == True # [4, 1, 2]
    
    # Test getFront
    assert circularDeque.getFront() == 4
    
    # Test deleteFront
    assert circularDeque.deleteFront() == True  # [1, 2]
    
    # Test isEmpty
    assert circularDeque.isEmpty() == False
    
    print("All test cases passed!")

"""
Time Complexity Analysis:
- insertFront, insertLast, deleteFront, deleteLast, getFront, getRear, isEmpty, isFull: O(1)
  Each operation involves constant-time arithmetic and array indexing.

Space Complexity Analysis:
- Space complexity: O(k), where k is the capacity of the deque. The deque uses an array of size k.

Topic: Design, Queue
"""