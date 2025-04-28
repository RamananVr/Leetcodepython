"""
LeetCode Question #2880: Find the Difference Between Two Arrays

Problem Statement:
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:
- answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
- answer[1] is a list of all distinct integers in nums2 which are not present in nums1.

Note that the integers in the lists may be returned in any order.

Example 1:
Input: nums1 = [1,2,3], nums2 = [2,4,6]
Output: [[1,3],[4,6]]
Explanation:
- 1 and 3 are in nums1 but not in nums2.
- 4 and 6 are in nums2 but not in nums1.

Example 2:
Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
Output: [[3],[]]
Explanation:
- 3 is in nums1 but not in nums2.
- There are no numbers in nums2 that are not in nums1.

Constraints:
- 1 <= nums1.length, nums2.length <= 1000
- -1000 <= nums1[i], nums2[i] <= 1000
"""

# Solution
def findDifference(nums1, nums2):
    """
    Finds the difference between two arrays.

    Args:
    nums1 (List[int]): First array of integers.
    nums2 (List[int]): Second array of integers.

    Returns:
    List[List[int]]: A list containing two lists:
                     - Distinct integers in nums1 not in nums2.
                     - Distinct integers in nums2 not in nums1.
    """
    # Convert both arrays to sets to find unique elements
    set1, set2 = set(nums1), set(nums2)
    
    # Find elements in nums1 not in nums2 and vice versa
    diff1 = list(set1 - set2)
    diff2 = list(set2 - set1)
    
    return [diff1, diff2]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3]
    nums2 = [2, 4, 6]
    print(findDifference(nums1, nums2))  # Expected Output: [[1, 3], [4, 6]]

    # Test Case 2
    nums1 = [1, 2, 3, 3]
    nums2 = [1, 1, 2, 2]
    print(findDifference(nums1, nums2))  # Expected Output: [[3], []]

    # Test Case 3
    nums1 = [5, 10, 15]
    nums2 = [10, 20, 30]
    print(findDifference(nums1, nums2))  # Expected Output: [[5, 15], [20, 30]]

    # Test Case 4
    nums1 = [1, 1, 1]
    nums2 = [2, 2, 2]
    print(findDifference(nums1, nums2))  # Expected Output: [[1], [2]]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Converting nums1 and nums2 to sets takes O(n1 + n2), where n1 and n2 are the lengths of nums1 and nums2 respectively.
- Finding the difference between two sets takes O(min(n1, n2)).
- Constructing the result lists takes O(k1 + k2), where k1 and k2 are the sizes of the resulting lists.

Overall time complexity: O(n1 + n2)

Space Complexity:
- The space required for the sets set1 and set2 is O(n1 + n2).
- The space required for the result lists diff1 and diff2 is O(k1 + k2).

Overall space complexity: O(n1 + n2)
"""

# Topic: Arrays, Hashing