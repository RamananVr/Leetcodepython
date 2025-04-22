"""
LeetCode Question #4: Median of Two Sorted Arrays

Problem Statement:
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Example 3:
Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000

Example 4:
Input: nums1 = [], nums2 = [1]
Output: 1.00000

Example 5:
Input: nums1 = [2], nums2 = []
Output: 2.00000

Constraints:
- nums1.length == m
- nums2.length == n
- 0 <= m + n <= 2 * 10^6
- -10^6 <= nums1[i], nums2[i] <= 10^6
- nums1 and nums2 are sorted in non-decreasing order.
"""

def findMedianSortedArrays(nums1, nums2):
    """
    Finds the median of two sorted arrays using binary search.
    Time Complexity: O(log(min(m, n)))
    Space Complexity: O(1)
    """
    # Ensure nums1 is the smaller array
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    x, y = len(nums1), len(nums2)
    low, high = 0, x

    while low <= high:
        partitionX = (low + high) // 2
        partitionY = (x + y + 1) // 2 - partitionX

        # Handle edge cases for partitions
        maxX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
        minX = float('inf') if partitionX == x else nums1[partitionX]

        maxY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
        minY = float('inf') if partitionY == y else nums2[partitionY]

        # Check if we have found the correct partition
        if maxX <= minY and maxY <= minX:
            # If total length is even
            if (x + y) % 2 == 0:
                return (max(maxX, maxY) + min(minX, minY)) / 2
            # If total length is odd
            else:
                return max(maxX, maxY)
        elif maxX > minY:
            # Move towards the left in nums1
            high = partitionX - 1
        else:
            # Move towards the right in nums1
            low = partitionX + 1

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

# Topic: Binary Search