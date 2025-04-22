"""
LeetCode Problem #349: Intersection of Two Arrays

Problem Statement:
Given two integer arrays `nums1` and `nums2`, return an array of their intersection. 
Each element in the result must be unique, and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.

Constraints:
- 1 <= nums1.length, nums2.length <= 1000
- 0 <= nums1[i], nums2[i] <= 10^9
"""

# Solution
def intersection(nums1, nums2):
    """
    Finds the intersection of two arrays, returning unique elements.

    Args:
    nums1 (List[int]): First list of integers.
    nums2 (List[int]): Second list of integers.

    Returns:
    List[int]: List of unique integers that are present in both nums1 and nums2.
    """
    # Convert both lists to sets to remove duplicates and find the intersection
    set1 = set(nums1)
    set2 = set(nums2)
    return list(set1 & set2)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print(intersection(nums1, nums2))  # Output: [2]

    # Test Case 2
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    print(intersection(nums1, nums2))  # Output: [9, 4] or [4, 9]

    # Test Case 3
    nums1 = [1, 2, 3, 4]
    nums2 = [5, 6, 7, 8]
    print(intersection(nums1, nums2))  # Output: []

    # Test Case 4
    nums1 = [1, 1, 1, 1]
    nums2 = [1, 1, 1, 1]
    print(intersection(nums1, nums2))  # Output: [1]

    # Test Case 5
    nums1 = []
    nums2 = [1, 2, 3]
    print(intersection(nums1, nums2))  # Output: []

# Time and Space Complexity Analysis
"""
Time Complexity:
- Converting nums1 and nums2 to sets takes O(n + m), where n is the length of nums1 and m is the length of nums2.
- Finding the intersection of two sets takes O(min(n, m)).
- Converting the resulting set to a list takes O(k), where k is the size of the intersection.
Overall: O(n + m)

Space Complexity:
- The space required to store the sets is O(n + m).
- The space required to store the result is O(k), where k is the size of the intersection.
Overall: O(n + m)
"""

# Topic: Arrays, Hashing