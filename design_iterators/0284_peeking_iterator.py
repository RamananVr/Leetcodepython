"""
LeetCode Question #284: Peeking Iterator

Problem Statement:
Design an iterator that supports the `peek` operation on an existing iterator in addition to the `hasNext` and `next` operations.

Implement the PeekingIterator class:
- `PeekingIterator(Iterator iterator)` Initializes the object with the given iterator.
- `peek()` Returns the next element in the iterator without advancing the iterator.
- `next()` Advances the iterator and returns the next element.
- `hasNext()` Returns true if the iterator has more elements.

Notes:
1. The input iterator is guaranteed to have at least one element.
2. You may assume that `Iterator` is a class with the following methods:
   - `next()` Returns the next element in the sequence.
   - `hasNext()` Returns true if the sequence has more elements.

Constraints:
- 1 <= nums.length <= 1000
- 1 <= nums[i] <= 1000
"""

# Solution
class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize the PeekingIterator with the given iterator.
        """
        self.iterator = iterator
        self.peeked_value = None

    def peek(self):
        """
        Returns the next element in the iterator without advancing the iterator.
        """
        if self.peeked_value is None:
            self.peeked_value = self.iterator.next()
        return self.peeked_value

    def next(self):
        """
        Advances the iterator and returns the next element.
        """
        if self.peeked_value is not None:
            next_value = self.peeked_value
            self.peeked_value = None
            return next_value
        return self.iterator.next()

    def hasNext(self):
        """
        Returns true if the iterator has more elements.
        """
        return self.peeked_value is not None or self.iterator.hasNext()


# Example Test Cases
class Iterator:
    """
    A simple implementation of the Iterator class for testing purposes.
    """
    def __init__(self, nums):
        self.nums = nums
        self.index = 0

    def next(self):
        if self.hasNext():
            value = self.nums[self.index]
            self.index += 1
            return value
        raise StopIteration

    def hasNext(self):
        return self.index < len(self.nums)


if __name__ == "__main__":
    # Test Case 1
    nums = [1, 2, 3]
    iterator = Iterator(nums)
    peeking_iterator = PeekingIterator(iterator)

    print(peeking_iterator.peek())  # Output: 1
    print(peeking_iterator.next())  # Output: 1
    print(peeking_iterator.peek())  # Output: 2
    print(peeking_iterator.next())  # Output: 2
    print(peeking_iterator.hasNext())  # Output: True
    print(peeking_iterator.next())  # Output: 3
    print(peeking_iterator.hasNext())  # Output: False

    # Test Case 2
    nums = [10, 20, 30]
    iterator = Iterator(nums)
    peeking_iterator = PeekingIterator(iterator)

    print(peeking_iterator.peek())  # Output: 10
    print(peeking_iterator.next())  # Output: 10
    print(peeking_iterator.peek())  # Output: 20
    print(peeking_iterator.next())  # Output: 20
    print(peeking_iterator.hasNext())  # Output: True
    print(peeking_iterator.next())  # Output: 30
    print(peeking_iterator.hasNext())  # Output: False


# Time and Space Complexity Analysis
# Time Complexity:
# - `peek()`: O(1) - Fetching the next element without advancing the iterator.
# - `next()`: O(1) - Returning the next element and advancing the iterator.
# - `hasNext()`: O(1) - Checking if there are more elements.
# Overall, all operations are O(1).

# Space Complexity:
# - O(1) - The class uses a single variable `peeked_value` to store the next element temporarily.

# Topic: Design, Iterators