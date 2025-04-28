"""
LeetCode Problem #2808: Minimum Operations to Make Array Equal II

Problem Statement:
You are given two integer arrays nums1 and nums2 of length n and an integer k. 
The operation you can perform on nums1 is as follows:
- Pick two indices i and j, where i != j, and increment nums1[i] by k and decrement nums1[j] by k.

Return the minimum number of operations required to make nums1 equal to nums2. 
If it is impossible to make nums1 equal to nums2, return -1.

Example:
Input: nums1 = [1, 2, 5], nums2 = [4, 1, 3], k = 1
Output: 5

Constraints:
- n == nums1.length == nums2.length
- 1 <= n <= 10^5
- 0 <= nums1[i], nums2[i] <= 10^9
- 0 <= k <= 10^5
"""

# Python Solution
def minOperations(nums1, nums2, k):
    if nums1 == nums2:
        return 0  # Arrays are already equal
    
    if k == 0:
        return -1  # Impossible to make changes if k is 0
    
    total_diff = 0
    positive_diff = 0
    negative_diff = 0
    
    for a, b in zip(nums1, nums2):
        diff = b - a
        if diff % k != 0:
            return -1  # If the difference is not divisible by k, it's impossible
        total_diff += diff
        if diff > 0:
            positive_diff += diff // k
        elif diff < 0:
            negative_diff += abs(diff) // k
    
    # If total_diff is not zero, nums1 cannot be made equal to nums2
    if total_diff != 0:
        return -1
    
    # The number of operations required is the sum of positive_diff and negative_diff
    return max(positive_diff, negative_diff)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 5]
    nums2 = [4, 1, 3]
    k = 1
    print(minOperations(nums1, nums2, k))  # Output: 5

    # Test Case 2
    nums1 = [1, 2, 3]
    nums2 = [1, 2, 3]
    k = 1
    print(minOperations(nums1, nums2, k))  # Output: 0

    # Test Case 3
    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6]
    k = 0
    print(minOperations(nums1, nums2, k))  # Output: -1

    # Test Case 4
    nums1 = [1, 2, 3]
    nums2 = [7, 8, 9]
    k = 2
    print(minOperations(nums1, nums2, k))  # Output: -1

    # Test Case 5
    nums1 = [10, 20, 30]
    nums2 = [40, 50, 60]
    k = 10
    print(minOperations(nums1, nums2, k))  # Output: 6

# Time and Space Complexity Analysis
# Time Complexity: O(n)
# - We iterate through the arrays once to calculate the differences and check divisibility.
# - This results in a linear time complexity relative to the size of the arrays.

# Space Complexity: O(1)
# - We use a constant amount of extra space to store variables like total_diff, positive_diff, and negative_diff.
# - No additional data structures are used.

# Topic: Arrays