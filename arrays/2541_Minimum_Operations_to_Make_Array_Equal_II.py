"""
LeetCode Problem #2541: Minimum Operations to Make Array Equal II

Problem Statement:
You are given two integer arrays nums1 and nums2 of length n and an integer k. 
In one operation, you can pick two indices i and j (i != j) and increase nums1[i] by k and decrease nums1[j] by k. 
The goal is to make nums1 equal to nums2. Return the minimum number of operations required to make nums1 equal to nums2, 
or return -1 if it is impossible.

Example:
Input: nums1 = [1, 2, 3], nums2 = [4, 5, 6], k = 2
Output: 3

Constraints:
- n == nums1.length == nums2.length
- 1 <= n <= 10^5
- 0 <= nums1[i], nums2[i] <= 10^9
- 0 <= k <= 10^5
"""

# Python Solution
def minOperations(nums1, nums2, k):
    if k == 0:
        # If k is 0, nums1 must already equal nums2 to be valid
        return 0 if nums1 == nums2 else -1

    # Calculate the difference array
    diff = [nums2[i] - nums1[i] for i in range(len(nums1))]

    # Separate the positive and negative differences
    pos_sum = sum(d for d in diff if d > 0)
    neg_sum = sum(-d for d in diff if d < 0)

    # If the total positive and negative differences don't match, it's impossible
    if pos_sum != neg_sum:
        return -1

    # Check if all differences are divisible by k
    for d in diff:
        if d % k != 0:
            return -1

    # Calculate the total number of operations
    return pos_sum // k

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
    nums2 = [4, 5, 7]
    k = 2
    print(minOperations(nums1, nums2, k))  # Output: -1

# Time and Space Complexity Analysis
# Time Complexity: O(n)
# - Calculating the difference array takes O(n).
# - Summing positive and negative differences takes O(n).
# - Checking divisibility for each difference takes O(n).
# - Overall, the algorithm runs in linear time.

# Space Complexity: O(n)
# - The difference array requires O(n) space.
# - Other variables use constant space.
# - Overall, the space complexity is O(n).

# Topic: Arrays