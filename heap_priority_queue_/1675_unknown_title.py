"""
LeetCode Problem #1675: Minimize Deviation in Array

Problem Statement:
You are given an array nums of n positive integers.

You can perform two types of operations on any element of the array any number of times:
1. If the element is even, you can divide it by 2 (e.g., 8 becomes 4).
2. If the element is odd, you can multiply it by 2 (e.g., 3 becomes 6).

The deviation of the array is the difference between the maximum and minimum elements in the array.

Return the minimum deviation the array can have after performing some number of operations.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
"""

import heapq

def minimumDeviation(nums):
    """
    Minimize the deviation in the array by performing allowed operations.

    :param nums: List[int] - Array of positive integers
    :return: int - Minimum deviation
    """
    # Step 1: Normalize the array
    # If the number is odd, multiply it by 2 to make it even
    # Use a max heap to track the largest element (invert values for Python's min-heap)
    max_heap = []
    min_value = float('inf')
    
    for num in nums:
        if num % 2 == 1:
            num *= 2
        heapq.heappush(max_heap, -num)
        min_value = min(min_value, num)
    
    # Step 2: Minimize deviation
    min_deviation = float('inf')
    
    while max_heap:
        # Get the current largest element
        current_max = -heapq.heappop(max_heap)
        min_deviation = min(min_deviation, current_max - min_value)
        
        # If the largest element is even, divide it by 2
        if current_max % 2 == 0:
            new_value = current_max // 2
            heapq.heappush(max_heap, -new_value)
            min_value = min(min_value, new_value)
        else:
            # If the largest element is odd, stop as we cannot reduce it further
            break
    
    return min_deviation

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3, 4]
    print(minimumDeviation(nums1))  # Expected Output: 1

    # Test Case 2
    nums2 = [4, 1, 5, 20, 3]
    print(minimumDeviation(nums2))  # Expected Output: 3

    # Test Case 3
    nums3 = [2, 10, 8]
    print(minimumDeviation(nums3))  # Expected Output: 3

    # Test Case 4
    nums4 = [3, 5]
    print(minimumDeviation(nums4))  # Expected Output: 0

"""
Time and Space Complexity Analysis:

Time Complexity:
- Normalizing the array takes O(n), where n is the length of nums.
- Each operation on the heap (push/pop) takes O(log n).
- In the worst case, we perform O(log(max(nums))) heap operations for each element, where max(nums) is the largest number in the array.
- Overall complexity: O(n * log(max(nums))).

Space Complexity:
- The max heap stores n elements, so the space complexity is O(n).
- Additional space is used for variables like min_value and min_deviation, which are O(1).
- Overall space complexity: O(n).

Topic: Heap (Priority Queue)
"""