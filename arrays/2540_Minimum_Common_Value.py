"""
LeetCode Problem #2540: Minimum Common Value

Problem Statement:
Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer that is a common value between the two arrays. If there is no common value, return -1.

Note:
- An integer x is a common value between nums1 and nums2 if x is present in both arrays.

Constraints:
- 1 <= nums1.length, nums2.length <= 10^5
- 1 <= nums1[i], nums2[i] <= 10^9
- Both nums1 and nums2 are sorted in non-decreasing order.
"""

def getCommon(nums1, nums2):
    """
    Finds the minimum common value between two sorted arrays.

    Args:
    nums1 (List[int]): First sorted array.
    nums2 (List[int]): Second sorted array.

    Returns:
    int: Minimum common value, or -1 if no common value exists.
    """
    # Use two pointers to traverse both arrays
    i, j = 0, 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            return nums1[i]  # Return the first common value found
        elif nums1[i] < nums2[j]:
            i += 1  # Move the pointer in nums1 forward
        else:
            j += 1  # Move the pointer in nums2 forward
    return -1  # No common value found

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Common value exists
    nums1 = [1, 2, 3, 6]
    nums2 = [2, 3, 4, 5]
    print(getCommon(nums1, nums2))  # Output: 2

    # Test Case 2: No common value
    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6]
    print(getCommon(nums1, nums2))  # Output: -1

    # Test Case 3: Common value is the smallest element
    nums1 = [1, 2, 3]
    nums2 = [1, 4, 5]
    print(getCommon(nums1, nums2))  # Output: 1

    # Test Case 4: Large arrays with a common value
    nums1 = [1, 3, 5, 7, 9]
    nums2 = [2, 4, 6, 7, 8]
    print(getCommon(nums1, nums2))  # Output: 7

    # Test Case 5: Arrays with duplicate values
    nums1 = [1, 1, 2, 3]
    nums2 = [1, 1, 4, 5]
    print(getCommon(nums1, nums2))  # Output: 1

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm uses two pointers to traverse both arrays. In the worst case, each pointer traverses its respective array entirely.
- Therefore, the time complexity is O(n + m), where n is the length of nums1 and m is the length of nums2.

Space Complexity:
- The algorithm uses a constant amount of extra space (only two pointers and a few variables).
- Therefore, the space complexity is O(1).

Topic: Arrays
"""