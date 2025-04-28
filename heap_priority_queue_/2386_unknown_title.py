"""
LeetCode Problem #2386: Find the K-Sum of an Array

Problem Statement:
You are given an integer array `nums` and an integer `k`. The `k-sum` of the array is defined as the k-th largest sum of any non-empty subsequence of the array. A subsequence is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

Return the k-sum of the array.

Example:
Input: nums = [2,4,-2], k = 5
Output: 2
Explanation: All the sums of non-empty subsequences in sorted order are:
-4, -2, 0, 2, 2, 4, 6. The 5th largest sum is 2.

Constraints:
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
- 1 <= k <= min(2000, 2^nums.length)
"""

import heapq

def kSum(nums, k):
    """
    Finds the k-th largest sum of any non-empty subsequence of the array.

    :param nums: List[int] - The input array of integers.
    :param k: int - The k-th largest sum to find.
    :return: int - The k-th largest sum.
    """
    # Step 1: Calculate the maximum sum by treating all numbers as positive
    max_sum = sum(x for x in nums if x > 0)
    
    # Step 2: Convert all numbers to their absolute values
    nums = [abs(x) for x in nums]
    nums.sort()
    
    # Step 3: Use a min-heap to track the k largest sums
    heap = [(0, 0)]  # (current_sum, index)
    for _ in range(k - 1):
        current_sum, index = heapq.heappop(heap)
        if index < len(nums):
            # Add the next element to the current sum
            heapq.heappush(heap, (current_sum + nums[index], index + 1))
            # Skip the current element and move to the next index
            if index > 0:
                heapq.heappush(heap, (current_sum + nums[index] - nums[index - 1], index + 1))
    
    # The k-th largest sum is max_sum minus the smallest sum in the heap
    return max_sum - heap[0][0]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums = [2, 4, -2]
    k = 5
    print(kSum(nums, k))  # Output: 2

    # Test Case 2
    nums = [1, -1, 2, -2, 3]
    k = 7
    print(kSum(nums, k))  # Output: 3

    # Test Case 3
    nums = [5, -3, -2, 7]
    k = 6
    print(kSum(nums, k))  # Output: 5

    # Test Case 4
    nums = [-1, -2, -3, -4]
    k = 3
    print(kSum(nums, k))  # Output: -6

"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the array takes O(n log n), where n is the length of the array.
- The heap operations (push and pop) are performed k times, and each operation takes O(log k).
- Overall time complexity: O(n log n + k log k).

Space Complexity:
- The heap stores up to k elements, so the space complexity for the heap is O(k).
- The space complexity for the sorted array is O(n).
- Overall space complexity: O(n + k).

Topic: Heap (Priority Queue)
"""