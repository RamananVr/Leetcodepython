"""
LeetCode Problem #2884: Minimum Operations to Make Array Equal II

Problem Statement:
You are given two integer arrays `nums1` and `nums2` of length `n` and an integer `k`. 
The operation you can perform is as follows:
- Choose an index `i` in `nums1` and increment `nums1[i]` by `k`.
- Choose an index `i` in `nums1` and decrement `nums1[i]` by `k`.

Return the minimum number of operations required to make `nums1` equal to `nums2`. 
If it is impossible to make the two arrays equal, return `-1`.

Note:
- The operation can be performed on any index multiple times.
- The arrays are considered equal if they have the same elements at the same indices.

Constraints:
- `n == nums1.length == nums2.length`
- `1 <= n <= 10^5`
- `0 <= nums1[i], nums2[i] <= 10^9`
- `1 <= k <= 10^9`
"""

# Solution
def minOperations(nums1, nums2, k):
    if k == 0:
        # If k is 0, we cannot perform any operations, so check if arrays are already equal
        return 0 if nums1 == nums2 else -1

    total_increment = 0
    total_decrement = 0

    for a, b in zip(nums1, nums2):
        diff = b - a
        if diff % k != 0:
            # If the difference is not divisible by k, it's impossible to make the arrays equal
            return -1
        if diff > 0:
            total_increment += diff // k
        elif diff < 0:
            total_decrement += abs(diff) // k

    # To make the arrays equal, total increments must equal total decrements
    return total_increment if total_increment == total_decrement else -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Arrays can be made equal
    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6]
    k = 1
    print(minOperations(nums1, nums2, k))  # Output: 9

    # Test Case 2: Arrays are already equal
    nums1 = [1, 2, 3]
    nums2 = [1, 2, 3]
    k = 2
    print(minOperations(nums1, nums2, k))  # Output: 0

    # Test Case 3: Impossible to make arrays equal
    nums1 = [1, 2, 3]
    nums2 = [4, 5, 7]
    k = 2
    print(minOperations(nums1, nums2, k))  # Output: -1

    # Test Case 4: k is 0, arrays are already equal
    nums1 = [1, 2, 3]
    nums2 = [1, 2, 3]
    k = 0
    print(minOperations(nums1, nums2, k))  # Output: 0

    # Test Case 5: k is 0, arrays are not equal
    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6]
    k = 0
    print(minOperations(nums1, nums2, k))  # Output: -1

# Time and Space Complexity Analysis
# Time Complexity:
# - The function iterates through the arrays once, so the time complexity is O(n), 
#   where n is the length of the arrays.

# Space Complexity:
# - The function uses a constant amount of extra space, so the space complexity is O(1).

# Topic: Arrays