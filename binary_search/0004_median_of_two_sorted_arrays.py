"""
LeetCode Question #4: Median of Two Sorted Arrays

Problem Statement:
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Constraints:
- nums1 and nums2 are sorted in non-decreasing order.
- 0 <= m, n <= 1000
- -10^6 <= nums1[i], nums2[i] <= 10^6
- The median is defined as:
  - If the combined length of the arrays is odd, the median is the middle element.
  - If the combined length is even, the median is the average of the two middle elements.

Example:
Input: nums1 = [1, 3], nums2 = [2]
Output: 2.0

Input: nums1 = [1, 2], nums2 = [3, 4]
Output: 2.5
"""

def findMedianSortedArrays(nums1, nums2):
    """
    Finds the median of two sorted arrays using binary search.

    Args:
    nums1 (List[int]): First sorted array.
    nums2 (List[int]): Second sorted array.

    Returns:
    float: The median of the two sorted arrays.
    """
    # Ensure nums1 is the smaller array
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    total_length = m + n
    half_length = total_length // 2

    # Binary search on the smaller array
    left, right = 0, m
    while left <= right:
        partition1 = (left + right) // 2
        partition2 = half_length - partition1

        # Get the values around the partitions
        left1 = nums1[partition1 - 1] if partition1 > 0 else float('-inf')
        right1 = nums1[partition1] if partition1 < m else float('inf')
        left2 = nums2[partition2 - 1] if partition2 > 0 else float('-inf')
        right2 = nums2[partition2] if partition2 < n else float('inf')

        # Check if partitions are valid
        if left1 <= right2 and left2 <= right1:
            # Found the correct partition
            if total_length % 2 == 0:
                return (max(left1, left2) + min(right1, right2)) / 2.0
            else:
                return min(right1, right2)
        elif left1 > right2:
            # Move partition1 to the left
            right = partition1 - 1
        else:
            # Move partition1 to the right
            left = partition1 + 1

    raise ValueError("Input arrays are not sorted or invalid.")

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 3]
    nums2 = [2]
    print(findMedianSortedArrays(nums1, nums2))  # Output: 2.0

    # Test Case 2
    nums1 = [1, 2]
    nums2 = [3, 4]
    print(findMedianSortedArrays(nums1, nums2))  # Output: 2.5

    # Test Case 3
    nums1 = [0, 0]
    nums2 = [0, 0]
    print(findMedianSortedArrays(nums1, nums2))  # Output: 0.0

    # Test Case 4
    nums1 = []
    nums2 = [1]
    print(findMedianSortedArrays(nums1, nums2))  # Output: 1.0

    # Test Case 5
    nums1 = [2]
    nums2 = []
    print(findMedianSortedArrays(nums1, nums2))  # Output: 2.0

"""
Time and Space Complexity Analysis:

Time Complexity:
- The binary search is performed on the smaller array, which has a length of m.
- Each iteration of the binary search reduces the search space by half.
- Therefore, the time complexity is O(log(min(m, n))).

Space Complexity:
- The algorithm uses a constant amount of extra space.
- Therefore, the space complexity is O(1).

Topic: Binary Search
"""