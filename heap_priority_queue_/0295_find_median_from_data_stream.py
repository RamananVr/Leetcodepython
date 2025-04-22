"""
LeetCode Question #295: Find Median from Data Stream

Problem Statement:
The median is the middle value in an ordered integer list. If the size of the list is even, 
there is no middle value, and the median is the mean of the two middle values.

- For example, [2,3,4], the median is 3.
- For example, [2,3], the median is (2 + 3) / 2 = 2.5.

Implement the MedianFinder class:
1. MedianFinder() initializes the MedianFinder object.
2. void addNum(int num) adds the integer num from the data stream to the data structure.
3. double findMedian() returns the median of all elements so far. Answers within 10^-5 of the actual answer will be accepted.

Constraints:
- -10^5 <= num <= 10^5
- There will be at least one element in the data structure before calling findMedian.
- At most 5 * 10^4 calls will be made to addNum and findMedian.

Follow-up:
- If all integer numbers from the stream are in the range [0, 100], how would you optimize it?
- If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize it?
"""

import heapq

class MedianFinder:
    def __init__(self):
        """
        Initialize two heaps:
        - max_heap: A max-heap to store the smaller half of the numbers (inverted to act as a max-heap using negative values).
        - min_heap: A min-heap to store the larger half of the numbers.
        """
        self.max_heap = []  # Max-heap (stores negative values for inversion)
        self.min_heap = []  # Min-heap

    def addNum(self, num: int) -> None:
        """
        Add a number to the data structure.
        """
        # Add to max_heap first (inverted to maintain max-heap property)
        heapq.heappush(self.max_heap, -num)

        # Ensure the largest value in max_heap is smaller than the smallest value in min_heap
        if self.max_heap and self.min_heap and (-self.max_heap[0] > self.min_heap[0]):
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

        # Balance the heaps to ensure their sizes differ by at most 1
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        """
        Find and return the median of the current data stream.
        """
        # If the heaps are of equal size, the median is the average of the two middle values
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        # Otherwise, the median is the top of the larger heap
        return -self.max_heap[0]


# Example Test Cases
if __name__ == "__main__":
    mf = MedianFinder()
    
    # Test Case 1
    mf.addNum(1)
    mf.addNum(2)
    print(mf.findMedian())  # Output: 1.5
    
    # Test Case 2
    mf.addNum(3)
    print(mf.findMedian())  # Output: 2.0
    
    # Test Case 3
    mf.addNum(4)
    mf.addNum(5)
    print(mf.findMedian())  # Output: 3.0
    
    # Test Case 4
    mf.addNum(-1)
    print(mf.findMedian())  # Output: 2.0


"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - addNum: O(log n), where n is the number of elements in the data stream. This is because we perform heap operations (push and pop) which take O(log n).
   - findMedian: O(1), as retrieving the median involves accessing the top elements of the heaps.

2. Space Complexity:
   - O(n), where n is the number of elements in the data stream. This is because we store all elements in the two heaps.

Topic: Heap (Priority Queue)
"""