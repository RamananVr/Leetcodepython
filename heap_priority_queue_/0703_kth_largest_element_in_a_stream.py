"""
LeetCode Question #703: Kth Largest Element in a Stream

Problem Statement:
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement the KthLargest class:
- KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
- int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.

Constraints:
- 1 <= k <= 10^4
- 0 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
- -10^4 <= val <= 10^4
- At most 10^4 calls will be made to add.
- It is guaranteed that there will be at least k elements in the array when you search for the kth element.
"""

import heapq

class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        """
        Initializes the KthLargest object with k and nums.
        Uses a min-heap to maintain the k largest elements.
        """
        self.k = k
        self.min_heap = []
        
        # Add all elements from nums to the heap
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        """
        Adds a new value to the stream and returns the kth largest element.
        """
        heapq.heappush(self.min_heap, val)
        
        # Ensure the heap size does not exceed k
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        
        # The root of the heap is the kth largest element
        return self.min_heap[0]


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    kthLargest = KthLargest(3, [4, 5, 8, 2])
    print(kthLargest.add(3))  # Output: 4
    print(kthLargest.add(5))  # Output: 5
    print(kthLargest.add(10)) # Output: 5
    print(kthLargest.add(9))  # Output: 8
    print(kthLargest.add(4))  # Output: 8

    # Test Case 2
    kthLargest = KthLargest(2, [1, 2, 3])
    print(kthLargest.add(4))  # Output: 3
    print(kthLargest.add(5))  # Output: 4

"""
Time and Space Complexity Analysis:

1. Initialization (__init__):
   - Adding all elements from nums to the heap takes O(n * log(k)), where n is the length of nums and k is the size of the heap.
   - Space complexity is O(k) for the heap.

2. Adding a new value (add):
   - Adding a value to the heap takes O(log(k)).
   - If the heap exceeds size k, removing the smallest element also takes O(log(k)).
   - Space complexity remains O(k) for the heap.

Overall:
- Time Complexity: O(n * log(k)) for initialization + O(log(k)) per add operation.
- Space Complexity: O(k).

Topic: Heap (Priority Queue)
"""