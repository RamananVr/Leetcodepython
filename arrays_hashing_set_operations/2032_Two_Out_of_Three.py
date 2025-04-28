"""
LeetCode Problem #2032: Two Out of Three

Problem Statement:
Given three integer arrays `nums1`, `nums2`, and `nums3`, return a distinct array containing all the values that are present in at least two out of the three arrays. 
You may return the values in any order.

Example 1:
Input: nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3]
Output: [3,2]
Explanation: The values that are present in at least two arrays are:
- 3, which is present in all three arrays.
- 2, which is present in nums1 and nums2.

Example 2:
Input: nums1 = [3,1], nums2 = [2,3], nums3 = [1,2]
Output: [2,3,1]
Explanation: The values that are present in at least two arrays are:
- 2, which is present in nums2 and nums3.
- 3, which is present in nums1 and nums2.
- 1, which is present in nums1 and nums3.

Example 3:
Input: nums1 = [1,2,2], nums2 = [4,3,3], nums3 = [5]
Output: []
Explanation: No value is present in at least two arrays.

Constraints:
- 1 <= nums1.length, nums2.length, nums3.length <= 100
- 1 <= nums1[i], nums2[i], nums3[i] <= 100
"""

# Solution
def twoOutOfThree(nums1, nums2, nums3):
    """
    Returns a list of distinct integers that are present in at least two out of the three input arrays.

    Args:
    nums1 (List[int]): First list of integers.
    nums2 (List[int]): Second list of integers.
    nums3 (List[int]): Third list of integers.

    Returns:
    List[int]: List of integers present in at least two arrays.
    """
    # Convert each list to a set to remove duplicates
    set1, set2, set3 = set(nums1), set(nums2), set(nums3)
    
    # Find the union of intersections between any two sets
    result = (set1 & set2) | (set2 & set3) | (set1 & set3)
    
    # Convert the result to a list and return
    return list(result)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 1, 3, 2]
    nums2 = [2, 3]
    nums3 = [3]
    print(twoOutOfThree(nums1, nums2, nums3))  # Output: [3, 2]

    # Test Case 2
    nums1 = [3, 1]
    nums2 = [2, 3]
    nums3 = [1, 2]
    print(twoOutOfThree(nums1, nums2, nums3))  # Output: [2, 3, 1]

    # Test Case 3
    nums1 = [1, 2, 2]
    nums2 = [4, 3, 3]
    nums3 = [5]
    print(twoOutOfThree(nums1, nums2, nums3))  # Output: []

    # Test Case 4
    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6]
    nums3 = [7, 8, 9]
    print(twoOutOfThree(nums1, nums2, nums3))  # Output: []

    # Test Case 5
    nums1 = [1, 2, 3]
    nums2 = [3, 4, 5]
    nums3 = [5, 6, 1]
    print(twoOutOfThree(nums1, nums2, nums3))  # Output: [1, 3, 5]

# Time Complexity Analysis:
# - Converting each list to a set takes O(n1 + n2 + n3), where n1, n2, and n3 are the lengths of nums1, nums2, and nums3 respectively.
# - Calculating the intersections and union of sets takes O(min(n1, n2) + min(n2, n3) + min(n1, n3)).
# - Converting the result set to a list takes O(k), where k is the size of the result set.
# Overall Time Complexity: O(n1 + n2 + n3)

# Space Complexity Analysis:
# - The space required to store the sets is O(n1 + n2 + n3).
# - The result set requires O(k) space.
# Overall Space Complexity: O(n1 + n2 + n3)

# Topic: Arrays, Hashing, Set Operations