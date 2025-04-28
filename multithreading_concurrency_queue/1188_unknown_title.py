"""
LeetCode Problem #1188: Design Bounded Blocking Queue

Problem Statement:
Implement a thread-safe bounded blocking queue that has the following methods:

1. `BoundedBlockingQueue(int capacity)` Initializes the queue with a maximum capacity.
2. `void enqueue(int element)` Adds an element to the queue. If the queue is full, the calling thread is blocked until the queue is no longer full.
3. `int dequeue()` Removes and returns the front element of the queue. If the queue is empty, the calling thread is blocked until the queue is no longer empty.
4. `int size()` Returns the number of elements currently in the queue.

Your implementation should be thread-safe, meaning that multiple threads can call these methods concurrently.

Constraints:
- The number of threads accessing the queue can be very large.
- The methods `enqueue`, `dequeue`, and `size` should all run in constant time.

Example:
BoundedBlockingQueue queue = new BoundedBlockingQueue(2); // Initialize with capacity 2.
queue.enqueue(1);
queue.enqueue(2);
queue.dequeue(); // Returns 1.
queue.enqueue(3);
queue.size(); // Returns 2.

"""

import threading
from collections import deque

class BoundedBlockingQueue:
    def __init__(self, capacity: int):
        """
        Initialize the bounded blocking queue with a given capacity.
        """
        self.capacity = capacity
        self.queue = deque()
        self.lock = threading.Lock()
        self.not_empty = threading.Condition(self.lock)
        self.not_full = threading.Condition(self.lock)

    def enqueue(self, element: int) -> None:
        """
        Add an element to the queue. Block if the queue is full.
        """
        with self.not_full:
            while len(self.queue) == self.capacity:
                self.not_full.wait()
            self.queue.append(element)
            self.not_empty.notify()

    def dequeue(self) -> int:
        """
        Remove and return the front element of the queue. Block if the queue is empty.
        """
        with self.not_empty:
            while len(self.queue) == 0:
                self.not_empty.wait()
            element = self.queue.popleft()
            self.not_full.notify()
            return element

    def size(self) -> int:
        """
        Return the number of elements currently in the queue.
        """
        with self.lock:
            return len(self.queue)


# Example Test Cases
if __name__ == "__main__":
    import threading
    import time

    def test_enqueue_dequeue():
        queue = BoundedBlockingQueue(2)
        queue.enqueue(1)
        queue.enqueue(2)
        print(queue.dequeue())  # Expected: 1
        queue.enqueue(3)
        print(queue.size())     # Expected: 2

    def test_multithreading():
        queue = BoundedBlockingQueue(3)

        def producer():
            for i in range(5):
                queue.enqueue(i)
                print(f"Enqueued: {i}")
                time.sleep(0.1)

        def consumer():
            for _ in range(5):
                item = queue.dequeue()
                print(f"Dequeued: {item}")
                time.sleep(0.2)

        producer_thread = threading.Thread(target=producer)
        consumer_thread = threading.Thread(target=consumer)

        producer_thread.start()
        consumer_thread.start()

        producer_thread.join()
        consumer_thread.join()

    # Run test cases
    print("Test Case 1: Basic enqueue and dequeue")
    test_enqueue_dequeue()

    print("\nTest Case 2: Multithreading")
    test_multithreading()


"""
Time and Space Complexity Analysis:

1. `enqueue`:
   - Time Complexity: O(1) (appending to the deque is constant time).
   - Space Complexity: O(1) (no additional space used).

2. `dequeue`:
   - Time Complexity: O(1) (removing from the front of the deque is constant time).
   - Space Complexity: O(1) (no additional space used).

3. `size`:
   - Time Complexity: O(1) (getting the length of the deque is constant time).
   - Space Complexity: O(1) (no additional space used).

Overall:
- Time Complexity: O(1) for all operations.
- Space Complexity: O(n), where n is the capacity of the queue.

Topic: Multithreading, Concurrency, Queue
"""