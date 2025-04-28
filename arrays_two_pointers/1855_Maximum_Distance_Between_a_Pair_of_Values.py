"""
LeetCode Problem #1855: Maximum Distance Between a Pair of Values

Problem Statement:
You are given two non-increasing 0-indexed integer arrays `nums1` and `nums2`.

A pair of indices `(i, j)` is valid if:
- 0 <= i < nums1.length
- 0 <= j < nums2.length
- nums1[i] <= nums2[j]

The distance of the pair is `j - i` (the difference between the indices).

Return the maximum distance of any valid pair `(i, j)`. If there are no valid pairs, return 0.

Example 1:
Input: nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5]
Output: 2
Explanation: The valid pairs are:
- (0,0), distance = 0
- (1,1), distance = 0
- (2,2), distance = 0
- (2,3), distance = 1
- (2,4), distance = 2
The maximum distance is 2.

Example 2:
Input: nums1 = [2,2,2], nums2 = [10,10,1]
Output: 1
Explanation: The valid pairs are:
- (0,0), distance = 0
- (0,1), distance = 1
- (1,1), distance = 0
- (2,2), distance = 0
The maximum distance is 1.

Example 3:
Input: nums1 = [30,29,19,5], nums2 = [25,25,25,25,25]
Output: 2
Explanation: The valid pairs are:
- (2,2), distance = 0
- (2,3), distance = 1
- (2,4), distance = 2
The maximum distance is 2.

Constraints:
- 1 <= nums1.length, nums2.length <= 10^5
- 1 <= nums1[i], nums2[j] <= 10^5
- Both nums1 and nums2 are non-increasing.
"""

# Python Solution
def maxDistance(nums1, nums2):
    """
    Finds the maximum distance between a valid pair of indices (i, j) such that nums1[i] <= nums2[j].
    
    Args:
    nums1 (List[int]): A non-increasing list of integers.
    nums2 (List[int]): A non-increasing list of integers.
    
    Returns:
    int: The maximum distance of any valid pair (i, j).
    """
    i, j = 0, 0
    max_dist = 0
    n, m = len(nums1), len(nums2)
    
    while i < n and j < m:
        if nums1[i] <= nums2[j]:
            max_dist = max(max_dist, j - i)
            j += 1
        else:
            i += 1
    
    return max_dist

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [55, 30, 5, 4, 2]
    nums2 = [100, 20, 10, 10, 5]
    print(maxDistance(nums1, nums2))  # Output: 2

    # Test Case 2
    nums1 = [2, 2, 2]
    nums2 = [10, 10, 1]
    print(maxDistance(nums1, nums2))  # Output: 1

    # Test Case 3
    nums1 = [30, 29, 19, 5]
    nums2 = [25, 25, 25, 25, 25]
    print(maxDistance(nums1, nums2))  # Output: 2

    # Test Case 4
    nums1 = [10, 9, 8, 7]
    nums2 = [10, 10, 10, 10]
    print(maxDistance(nums1, nums2))  # Output: 3

    # Test Case 5
    nums1 = [1]
    nums2 = [1]
    print(maxDistance(nums1, nums2))  # Output: 0

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm uses two pointers (i and j) to traverse nums1 and nums2.
- In the worst case, each pointer moves at most once through its respective array.
- Therefore, the time complexity is O(n + m), where n is the length of nums1 and m is the length of nums2.

Space Complexity:
- The algorithm uses a constant amount of extra space, so the space complexity is O(1).
"""

# Topic: Arrays, Two Pointers