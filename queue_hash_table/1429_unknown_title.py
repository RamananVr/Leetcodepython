"""
LeetCode Problem #1429: First Unique Number

Problem Statement:
You have a queue of integers, you need to retrieve the first unique integer in the queue. Implement the `FirstUnique` class:

- `FirstUnique(int[] nums)` Initializes the object with the numbers in the queue.
- `int showFirstUnique()` Returns the value of the first unique integer of the queue, and returns -1 if there is no such integer.
- `void add(int value)` Insert value to the queue.

Example:
FirstUnique firstUnique = new FirstUnique([2,3,5]);
firstUnique.showFirstUnique(); // return 2
firstUnique.add(5);            // the queue is now [2,3,5,5]
firstUnique.showFirstUnique(); // return 2
firstUnique.add(2);            // the queue is now [2,3,5,5,2]
firstUnique.showFirstUnique(); // return 3
firstUnique.add(3);            // the queue is now [2,3,5,5,2,3]
firstUnique.showFirstUnique(); // return -1

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^8
- 1 <= value <= 10^8
"""

from collections import deque, Counter

class FirstUnique:
    def __init__(self, nums):
        """
        Initialize the object with the numbers in the queue.
        """
        self.queue = deque()
        self.count = Counter()
        
        for num in nums:
            self.add(num)

    def showFirstUnique(self):
        """
        Returns the value of the first unique integer in the queue.
        If no unique integer exists, return -1.
        """
        while self.queue and self.count[self.queue[0]] > 1:
            self.queue.popleft()
        
        if self.queue:
            return self.queue[0]
        return -1

    def add(self, value):
        """
        Insert value into the queue.
        """
        self.count[value] += 1
        if self.count[value] == 1:
            self.queue.append(value)


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    firstUnique = FirstUnique([2, 3, 5])
    print(firstUnique.showFirstUnique())  # Output: 2
    firstUnique.add(5)                    # Queue: [2, 3, 5, 5]
    print(firstUnique.showFirstUnique())  # Output: 2
    firstUnique.add(2)                    # Queue: [2, 3, 5, 5, 2]
    print(firstUnique.showFirstUnique())  # Output: 3
    firstUnique.add(3)                    # Queue: [2, 3, 5, 5, 2, 3]
    print(firstUnique.showFirstUnique())  # Output: -1

    # Test Case 2
    firstUnique = FirstUnique([7, 7, 7, 7, 7, 7])
    print(firstUnique.showFirstUnique())  # Output: -1
    firstUnique.add(7)                    # Queue: [7, 7, 7, 7, 7, 7, 7]
    print(firstUnique.showFirstUnique())  # Output: -1
    firstUnique.add(8)                    # Queue: [7, 7, 7, 7, 7, 7, 7, 8]
    print(firstUnique.showFirstUnique())  # Output: 8

    # Test Case 3
    firstUnique = FirstUnique([1, 2, 3, 4, 5])
    print(firstUnique.showFirstUnique())  # Output: 1
    firstUnique.add(1)                    # Queue: [1, 2, 3, 4, 5, 1]
    print(firstUnique.showFirstUnique())  # Output: 2
    firstUnique.add(2)                    # Queue: [1, 2, 3, 4, 5, 1, 2]
    print(firstUnique.showFirstUnique())  # Output: 3

"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - `__init__`: O(n), where n is the length of the input list `nums`. Each number is added to the queue and its count is updated.
   - `showFirstUnique`: O(1) amortized. In the worst case, we may need to remove multiple elements from the front of the queue, but each element is processed at most once.
   - `add`: O(1) for updating the count and appending to the queue.

2. Space Complexity:
   - The space complexity is O(n), where n is the number of elements in the queue and the count dictionary.

Topic: Queue, Hash Table
"""