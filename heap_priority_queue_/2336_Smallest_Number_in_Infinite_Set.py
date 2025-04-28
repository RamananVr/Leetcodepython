"""
LeetCode Problem #2336: Smallest Number in Infinite Set

Problem Statement:
You have a set which contains all positive integers [1, 2, 3, ...]. Implement the SmallestInfiniteSet class:

1. SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
2. int popSmallest() Removes and returns the smallest integer contained in the infinite set.
3. void addBack(int num) Adds a positive integer num back into the infinite set, if it is not already present.

Constraints:
- 1 <= num <= 1000
- At most 1000 calls will be made in total to popSmallest and addBack.

"""

# Solution
import heapq

class SmallestInfiniteSet:
    def __init__(self):
        # Min-heap to store the smallest numbers that can be popped
        self.heap = []
        # Set to track numbers that are currently in the heap
        self.set = set()
        # Pointer to track the smallest number not yet popped
        self.current = 1

    def popSmallest(self) -> int:
        # If the heap is not empty, pop the smallest number from the heap
        if self.heap:
            smallest = heapq.heappop(self.heap)
            self.set.remove(smallest)
            return smallest
        # Otherwise, return the current smallest number and increment the pointer
        smallest = self.current
        self.current += 1
        return smallest

    def addBack(self, num: int) -> None:
        # Add the number back only if it is smaller than `current` and not already in the heap
        if num < self.current and num not in self.set:
            heapq.heappush(self.heap, num)
            self.set.add(num)

# Example Test Cases
if __name__ == "__main__":
    # Initialize the SmallestInfiniteSet
    obj = SmallestInfiniteSet()
    
    # Test popSmallest
    print(obj.popSmallest())  # Output: 1
    print(obj.popSmallest())  # Output: 2
    
    # Test addBack
    obj.addBack(1)            # Add 1 back to the set
    print(obj.popSmallest())  # Output: 1
    print(obj.popSmallest())  # Output: 3
    
    # Add more numbers back and test
    obj.addBack(2)
    print(obj.popSmallest())  # Output: 2
    print(obj.popSmallest())  # Output: 4

"""
Time and Space Complexity Analysis:

1. popSmallest():
   - Time Complexity: O(log k), where k is the size of the heap. This is due to the heap pop operation.
   - Space Complexity: O(1), as no additional space is used.

2. addBack():
   - Time Complexity: O(log k), where k is the size of the heap. This is due to the heap push operation.
   - Space Complexity: O(1), as no additional space is used.

3. Overall:
   - Time Complexity: O(log k) per operation, where k is the size of the heap.
   - Space Complexity: O(k), where k is the number of elements in the heap and set.

Topic: Heap (Priority Queue)
"""