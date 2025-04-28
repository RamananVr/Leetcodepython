"""
LeetCode Problem #2099: Find Subsequence of Length K With the Largest Sum

Problem Statement:
You are given an integer array `nums` and an integer `k`. You want to find a subsequence of `nums` of length `k` that has the largest sum.

Return any such subsequence as an integer array of length `k`.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

Example 1:
Input: nums = [2,1,3,3], k = 2
Output: [3,3]
Explanation:
The subsequence has the largest sum of 6. Note that there are other subsequences of size 2 with the same sum, but [3,3] is returned.

Example 2:
Input: nums = [-1,-2,3,4], k = 3
Output: [-1,3,4]
Explanation:
The subsequence has the largest sum of 6.

Example 3:
Input: nums = [3,4,3,3], k = 2
Output: [4,3]
Explanation:
The subsequence has the largest sum of 7. Note that there are other subsequences of size 2 with the same sum, but [4,3] is returned.

Constraints:
- 1 <= nums.length <= 1000
- -10^5 <= nums[i] <= 10^5
- 1 <= k <= nums.length
"""

# Python Solution
from typing import List

def maxSubsequence(nums: List[int], k: int) -> List[int]:
    # Step 1: Pair each number with its index
    indexed_nums = [(num, i) for i, num in enumerate(nums)]
    
    # Step 2: Sort by value in descending order
    indexed_nums.sort(key=lambda x: x[0], reverse=True)
    
    # Step 3: Take the top k elements
    top_k = indexed_nums[:k]
    
    # Step 4: Sort the top k elements by their original indices
    top_k.sort(key=lambda x: x[1])
    
    # Step 5: Extract the values and return
    return [num for num, _ in top_k]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 1, 3, 3]
    k1 = 2
    print(maxSubsequence(nums1, k1))  # Output: [3, 3]

    # Test Case 2
    nums2 = [-1, -2, 3, 4]
    k2 = 3
    print(maxSubsequence(nums2, k2))  # Output: [-1, 3, 4]

    # Test Case 3
    nums3 = [3, 4, 3, 3]
    k3 = 2
    print(maxSubsequence(nums3, k3))  # Output: [4, 3]

    # Test Case 4
    nums4 = [1, 2, 3, 4, 5]
    k4 = 3
    print(maxSubsequence(nums4, k4))  # Output: [3, 4, 5]

    # Test Case 5
    nums5 = [10, -10, 20, -20, 30]
    k5 = 2
    print(maxSubsequence(nums5, k5))  # Output: [20, 30]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Pairing each number with its index takes O(n), where n is the length of nums.
- Sorting the array by value takes O(n log n).
- Sorting the top k elements by their original indices takes O(k log k).
- Extracting the values takes O(k).
Overall: O(n log n) due to the initial sort.

Space Complexity:
- The indexed_nums list takes O(n) space.
- The top_k list takes O(k) space.
Overall: O(n) space.
"""

# Topic: Arrays