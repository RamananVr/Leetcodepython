"""
LeetCode Question #2757: Minimum Operations to Make Array Equal II

Problem Statement:
You are given two integer arrays `nums1` and `nums2` of length `n` and an integer `k`. 
In one operation, you can pick two indices `i` and `j` (1 <= i, j <= n) and increment 
`nums1[i]` by `k` and decrement `nums1[j]` by `k`. The goal is to make `nums1` equal to `nums2`.

Return the minimum number of operations required to make `nums1` equal to `nums2`. 
If it is impossible to make the arrays equal, return `-1`.

Example:
Input: nums1 = [1, 2, 3], nums2 = [2, 1, 3], k = 1
Output: 1

Constraints:
- `n == nums1.length == nums2.length`
- `1 <= n <= 10^5`
- `0 <= nums1[i], nums2[i] <= 10^9`
- `0 <= k <= 10^9`
"""

# Python Solution
def minOperations(nums1, nums2, k):
    if nums1 == nums2:
        return 0  # Arrays are already equal
    
    if k == 0:
        return -1  # Impossible to make changes if k is 0
    
    diff = [nums2[i] - nums1[i] for i in range(len(nums1))]
    positive_moves = 0
    negative_moves = 0
    
    for d in diff:
        if d % k != 0:
            return -1  # If the difference is not divisible by k, it's impossible
        if d > 0:
            positive_moves += d // k
        elif d < 0:
            negative_moves += abs(d) // k
    
    # If the total positive moves don't match the total negative moves, it's impossible
    if positive_moves != negative_moves:
        return -1
    
    return positive_moves  # Minimum operations required

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3]
    nums2 = [2, 1, 3]
    k = 1
    print(minOperations(nums1, nums2, k))  # Output: 1

    # Test Case 2
    nums1 = [4, 3, 1]
    nums2 = [1, 3, 4]
    k = 2
    print(minOperations(nums1, nums2, k))  # Output: -1

    # Test Case 3
    nums1 = [1, 5, 7]
    nums2 = [5, 1, 7]
    k = 2
    print(minOperations(nums1, nums2, k))  # Output: 2

    # Test Case 4
    nums1 = [10, 20, 30]
    nums2 = [10, 20, 30]
    k = 5
    print(minOperations(nums1, nums2, k))  # Output: 0

# Time and Space Complexity Analysis
"""
Time Complexity:
- Calculating the difference array takes O(n), where n is the length of nums1 and nums2.
- Iterating through the difference array also takes O(n).
- Overall time complexity: O(n).

Space Complexity:
- The difference array requires O(n) space.
- Overall space complexity: O(n).
"""

# Topic: Arrays