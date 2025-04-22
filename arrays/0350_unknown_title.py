"""
LeetCode Problem #350: Intersection of Two Arrays II

Problem Statement:
Given two integer arrays `nums1` and `nums2`, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays, 
and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.

Constraints:
- 1 <= nums1.length, nums2.length <= 1000
- 0 <= nums1[i], nums2[i] <= 1000

Follow up:
- What if the given array is already sorted? How would you optimize your algorithm?
- What if nums1's size is small compared to nums2's size? Which algorithm is better?
- What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into memory at once?
"""

# Clean and Correct Python Solution
from collections import Counter
from typing import List

def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    Finds the intersection of two arrays, allowing duplicate elements.
    """
    # Count the occurrences of each number in both arrays
    count1 = Counter(nums1)
    count2 = Counter(nums2)
    
    # Find the intersection by taking the minimum count for each element
    intersection = []
    for num in count1:
        if num in count2:
            intersection.extend([num] * min(count1[num], count2[num]))
    
    return intersection

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print(intersect(nums1, nums2))  # Output: [2, 2]

    # Test Case 2
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    print(intersect(nums1, nums2))  # Output: [4, 9] or [9, 4]

    # Test Case 3
    nums1 = [1, 1, 1, 2]
    nums2 = [1, 1, 3]
    print(intersect(nums1, nums2))  # Output: [1, 1]

    # Test Case 4
    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6]
    print(intersect(nums1, nums2))  # Output: []

# Time and Space Complexity Analysis
"""
Time Complexity:
- Counting the elements in nums1 and nums2 takes O(n + m), where n is the length of nums1 and m is the length of nums2.
- Iterating through the keys of count1 and finding the intersection takes O(k), where k is the number of unique elements in nums1.
- Overall time complexity: O(n + m).

Space Complexity:
- The space required for the Counter objects is O(n + m), where n and m are the lengths of nums1 and nums2.
- The space required for the output list depends on the size of the intersection, which is at most O(min(n, m)).
- Overall space complexity: O(n + m).
"""

# Topic: Arrays