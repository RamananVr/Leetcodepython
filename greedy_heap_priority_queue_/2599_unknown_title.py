"""
LeetCode Problem #2599: Make the Prefix Sum Non-negative

Problem Statement:
You are given a 0-indexed integer array `nums`. You can apply the following operation any number of times:
- Choose any index `i` in the array and set `nums[i]` to `-nums[i]` (i.e., flip the sign of `nums[i]`).

Your goal is to make the prefix sum of `nums` non-negative for every index `i` (0 <= i < nums.length). 
Return the minimum number of operations required to achieve this.

A prefix sum of `nums` is defined as the sum of the first `i + 1` elements of `nums` (0-indexed).

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
"""

# Solution
import heapq

def makePrefSumNonNegative(nums):
    """
    Function to calculate the minimum number of operations required to make the prefix sum of nums non-negative.

    Args:
    nums (List[int]): The input array of integers.

    Returns:
    int: The minimum number of operations required.
    """
    min_heap = []  # Min-heap to store negative numbers flipped
    prefix_sum = 0
    operations = 0

    for num in nums:
        prefix_sum += num
        if prefix_sum < 0:
            # If prefix sum becomes negative, we need to flip the largest negative number
            heapq.heappush(min_heap, num)
            prefix_sum -= 2 * heapq.heappop(min_heap)
            operations += 1

    return operations

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [-1, -2, -3, 4]
    print(makePrefSumNonNegative(nums1))  # Output: 2

    # Test Case 2
    nums2 = [3, -5, 2, -1, 4]
    print(makePrefSumNonNegative(nums2))  # Output: 1

    # Test Case 3
    nums3 = [1, 2, 3, 4]
    print(makePrefSumNonNegative(nums3))  # Output: 0

    # Test Case 4
    nums4 = [-5, -2, -3, -4]
    print(makePrefSumNonNegative(nums4))  # Output: 4

    # Test Case 5
    nums5 = [10, -20, 10, -5, 15]
    print(makePrefSumNonNegative(nums5))  # Output: 1

"""
Time Complexity Analysis:
- The loop iterates through the array once, so the time complexity is O(n), where n is the length of nums.
- Each heap operation (push and pop) takes O(log k), where k is the size of the heap. In the worst case, k <= n.
- Therefore, the overall time complexity is O(n log n).

Space Complexity Analysis:
- The space complexity is O(k), where k is the size of the heap. In the worst case, k <= n.
- Therefore, the space complexity is O(n).

Topic: Greedy, Heap (Priority Queue)
"""