"""
LeetCode Question #900: RLE Iterator

Problem Statement:
Write an iterator that iterates through a run-length encoded sequence.

The iterator is initialized by a list of integers encoding the sequence. For example, the list [2, 3, 1, 4] means that the sequence is "3, 3, 4" (two 3's followed by one 4).

The iterator supports the following operations:
- `next(int n)`: Exhausts the next `n` elements (n >= 1) and returns the last element exhausted. If there are fewer than `n` elements left, the iterator exhausts all remaining elements and returns -1.

Example:
Input:
["RLEIterator", "next", "next", "next", "next"]
[[[3,8,0,9,2,5]], [2], [1], [1], [2]]

Output:
[null, 8, 8, 5, -1]

Explanation:
RLEIterator rleIterator = new RLEIterator([3,8,0,9,2,5]);
rleIterator.next(2); // exhausts 2 terms of the sequence, returning 8.
rleIterator.next(1); // exhausts 1 term of the sequence, returning 8.
rleIterator.next(1); // exhausts 1 term of the sequence, returning 5.
rleIterator.next(2); // exhausts 2 terms, but the sequence is now exhausted, so return -1.

Constraints:
- 0 <= encoding.length <= 1000
- encoding.length is even.
- 1 <= encoding[i] <= 10^9 for all even i.
- 1 <= n <= 10^9
- At most 1000 calls will be made to next.

"""

# Python Solution
class RLEIterator:
    def __init__(self, encoding: list[int]):
        """
        Initialize the RLEIterator with the given encoding.
        """
        self.encoding = encoding
        self.index = 0  # Current index in the encoding list
        self.remaining = 0  # Remaining count of the current element

    def next(self, n: int) -> int:
        """
        Exhausts the next n elements and returns the last element exhausted.
        If fewer than n elements remain, exhaust all and return -1.
        """
        while n > 0:
            # If the current index is out of bounds, return -1
            if self.index >= len(self.encoding):
                return -1
            
            # If there are remaining elements for the current value
            if self.remaining == 0:
                self.remaining = self.encoding[self.index]  # Load the count
                self.index += 1  # Move to the value
            
            # Exhaust elements from the current value
            if n <= self.remaining:
                self.remaining -= n
                return self.encoding[self.index]
            else:
                n -= self.remaining
                self.remaining = 0
                self.index += 1  # Move to the next count-value pair
        
        return -1

# Example Test Cases
if __name__ == "__main__":
    # Initialize the RLEIterator
    rleIterator = RLEIterator([3, 8, 0, 9, 2, 5])
    
    # Test cases
    print(rleIterator.next(2))  # Output: 8
    print(rleIterator.next(1))  # Output: 8
    print(rleIterator.next(1))  # Output: 5
    print(rleIterator.next(2))  # Output: -1

"""
Time and Space Complexity Analysis:

Time Complexity:
- The `next` method iterates through the encoding list until `n` elements are exhausted.
- In the worst case, the method may iterate through the entire encoding list, which has a length of O(len(encoding)).
- Therefore, the time complexity of the `next` method is O(len(encoding)).

Space Complexity:
- The space complexity is O(1) since we are only using a few variables to track the current index and remaining count.
- The input encoding list is provided externally and does not contribute to the space complexity of the class.

Topic: Arrays
"""