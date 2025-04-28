"""
LeetCode Question #1885: Count Pairs in Two Arrays

Problem Statement:
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k. 
A pair (i, j) is called a good pair if nums1[i] + nums2[j] < k. Return the number of good pairs.

Constraints:
- 1 <= nums1.length, nums2.length <= 10^5
- -10^9 <= nums1[i], nums2[j] <= 10^9
- nums1 and nums2 are sorted in ascending order.

"""

# Solution
def countPairs(nums1, nums2, k):
    """
    Counts the number of good pairs (i, j) such that nums1[i] + nums2[j] < k.

    Args:
    nums1 (List[int]): First sorted array.
    nums2 (List[int]): Second sorted array.
    k (int): Target sum.

    Returns:
    int: Number of good pairs.
    """
    count = 0
    j = len(nums2) - 1

    for i in range(len(nums1)):
        while j >= 0 and nums1[i] + nums2[j] >= k:
            j -= 1
        count += (j + 1)

    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3]
    nums2 = [1, 2, 3]
    k = 5
    print(countPairs(nums1, nums2, k))  # Expected Output: 4

    # Test Case 2
    nums1 = [1, 2]
    nums2 = [3, 4]
    k = 6
    print(countPairs(nums1, nums2, k))  # Expected Output: 2

    # Test Case 3
    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6]
    k = 10
    print(countPairs(nums1, nums2, k))  # Expected Output: 9

    # Test Case 4
    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6]
    k = 3
    print(countPairs(nums1, nums2, k))  # Expected Output: 0

# Time and Space Complexity Analysis
"""
Time Complexity:
- The outer loop iterates through nums1, which has a length of n1.
- The inner loop (while loop) iterates through nums2, which has a length of n2.
- Since the while loop only moves the pointer j backward, the total number of iterations across all loops is O(n1 + n2).
- Therefore, the time complexity is O(n1 + n2).

Space Complexity:
- The algorithm uses a constant amount of extra space, so the space complexity is O(1).

Where n1 = len(nums1) and n2 = len(nums2).
"""

# Topic: Arrays, Two Pointers