"""
LeetCode Problem #1818: Minimum Absolute Sum Difference

Problem Statement:
You are given two arrays `nums1` and `nums2` of the same length `n`, and an integer `mod = 10^9 + 7`.

The absolute sum difference of arrays `nums1` and `nums2` is defined as the sum of `|nums1[i] - nums2[i]|` for each `0 <= i < n`.

You can replace at most one element of `nums1` with any other element from `nums1` to minimize the absolute sum difference.

Return the minimum absolute sum difference after at most one replacement. Since the answer may be large, return it modulo `10^9 + 7`.

Constraints:
- `n == nums1.length == nums2.length`
- `1 <= n <= 10^5`
- `1 <= nums1[i], nums2[i] <= 10^5`

Example:
Input: nums1 = [1,7,5], nums2 = [2,3,5]
Output: 3
Explanation: Replace nums1[1] with nums1[0], or nums1[1] with nums1[2], to minimize the absolute sum difference.

Input: nums1 = [2,4,6,8,10], nums2 = [2,4,6,8,10]
Output: 0
Explanation: No replacement is needed since the arrays are already equal.

Input: nums1 = [1,10,4,4,2,7], nums2 = [9,3,5,1,7,4]
Output: 20
"""

# Python Solution
from bisect import bisect_left

def minAbsoluteSumDiff(nums1, nums2):
    MOD = 10**9 + 7
    n = len(nums1)
    
    # Calculate the initial absolute sum difference
    initial_sum = sum(abs(nums1[i] - nums2[i]) for i in range(n))
    
    # Sort nums1 for binary search
    sorted_nums1 = sorted(nums1)
    
    # Initialize the maximum improvement
    max_improvement = 0
    
    # Iterate through nums2 to find the best replacement
    for i in range(n):
        original_diff = abs(nums1[i] - nums2[i])
        
        # Binary search to find the closest value in sorted_nums1
        pos = bisect_left(sorted_nums1, nums2[i])
        
        # Check the closest value on the left (if exists)
        if pos > 0:
            left_diff = abs(sorted_nums1[pos - 1] - nums2[i])
            max_improvement = max(max_improvement, original_diff - left_diff)
        
        # Check the closest value on the right (if exists)
        if pos < len(sorted_nums1):
            right_diff = abs(sorted_nums1[pos] - nums2[i])
            max_improvement = max(max_improvement, original_diff - right_diff)
    
    # Calculate the minimized absolute sum difference
    minimized_sum = initial_sum - max_improvement
    
    # Return the result modulo MOD
    return minimized_sum % MOD

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 7, 5]
    nums2 = [2, 3, 5]
    print(minAbsoluteSumDiff(nums1, nums2))  # Output: 3

    # Test Case 2
    nums1 = [2, 4, 6, 8, 10]
    nums2 = [2, 4, 6, 8, 10]
    print(minAbsoluteSumDiff(nums1, nums2))  # Output: 0

    # Test Case 3
    nums1 = [1, 10, 4, 4, 2, 7]
    nums2 = [9, 3, 5, 1, 7, 4]
    print(minAbsoluteSumDiff(nums1, nums2))  # Output: 20

# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting nums1 takes O(n log n).
- Calculating the initial absolute sum difference takes O(n).
- For each element in nums2, we perform a binary search in sorted_nums1, which takes O(log n).
- Overall, the time complexity is O(n log n).

Space Complexity:
- The space complexity is O(n) due to the storage of sorted_nums1.
"""

# Topic: Arrays, Binary Search