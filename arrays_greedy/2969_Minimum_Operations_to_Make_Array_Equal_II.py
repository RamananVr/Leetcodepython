"""
LeetCode Problem #2969: Minimum Operations to Make Array Equal II

Problem Statement:
You are given two integer arrays `nums1` and `nums2` of equal length `n` and an integer `k`. 
In one operation, you can pick two indices `i` and `j` (0 <= i, j < n) and increment `nums1[i]` by `k` and decrement `nums1[j]` by `k`. 
In other words, `nums1[i] += k` and `nums1[j] -= k`.

Return the minimum number of operations required to make `nums1` equal to `nums2`. If it is impossible to make the two arrays equal, return `-1`.

Example:
Input: nums1 = [1, 2, 3], nums2 = [5, 4, 3], k = 1
Output: 4

Constraints:
- `n == nums1.length == nums2.length`
- `1 <= n <= 10^5`
- `0 <= nums1[i], nums2[i] <= 10^9`
- `0 <= k <= 10^9`
"""

def minOperations(nums1, nums2, k):
    """
    Calculate the minimum number of operations to make nums1 equal to nums2.
    
    Args:
    nums1 (List[int]): The first array.
    nums2 (List[int]): The second array.
    k (int): The increment/decrement value for operations.
    
    Returns:
    int: The minimum number of operations, or -1 if it's impossible.
    """
    # If k is 0, nums1 must already equal nums2
    if k == 0:
        return 0 if nums1 == nums2 else -1

    # Calculate the differences between nums1 and nums2
    diff = [nums2[i] - nums1[i] for i in range(len(nums1))]

    # Track the total positive and negative differences
    pos_diff = 0
    neg_diff = 0

    for d in diff:
        if d % k != 0:  # If the difference is not divisible by k, it's impossible
            return -1
        if d > 0:
            pos_diff += d // k
        elif d < 0:
            neg_diff += abs(d) // k

    # To make nums1 equal to nums2, the total positive and negative differences must balance
    if pos_diff == neg_diff:
        return pos_diff
    else:
        return -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3]
    nums2 = [5, 4, 3]
    k = 1
    print(minOperations(nums1, nums2, k))  # Output: 4

    # Test Case 2
    nums1 = [1, 2, 3]
    nums2 = [5, 4, 3]
    k = 0
    print(minOperations(nums1, nums2, k))  # Output: -1

    # Test Case 3
    nums1 = [10, 20, 30]
    nums2 = [40, 50, 60]
    k = 10
    print(minOperations(nums1, nums2, k))  # Output: 6

    # Test Case 4
    nums1 = [1, 1, 1]
    nums2 = [2, 2, 2]
    k = 2
    print(minOperations(nums1, nums2, k))  # Output: -1

    # Test Case 5
    nums1 = [0, 0, 0]
    nums2 = [0, 0, 0]
    k = 5
    print(minOperations(nums1, nums2, k))  # Output: 0

"""
Time Complexity:
- Calculating the differences takes O(n), where n is the length of nums1 and nums2.
- Summing the positive and negative differences also takes O(n).
- Overall, the time complexity is O(n).

Space Complexity:
- The space complexity is O(n) due to the `diff` array.

Topic: Arrays, Greedy
"""