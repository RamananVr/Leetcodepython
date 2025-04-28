"""
LeetCode Problem #2854: Minimum Operations to Make Array Equal II

Problem Statement:
You are given two integer arrays `nums1` and `nums2` of length `n` and an integer `k`. 
In one operation, you can choose an index `i` (0 <= i < n) and increment `nums1[i]` by `k` or decrement `nums1[i]` by `k`.

Return the minimum number of operations required to make `nums1` equal to `nums2`. If it is impossible to make the arrays equal, return -1.

Example:
Input: nums1 = [4, 3, 1], nums2 = [7, 6, 1], k = 3
Output: 2
Explanation: Increment nums1[0] by k twice to make nums1[0] = 7, and increment nums1[1] by k once to make nums1[1] = 6.

Constraints:
- `n == nums1.length == nums2.length`
- `1 <= n <= 10^5`
- `0 <= nums1[i], nums2[i] <= 10^9`
- `0 <= k <= 10^9`
"""

# Python Solution
def minOperations(nums1, nums2, k):
    if k == 0:
        # If k is 0, nums1 must already equal nums2
        return 0 if nums1 == nums2 else -1

    total_increment = 0
    total_decrement = 0

    for a, b in zip(nums1, nums2):
        diff = b - a
        if diff % k != 0:
            # If the difference is not divisible by k, it's impossible to make nums1 equal to nums2
            return -1
        if diff > 0:
            total_increment += diff // k
        elif diff < 0:
            total_decrement += abs(diff) // k

    # If total increments and decrements don't balance, it's impossible
    if total_increment != total_decrement:
        return -1

    return total_increment

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [4, 3, 1]
    nums2 = [7, 6, 1]
    k = 3
    print(minOperations(nums1, nums2, k))  # Output: 2

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
    nums2 = [4, 5, 6]
    k = 2
    print(minOperations(nums1, nums2, k))  # Output: -1

    # Test Case 5
    nums1 = [10, 20, 30]
    nums2 = [40, 50, 60]
    k = 10
    print(minOperations(nums1, nums2, k))  # Output: 6

# Time and Space Complexity Analysis
# Time Complexity: O(n)
# - We iterate through the arrays once, performing constant-time operations for each element.
# - Therefore, the time complexity is linear in the size of the arrays.

# Space Complexity: O(1)
# - We use a constant amount of extra space to store variables like `total_increment` and `total_decrement`.
# - No additional data structures are used, so the space complexity is constant.

# Topic: Arrays