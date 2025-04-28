"""
LeetCode Problem #1906: Minimum Absolute Difference Queries

Problem Statement:
You are given an integer array nums and an array queries where queries[i] = [li, ri]. 
For each query i, compute the minimum absolute difference between any two elements in the subarray nums[li...ri] 
(a subarray is defined as a contiguous subsequence of the array nums).

Return an array ans where ans[i] is the answer to the ith query. If no such pair exists, return -1.

The minimum absolute difference of an array is the smallest absolute difference between any two of its elements.

Example:
Input: nums = [1,3,4,8], queries = [[0,1],[1,2],[2,3],[0,3]]
Output: [2,1,4,1]
Explanation:
The queries are processed as follows:
- queries[0] = [0,1]: The subarray is [1,3] and the minimum absolute difference is |1-3| = 2.
- queries[1] = [1,2]: The subarray is [3,4] and the minimum absolute difference is |3-4| = 1.
- queries[2] = [2,3]: The subarray is [4,8] and the minimum absolute difference is |4-8| = 4.
- queries[3] = [0,3]: The subarray is [1,3,4,8] and the minimum absolute difference is |3-4| = 1.

Constraints:
- 2 <= nums.length <= 10^5
- 1 <= nums[i] <= 100
- 1 <= queries.length <= 10^4
- 0 <= li < ri < nums.length
"""

from typing import List

def minDifference(nums: List[int], queries: List[List[int]]) -> List[int]:
    # Precompute prefix frequency for numbers in the range [1, 100]
    max_val = 100
    n = len(nums)
    prefix_freq = [[0] * (max_val + 1) for _ in range(n + 1)]
    
    for i in range(n):
        for j in range(1, max_val + 1):
            prefix_freq[i + 1][j] = prefix_freq[i][j]
        prefix_freq[i + 1][nums[i]] += 1

    result = []
    for l, r in queries:
        # Find all unique numbers in the range [l, r]
        unique_nums = []
        for num in range(1, max_val + 1):
            if prefix_freq[r + 1][num] - prefix_freq[l][num] > 0:
                unique_nums.append(num)
        
        # Compute the minimum absolute difference
        if len(unique_nums) < 2:
            result.append(-1)
        else:
            min_diff = float('inf')
            for i in range(1, len(unique_nums)):
                min_diff = min(min_diff, unique_nums[i] - unique_nums[i - 1])
            result.append(min_diff)
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums = [1, 3, 4, 8]
    queries = [[0, 1], [1, 2], [2, 3], [0, 3]]
    print(minDifference(nums, queries))  # Output: [2, 1, 4, 1]

    # Test Case 2
    nums = [4, 2, 1, 10]
    queries = [[0, 3], [1, 2], [0, 1]]
    print(minDifference(nums, queries))  # Output: [1, 1, 2]

    # Test Case 3
    nums = [1, 1, 1, 1]
    queries = [[0, 3], [1, 2]]
    print(minDifference(nums, queries))  # Output: [-1, -1]

"""
Time Complexity:
- Precomputing the prefix frequency array takes O(n * max_val), where n is the length of nums and max_val is 100.
- For each query, we iterate over the range [1, 100], which takes O(max_val) per query.
- Total complexity: O(n * max_val + q * max_val), where q is the number of queries.
- Since max_val is constant (100), this simplifies to O(n + q).

Space Complexity:
- The prefix frequency array takes O(n * max_val) space.
- The space complexity is O(n) since max_val is constant.

Topic: Arrays, Prefix Sum
"""