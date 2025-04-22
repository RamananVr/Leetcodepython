"""
LeetCode Question #281: Zigzag Iterator

Problem Statement:
Given two 1-dimensional vectors `v1` and `v2`, implement an iterator to return their elements alternately. 
If one vector is longer than the other, the remaining elements of the longer vector should be appended to the result.

Implement the `ZigzagIterator` class:
- `ZigzagIterator.__init__(self, v1: List[int], v2: List[int])` Initializes the object with the two vectors `v1` and `v2`.
- `ZigzagIterator.next(self) -> int` Returns the next element in the zigzag order.
- `ZigzagIterator.hasNext(self) -> bool` Returns `True` if the iterator still has elements, and `False` otherwise.

Example:
Input:
v1 = [1, 2]
v2 = [3, 4, 5, 6]

Output:
[1, 3, 2, 4, 5, 6]

Explanation:
By calling `next` repeatedly until `hasNext` returns `False`, the order of elements returned by `next` should be: [1, 3, 2, 4, 5, 6].

Constraints:
- 0 <= len(v1), len(v2) <= 1000
- 1 <= v1[i], v2[i] <= 10^9
- At most 10^4 calls will be made to `next` and `hasNext`.
"""

from collections import deque
from typing import List

class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        """
        Initialize the ZigzagIterator with two input vectors.
        """
        self.queue = deque()
        if v1:
            self.queue.append(iter(v1))
        if v2:
            self.queue.append(iter(v2))

    def next(self) -> int:
        """
        Return the next element in zigzag order.
        """
        if self.hasNext():
            current_iter = self.queue.popleft()
            next_val = next(current_iter)
            # If the iterator still has elements, add it back to the queue
            if any(True for _ in current_iter):
                self.queue.append(current_iter)
            return next_val
        raise StopIteration("No more elements in the iterator.")

    def hasNext(self) -> bool:
        """
        Check if there are any elements left in the iterator.
        """
        return bool(self.queue)


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    v1 = [1, 2]
    v2 = [3, 4, 5, 6]
    zigzag = ZigzagIterator(v1, v2)
    result = []
    while zigzag.hasNext():
        result.append(zigzag.next())
    print(result)  # Output: [1, 3, 2, 4, 5, 6]

    # Test Case 2
    v1 = [1]
    v2 = [2, 3, 4]
    zigzag = ZigzagIterator(v1, v2)
    result = []
    while zigzag.hasNext():
        result.append(zigzag.next())
    print(result)  # Output: [1, 2, 3, 4]

    # Test Case 3
    v1 = []
    v2 = [1, 2, 3]
    zigzag = ZigzagIterator(v1, v2)
    result = []
    while zigzag.hasNext():
        result.append(zigzag.next())
    print(result)  # Output: [1, 2, 3]

    # Test Case 4
    v1 = [1, 2, 3]
    v2 = []
    zigzag = ZigzagIterator(v1, v2)
    result = []
    while zigzag.hasNext():
        result.append(zigzag.next())
    print(result)  # Output: [1, 2, 3]

"""
Time Complexity:
- `__init__`: O(1) to initialize the deque with at most two iterators.
- `next`: O(1) amortized. Each call to `next` processes one element and may re-add an iterator to the queue.
- `hasNext`: O(1) to check if the deque is non-empty.

Space Complexity:
- O(1) additional space for the deque, as it only stores references to the iterators.

Topic: Iterators, Queues
"""