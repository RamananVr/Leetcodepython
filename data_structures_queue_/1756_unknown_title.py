"""
LeetCode Problem #1756: Design Most Recently Used Queue

Problem Statement:
Design a queue-like data structure that moves the most recently used (MRU) element to the end of the queue. 
Implement the MRUQueue class:

1. MRUQueue(int n) Initializes the queue to contain the integers in the range [1, n] (inclusive) in increasing order.
2. int fetch(int k) Moves the kth element (1-indexed) to the end of the queue and returns it.

Constraints:
- 1 <= n <= 2000
- 1 <= k <= the current size of the queue
- At most 2000 calls will be made to fetch.

Example:
Input:
["MRUQueue", "fetch", "fetch", "fetch", "fetch"]
[[8], [3], [5], [2], [8]]
Output:
[null, 3, 6, 2, 2]

Explanation:
MRUQueue mruQueue = new MRUQueue(8); // Initializes the queue [1, 2, 3, 4, 5, 6, 7, 8].
mruQueue.fetch(3); // Moves the 3rd element (3) to the end of the queue. Returns 3. Queue becomes [1, 2, 4, 5, 6, 7, 8, 3].
mruQueue.fetch(5); // Moves the 5th element (6) to the end of the queue. Returns 6. Queue becomes [1, 2, 4, 5, 7, 8, 3, 6].
mruQueue.fetch(2); // Moves the 2nd element (2) to the end of the queue. Returns 2. Queue becomes [1, 4, 5, 7, 8, 3, 6, 2].
mruQueue.fetch(8); // Moves the 8th element (2) to the end of the queue. Returns 2. Queue becomes [1, 4, 5, 7, 8, 3, 6, 2].
"""

from collections import deque

class MRUQueue:
    def __init__(self, n: int):
        """
        Initialize the queue with integers from 1 to n.
        """
        self.queue = deque(range(1, n + 1))

    def fetch(self, k: int) -> int:
        """
        Move the kth element (1-indexed) to the end of the queue and return it.
        """
        # Convert 1-indexed to 0-indexed
        element = self.queue[k - 1]
        # Remove the element from its current position
        del self.queue[k - 1]
        # Append the element to the end of the queue
        self.queue.append(element)
        return element


# Example Test Cases
if __name__ == "__main__":
    # Initialize the MRUQueue
    mruQueue = MRUQueue(8)  # Queue: [1, 2, 3, 4, 5, 6, 7, 8]

    # Test Case 1
    assert mruQueue.fetch(3) == 3  # Queue becomes [1, 2, 4, 5, 6, 7, 8, 3]
    # Test Case 2
    assert mruQueue.fetch(5) == 6  # Queue becomes [1, 2, 4, 5, 7, 8, 3, 6]
    # Test Case 3
    assert mruQueue.fetch(2) == 2  # Queue becomes [1, 4, 5, 7, 8, 3, 6, 2]
    # Test Case 4
    assert mruQueue.fetch(8) == 2  # Queue becomes [1, 4, 5, 7, 8, 3, 6, 2]

    print("All test cases passed!")

"""
Time Complexity:
- Initialization: O(n), where n is the size of the queue.
- fetch(k): O(k) in the worst case, as removing an element from the middle of a deque requires shifting elements.

Space Complexity:
- O(n), where n is the size of the queue, as we store all elements in a deque.

Topic: Data Structures (Queue)
"""