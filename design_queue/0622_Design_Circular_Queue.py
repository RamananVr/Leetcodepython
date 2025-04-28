"""
LeetCode Problem #622: Design Circular Queue

Problem Statement:
Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle, and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

Your implementation should support the following operations:
- `MyCircularQueue(k)`: Constructor, sets the size of the queue to be `k`.
- `enQueue(value)`: Inserts an element into the circular queue. Return `true` if the operation is successful.
- `deQueue()`: Deletes an element from the circular queue. Return `true` if the operation is successful.
- `Front()`: Gets the front item from the queue. If the queue is empty, return `-1`.
- `Rear()`: Gets the last item from the queue. If the queue is empty, return `-1`.
- `isEmpty()`: Checks whether the circular queue is empty or not.
- `isFull()`: Checks whether the circular queue is full or not.

Constraints:
- All values will be in the range of 0 to 1000.
- The number of operations will be in the range of 1 to 1000.
- Please do not use the built-in queue library.

"""

class MyCircularQueue:
    def __init__(self, k: int):
        """
        Initialize the circular queue with a fixed size k.
        """
        self.queue = [0] * k
        self.head = -1
        self.tail = -1
        self.size = k

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return True if successful.
        """
        if self.isFull():
            return False
        if self.isEmpty():
            self.head = 0
        self.tail = (self.tail + 1) % self.size
        self.queue[self.tail] = value
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return True if successful.
        """
        if self.isEmpty():
            return False
        if self.head == self.tail:
            self.head = -1
            self.tail = -1
        else:
            self.head = (self.head + 1) % self.size
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue. Return -1 if the queue is empty.
        """
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        """
        Get the last item from the queue. Return -1 if the queue is empty.
        """
        if self.isEmpty():
            return -1
        return self.queue[self.tail]

    def isEmpty(self) -> bool:
        """
        Check whether the circular queue is empty.
        """
        return self.head == -1

    def isFull(self) -> bool:
        """
        Check whether the circular queue is full.
        """
        return (self.tail + 1) % self.size == self.head


# Example Test Cases
if __name__ == "__main__":
    # Initialize a circular queue with size 3
    circularQueue = MyCircularQueue(3)
    assert circularQueue.enQueue(1) == True  # Insert 1, returns True
    assert circularQueue.enQueue(2) == True  # Insert 2, returns True
    assert circularQueue.enQueue(3) == True  # Insert 3, returns True
    assert circularQueue.enQueue(4) == False  # Queue is full, returns False
    assert circularQueue.Rear() == 3  # Last element is 3
    assert circularQueue.isFull() == True  # Queue is full
    assert circularQueue.deQueue() == True  # Remove 1, returns True
    assert circularQueue.enQueue(4) == True  # Insert 4, returns True
    assert circularQueue.Rear() == 4  # Last element is 4
    assert circularQueue.Front() == 2  # First element is 2
    assert circularQueue.isEmpty() == False  # Queue is not empty
    print("All test cases passed!")

"""
Time Complexity:
- enQueue: O(1) - Insertion is done in constant time.
- deQueue: O(1) - Deletion is done in constant time.
- Front: O(1) - Accessing the front element is constant time.
- Rear: O(1) - Accessing the rear element is constant time.
- isEmpty: O(1) - Checking if the queue is empty is constant time.
- isFull: O(1) - Checking if the queue is full is constant time.

Space Complexity:
- O(k) - The queue uses an array of size k to store elements.

Topic: Design, Queue
"""