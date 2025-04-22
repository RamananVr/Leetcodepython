"""
LeetCode Problem #632: Smallest Range Covering Elements from K Lists

Problem Statement:
You have k lists of sorted integers in non-decreasing order. Find the smallest range that includes at least one number from each of the k lists.

Formally, the range [a, b] is smaller than range [c, d] if:
- b - a < d - c, or
- a < c if b - a == d - c.

Return the smallest range [a, b].

Constraints:
- k == nums.length
- 1 <= k <= 3500
- 1 <= nums[i].length <= 50
- -10^5 <= nums[i][j] <= 10^5
- nums[i] is sorted in non-decreasing order.

Example:
Input: nums = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
Output: [20,24]
Explanation: 
- List 1: [4, 10, 15, 24, 26]
- List 2: [0, 9, 12, 20]
- List 3: [5, 18, 22, 30]
The smallest range is [20, 24] because it includes 24 from list 1, 20 from list 2, and 22 from list 3.

"""

from heapq import heappush, heappop

def smallestRange(nums):
    """
    Finds the smallest range that includes at least one number from each of the k lists.

    :param nums: List[List[int]] - A list of k sorted lists of integers.
    :return: List[int] - The smallest range [a, b].
    """
    # Min-heap to store the current elements from each list
    min_heap = []
    max_value = float('-inf')

    # Initialize the heap with the first element of each list
    for i in range(len(nums)):
        heappush(min_heap, (nums[i][0], i, 0))
        max_value = max(max_value, nums[i][0])

    # Initialize the smallest range
    smallest_range = [float('-inf'), float('inf')]

    while min_heap:
        min_value, list_idx, element_idx = heappop(min_heap)

        # Update the smallest range if the current range is smaller
        if max_value - min_value < smallest_range[1] - smallest_range[0]:
            smallest_range = [min_value, max_value]

        # If we have reached the end of one of the lists, break
        if element_idx + 1 == len(nums[list_idx]):
            break

        # Add the next element from the same list to the heap
        next_value = nums[list_idx][element_idx + 1]
        heappush(min_heap, (next_value, list_idx, element_idx + 1))
        max_value = max(max_value, next_value)

    return smallest_range

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
    print(smallestRange(nums1))  # Output: [20, 24]

    # Test Case 2
    nums2 = [[1,2,3], [1,2,3], [1,2,3]]
    print(smallestRange(nums2))  # Output: [1, 1]

    # Test Case 3
    nums3 = [[1,2,3], [4,5,6], [7,8,9]]
    print(smallestRange(nums3))  # Output: [3, 7]

    # Test Case 4
    nums4 = [[1], [2], [3]]
    print(smallestRange(nums4))  # Output: [1, 3]

"""
Time Complexity:
- Let k be the number of lists and n be the average length of each list.
- The heap operations (push and pop) take O(log k), and we perform these operations for every element in all lists.
- Total time complexity: O(n * k * log k).

Space Complexity:
- The heap stores at most k elements at any time, so the space complexity is O(k).

Topic: Heap (Priority Queue), Two Pointers
"""