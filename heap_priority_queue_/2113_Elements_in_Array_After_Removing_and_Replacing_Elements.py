"""
LeetCode Problem #2113: Elements in Array After Removing and Replacing Elements

Problem Statement:
You are given an integer array `nums` and an integer `k`. You need to perform the following operation exactly `k` times:

1. Remove the smallest element from the array.
2. Replace it with the sum of the removed element and the next smallest element in the array.

Return the array after performing the operation `k` times.

Constraints:
- 2 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
- 1 <= k <= 10^5
"""

# Solution
import heapq

def elementsAfterOperations(nums, k):
    """
    Perform the operation k times on the array nums and return the resulting array.

    :param nums: List[int] - The input array of integers.
    :param k: int - The number of operations to perform.
    :return: List[int] - The resulting array after k operations.
    """
    # Convert nums into a min-heap
    heapq.heapify(nums)
    
    for _ in range(k):
        # Remove the smallest element
        smallest = heapq.heappop(nums)
        # Remove the next smallest element
        next_smallest = heapq.heappop(nums)
        # Replace with their sum
        new_element = smallest + next_smallest
        # Push the new element back into the heap
        heapq.heappush(nums, new_element)
        # Push the next smallest element back into the heap
        heapq.heappush(nums, next_smallest)
    
    return nums

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3, 4]
    k1 = 2
    print(elementsAfterOperations(nums1, k1))  # Expected Output: [4, 4, 5, 5]

    # Test Case 2
    nums2 = [5, 7, 9]
    k2 = 1
    print(elementsAfterOperations(nums2, k2))  # Expected Output: [7, 9, 12]

    # Test Case 3
    nums3 = [1, 1, 1, 1]
    k3 = 3
    print(elementsAfterOperations(nums3, k3))  # Expected Output: [2, 2, 2, 4]

"""
Time Complexity Analysis:
- Converting the array into a heap takes O(n), where n is the length of nums.
- Each operation involves popping two elements and pushing two elements back into the heap, which takes O(log n) per operation.
- Since we perform k operations, the total time complexity is O(n + k * log n).

Space Complexity Analysis:
- The space complexity is O(n) due to the heap storage.

Topic: Heap (Priority Queue)
"""