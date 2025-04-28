"""
LeetCode Problem #2263: Make Array Non-decreasing or Non-increasing

Problem Statement:
You are given an integer array `nums`. You can perform the following operation any number of times:
- Choose an index `i` (0 <= i < len(nums)) and set `nums[i]` to any value.

Your goal is to make the array either non-decreasing or non-increasing. Return the minimum number of operations required to achieve this.

An array is non-decreasing if `nums[i] <= nums[i+1]` for all valid `i`. Similarly, an array is non-increasing if `nums[i] >= nums[i+1]` for all valid `i`.

Constraints:
- 1 <= nums.length <= 2000
- 1 <= nums[i] <= 10^9
"""

# Solution
from bisect import bisect_left

def min_operations(nums):
    def lis_length(arr):
        """Helper function to calculate the length of the Longest Increasing Subsequence (LIS)."""
        lis = []
        for num in arr:
            pos = bisect_left(lis, num)
            if pos == len(lis):
                lis.append(num)
            else:
                lis[pos] = num
        return len(lis)
    
    # Calculate LIS for non-decreasing order
    non_decreasing_lis = lis_length(nums)
    
    # Calculate LIS for non-increasing order
    non_increasing_lis = lis_length([-num for num in nums])
    
    # Minimum operations to make the array non-decreasing or non-increasing
    return len(nums) - max(non_decreasing_lis, non_increasing_lis)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [3, 2, 5, 1, 7]
    print(min_operations(nums1))  # Expected Output: 2

    # Test Case 2
    nums2 = [1, 2, 3, 4, 5]
    print(min_operations(nums2))  # Expected Output: 0

    # Test Case 3
    nums3 = [5, 4, 3, 2, 1]
    print(min_operations(nums3))  # Expected Output: 0

    # Test Case 4
    nums4 = [1, 3, 2, 4, 5]
    print(min_operations(nums4))  # Expected Output: 1

    # Test Case 5
    nums5 = [10, 1, 2, 3, 4]
    print(min_operations(nums5))  # Expected Output: 1

"""
Time Complexity Analysis:
- The `lis_length` function uses a binary search approach to calculate the LIS, which takes O(n log n) time.
- Since we call `lis_length` twice (once for non-decreasing and once for non-increasing), the total time complexity is O(n log n), where n is the length of the input array.

Space Complexity Analysis:
- The `lis` list in the `lis_length` function requires O(n) space in the worst case.
- Therefore, the space complexity is O(n).

Topic: Dynamic Programming (DP), Binary Search
"""