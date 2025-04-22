"""
LeetCode Problem #88: Merge Sorted Array

Problem Statement:
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums2 into nums1 as one sorted array.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: nums1 = [1,2,2,3,5,6]

Example 2:
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: nums1 = [1]

Example 3:
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: nums1 = [1]

Constraints:
- nums1.length == m + n
- nums2.length == n
- 0 <= m, n <= 200
- 1 <= m + n <= 200
- -10^9 <= nums1[i], nums2[j] <= 10^9
"""

def merge(nums1, m, nums2, n):
    """
    Merges two sorted arrays nums1 and nums2 into nums1 in-place.

    Args:
    nums1 (List[int]): The first sorted array with extra space for nums2.
    m (int): Number of valid elements in nums1.
    nums2 (List[int]): The second sorted array.
    n (int): Number of valid elements in nums2.

    Returns:
    None: The function modifies nums1 in-place.
    """
    # Start merging from the end of nums1 and nums2
    p1, p2, p = m - 1, n - 1, m + n - 1

    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

    # If there are remaining elements in nums2, copy them
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    merge(nums1, m, nums2, n)
    print(nums1)  # Output: [1, 2, 2, 3, 5, 6]

    # Test Case 2
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    merge(nums1, m, nums2, n)
    print(nums1)  # Output: [1]

    # Test Case 3
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    merge(nums1, m, nums2, n)
    print(nums1)  # Output: [1]

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through both arrays nums1 and nums2 once.
- The total number of iterations is proportional to m + n.
- Therefore, the time complexity is O(m + n).

Space Complexity:
- The algorithm performs the merge in-place, using no additional space.
- Therefore, the space complexity is O(1).

Topic: Arrays
"""