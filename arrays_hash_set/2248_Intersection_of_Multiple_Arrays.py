"""
LeetCode Problem #2248: Intersection of Multiple Arrays

Problem Statement:
Given a 2D integer array `nums` where `nums[i]` is a non-empty array of distinct positive integers, 
return the list of integers that are present in each array of `nums` sorted in ascending order.

Example 1:
Input: nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
Output: [3,4]
Explanation: 
The integers that are present in each array are:
- 3, because it appears in all arrays.
- 4, because it appears in all arrays.
Hence, the intersection is [3,4].

Example 2:
Input: nums = [[1,2,3],[4,5,6]]
Output: []
Explanation: 
There is no integer present in all arrays.

Constraints:
- `1 <= nums.length <= 1000`
- `1 <= nums[i].length <= 1000`
- `1 <= nums[i][j] <= 1000`
- All the integers in `nums[i]` are distinct.
"""

# Clean and Correct Python Solution
from typing import List

def intersection(nums: List[List[int]]) -> List[int]:
    # Start with the set of the first array
    result_set = set(nums[0])
    
    # Intersect with the sets of the remaining arrays
    for arr in nums[1:]:
        result_set &= set(arr)
    
    # Return the sorted list of the intersection
    return sorted(result_set)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]
    print(intersection(nums1))  # Output: [3, 4]

    # Test Case 2
    nums2 = [[1, 2, 3], [4, 5, 6]]
    print(intersection(nums2))  # Output: []

    # Test Case 3
    nums3 = [[1, 2, 3, 4], [2, 3, 4], [3, 4]]
    print(intersection(nums3))  # Output: [3, 4]

    # Test Case 4
    nums4 = [[1], [1], [1]]
    print(intersection(nums4))  # Output: [1]

    # Test Case 5
    nums5 = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
    print(intersection(nums5))  # Output: [3]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Let `n` be the number of arrays in `nums` and `m` be the average length of each array.
- Converting each array to a set takes O(m) time.
- Intersecting two sets takes O(min(len(set1), len(set2))) time. In the worst case, this is O(m).
- Since we perform the intersection operation for `n-1` arrays, the total time complexity is O(n * m).

Space Complexity:
- The space complexity is O(m) for storing the intermediate result set.
- Additionally, converting each array to a set also requires O(m) space.
- Therefore, the overall space complexity is O(m).
"""

# Topic: Arrays, Hash Set