"""
LeetCode Problem #2208: Minimum Operations to Halve Array Sum

Problem Statement:
You are given an array `nums` of positive integers. In one operation, you can choose any number from the array and reduce it to half (i.e., replace the number `x` with `x / 2`).

Return the minimum number of operations required to reduce the sum of the array by at least half.

Example:
Input: nums = [5, 19, 8, 1]
Output: 3
Explanation:
- Choose 19 and reduce it to 9.5. Array becomes [5, 9.5, 8, 1].
- Choose 9.5 and reduce it to 4.75. Array becomes [5, 4.75, 8, 1].
- Choose 8 and reduce it to 4. Array becomes [5, 4.75, 4, 1].
The sum of the array is now 14.75, which is less than half of the initial sum (33 / 2 = 16.5). So, 3 operations are required.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^7
"""

import heapq

def halveArray(nums):
    """
    Function to calculate the minimum number of operations required to reduce the sum of the array by at least half.

    :param nums: List[int] - Array of positive integers
    :return: int - Minimum number of operations
    """
    # Calculate the initial sum of the array
    total_sum = sum(nums)
    target = total_sum / 2  # Target sum to achieve
    current_sum = total_sum

    # Use a max heap to prioritize the largest elements
    max_heap = [-num for num in nums]  # Negate values to simulate max heap
    heapq.heapify(max_heap)

    operations = 0

    # Perform operations until the sum is reduced to at least half
    while current_sum > target:
        # Extract the largest element from the heap
        largest = -heapq.heappop(max_heap)
        # Reduce the largest element to half
        reduced = largest / 2
        # Update the current sum
        current_sum -= reduced
        # Push the reduced value back into the heap
        heapq.heappush(max_heap, -reduced)
        # Increment the operation count
        operations += 1

    return operations

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [5, 19, 8, 1]
    print(halveArray(nums1))  # Output: 3

    # Test Case 2
    nums2 = [3, 8, 20]
    print(halveArray(nums2))  # Output: 3

    # Test Case 3
    nums3 = [1, 2, 3, 4, 5]
    print(halveArray(nums3))  # Output: 5

    # Test Case 4
    nums4 = [10, 10, 10, 10]
    print(halveArray(nums4))  # Output: 4

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm uses a max heap to repeatedly extract and reduce the largest element.
- Extracting and inserting into the heap takes O(log n) time per operation.
- In the worst case, we may need to perform operations for all elements in the array, resulting in O(n log n) time complexity.

Space Complexity:
- The space complexity is O(n) due to the heap storage.

Topic: Greedy, Heap (Priority Queue)
"""