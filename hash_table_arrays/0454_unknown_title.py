"""
LeetCode Problem #454: 4Sum II

Problem Statement:
Given four integer arrays `nums1`, `nums2`, `nums3`, and `nums4` all of length `n`, return the number of tuples `(i, j, k, l)` such that:
    - 0 <= i, j, k, l < n
    - nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

Example:
Input: nums1 = [1, 2], nums2 = [-2, -1], nums3 = [-1, 2], nums4 = [0, 2]
Output: 2
Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0

Constraints:
- n == nums1.length == nums2.length == nums3.length == nums4.length
- 1 <= n <= 200
- -2^28 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 2^28
"""

# Clean and Correct Python Solution
from collections import Counter

def fourSumCount(nums1, nums2, nums3, nums4):
    """
    Function to count the number of tuples (i, j, k, l) such that:
    nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
    """
    # Step 1: Compute all possible sums of pairs from nums1 and nums2
    sum_count = Counter(a + b for a in nums1 for b in nums2)
    
    # Step 2: Count the complementary sums from nums3 and nums4
    count = 0
    for c in nums3:
        for d in nums4:
            count += sum_count[-(c + d)]
    
    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2]
    nums2 = [-2, -1]
    nums3 = [-1, 2]
    nums4 = [0, 2]
    print(fourSumCount(nums1, nums2, nums3, nums4))  # Output: 2

    # Test Case 2
    nums1 = [0]
    nums2 = [0]
    nums3 = [0]
    nums4 = [0]
    print(fourSumCount(nums1, nums2, nums3, nums4))  # Output: 1

    # Test Case 3
    nums1 = [1, 1, -1, -1]
    nums2 = [-1, -1, 1, 1]
    nums3 = [1, -1, 0, 0]
    nums4 = [0, 0, 1, -1]
    print(fourSumCount(nums1, nums2, nums3, nums4))  # Output: 16

# Time and Space Complexity Analysis
"""
Time Complexity:
- Computing all pair sums for nums1 and nums2 takes O(n^2).
- Iterating through nums3 and nums4 to find complementary sums also takes O(n^2).
- Overall time complexity: O(n^2 + n^2) = O(n^2).

Space Complexity:
- The Counter object stores up to n^2 unique sums from nums1 and nums2.
- Space complexity: O(n^2).
"""

# Topic: Hash Table, Arrays