"""
LeetCode Problem #2474: "Smallest Number in Infinite Set"

Problem Statement:
You have a set which contains all positive integers [1, 2, 3, ...]. Implement the SmallestInfiniteSet class:

- SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
- int popSmallest() Removes and returns the smallest integer contained in the infinite set.
- void addBack(int num) Adds a positive integer num back into the infinite set, if it is not already in the infinite set.

Constraints:
- 1 <= num <= 1000
- At most 1000 calls will be made in total to popSmallest and addBack.

Example:
    Input:
    ["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest"]
    [[], [2], [], [], [], [1], [], []]

    Output:
    [null, null, 1, 2, 3, null, 1, 4]

    Explanation:
    SmallestInfiniteSet smallestInfiniteSet = new SmallestInfiniteSet();
    smallestInfiniteSet.addBack(2);    // 2 is already in the set, so no change is made.
    smallestInfiniteSet.popSmallest(); // return 1, then remove it from the set.
    smallestInfiniteSet.popSmallest(); // return 2, then remove it from the set.
    smallestInfiniteSet.popSmallest(); // return 3, then remove it from the set.
    smallestInfiniteSet.addBack(1);    // 1 is added back to the set.
    smallestInfiniteSet.popSmallest(); // return 1, then remove it from the set.
    smallestInfiniteSet.popSmallest(); // return 4, then remove it from the set.
"""

import heapq

class SmallestInfiniteSet:
    def __init__(self):
        # Min-heap to store the numbers that have been added back
        self.added_back = []
        # Set to track numbers in the heap
        self.added_back_set = set()
        # Pointer to track the smallest number in the infinite set
        self.current = 1

    def popSmallest(self) -> int:
        # If there are numbers in the heap, pop the smallest one
        if self.added_back:
            smallest = heapq.heappop(self.added_back)
            self.added_back_set.remove(smallest)
            return smallest
        # Otherwise, return the current smallest number and increment the pointer
        smallest = self.current
        self.current += 1
        return smallest

    def addBack(self, num: int) -> None:
        # Add the number back only if it's smaller than the current pointer
        # and not already in the heap
        if num < self.current and num not in self.added_back_set:
            heapq.heappush(self.added_back, num)
            self.added_back_set.add(num)


# Example Test Cases
if __name__ == "__main__":
    # Initialize the SmallestInfiniteSet
    smallestInfiniteSet = SmallestInfiniteSet()

    # Test Case 1
    smallestInfiniteSet.addBack(2)  # 2 is already in the set, so no change is made.
    print(smallestInfiniteSet.popSmallest())  # Output: 1
    print(smallestInfiniteSet.popSmallest())  # Output: 2
    print(smallestInfiniteSet.popSmallest())  # Output: 3
    smallestInfiniteSet.addBack(1)  # 1 is added back to the set.
    print(smallestInfiniteSet.popSmallest())  # Output: 1
    print(smallestInfiniteSet.popSmallest())  # Output: 4

    # Test Case 2
    smallestInfiniteSet = SmallestInfiniteSet()
    print(smallestInfiniteSet.popSmallest())  # Output: 1
    print(smallestInfiniteSet.popSmallest())  # Output: 2
    smallestInfiniteSet.addBack(1)  # 1 is added back to the set.
    print(smallestInfiniteSet.popSmallest())  # Output: 1
    print(smallestInfiniteSet.popSmallest())  # Output: 3


"""
Time Complexity Analysis:
- popSmallest():
  - If the heap is non-empty, popping the smallest element takes O(log k), where k is the size of the heap.
  - If the heap is empty, returning the current smallest number is O(1).
  - Overall: O(log k) in the worst case.
- addBack():
  - Checking if the number is in the set is O(1).
  - Adding the number to the heap takes O(log k), where k is the size of the heap.
  - Overall: O(log k) in the worst case.

Space Complexity:
- The heap and set used to store added-back numbers can grow up to O(n), where n is the number of calls to addBack.
- The pointer `current` uses O(1) space.
- Overall: O(n) space.

Topic: Heap (Priority Queue)
"""