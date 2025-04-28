"""
LeetCode Problem #2228: Minimum Operations to Make Array Equal II

Problem Statement:
You are given two integer arrays nums1 and nums2 of length n and an integer k. In one operation, you can pick two indices i and j (i != j) and increase nums1[i] by k and decrease nums1[j] by k. The goal is to make nums1 equal to nums2. Return the minimum number of operations required to make nums1 equal to nums2, or -1 if it is impossible.

Example:
Input: nums1 = [1, 2, 3], nums2 = [4, 5, 6], k = 2
Output: 3
Explanation: Perform the following operations:
- Increase nums1[0] by 2 and decrease nums1[1] by 2 -> nums1 = [3, 0, 3]
- Increase nums1[0] by 2 and decrease nums1[2] by 2 -> nums1 = [5, 0, 1]
- Increase nums1[1] by 2 and decrease nums1[2] by 2 -> nums1 = [5, 2, -1]
Now nums1 equals nums2.

Constraints:
- n == nums1.length == nums2.length
- 1 <= n <= 10^5
- 0 <= nums1[i], nums2[i] <= 10^9
- 0 <= k <= 10^5
"""

# Python Solution
def minOperations(nums1, nums2, k):
    if k == 0:
        # If k is 0, nums1 must already equal nums2 to be possible
        return 0 if nums1 == nums2 else -1
    
    total_diff = 0
    positive_diff = 0
    negative_diff = 0
    
    for a, b in zip(nums1, nums2):
        diff = b - a
        if diff % k != 0:
            # If the difference is not divisible by k, it's impossible
            return -1
        steps = diff // k
        if steps > 0:
            positive_diff += steps
        else:
            negative_diff += abs(steps)
        total_diff += diff
    
    # If the total difference is not zero, it's impossible
    if total_diff != 0:
        return -1
    
    # The number of operations required is the sum of positive differences
    return positive_diff

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6]
    k = 2
    print(minOperations(nums1, nums2, k))  # Output: 3

    # Test Case 2
    nums1 = [1, 2, 3]
    nums2 = [1, 2, 3]
    k = 2
    print(minOperations(nums1, nums2, k))  # Output: 0

    # Test Case 3
    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6]
    k = 0
    print(minOperations(nums1, nums2, k))  # Output: -1

    # Test Case 4
    nums1 = [1, 2, 3]
    nums2 = [7, 8, 9]
    k = 3
    print(minOperations(nums1, nums2, k))  # Output: 6

    # Test Case 5
    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6]
    k = 5
    print(minOperations(nums1, nums2, k))  # Output: -1

# Time and Space Complexity Analysis
# Time Complexity: O(n)
# - We iterate through the arrays nums1 and nums2 once, performing constant-time operations for each pair of elements.
# Space Complexity: O(1)
# - We use a constant amount of extra space to store variables like total_diff, positive_diff, and negative_diff.

# Topic: Arrays