"""
LeetCode Problem #2389: Longest Subsequence With Limited Sum

Problem Statement:
You are given an integer array `nums` of length `n`, and an integer array `queries` of length `m`.

You want to determine the maximum size of a subsequence of `nums` such that the sum of the subsequence is less than or equal to the value of each query in `queries`.

Return an array `answer` of length `m` where `answer[i]` is the maximum size of a subsequence that has a sum less than or equal to `queries[i]`.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

Constraints:
- `n == nums.length`
- `m == queries.length`
- `1 <= n, m <= 1000`
- `1 <= nums[i], queries[i] <= 10^6`
"""

from typing import List
import bisect

def answerQueries(nums: List[int], queries: List[int]) -> List[int]:
    """
    Function to find the maximum size of a subsequence with a sum less than or equal to each query.
    """
    # Sort the nums array to consider the smallest elements first
    nums.sort()
    
    # Compute the prefix sum of the sorted nums array
    prefix_sum = []
    current_sum = 0
    for num in nums:
        current_sum += num
        prefix_sum.append(current_sum)
    
    # For each query, use binary search to find the maximum size of the subsequence
    result = []
    for query in queries:
        # Use bisect_right to find the position where the query would fit in the prefix_sum
        max_size = bisect.bisect_right(prefix_sum, query)
        result.append(max_size)
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums = [4, 5, 2, 1]
    queries = [3, 10, 21]
    print(answerQueries(nums, queries))  # Output: [2, 3, 4]

    # Test Case 2
    nums = [2, 3, 4, 5]
    queries = [1, 7, 15]
    print(answerQueries(nums, queries))  # Output: [0, 2, 4]

    # Test Case 3
    nums = [1, 1, 1, 1]
    queries = [2, 3, 4]
    print(answerQueries(nums, queries))  # Output: [2, 3, 4]

"""
Time Complexity Analysis:
1. Sorting the `nums` array takes O(n log n), where n is the length of the `nums` array.
2. Computing the prefix sum takes O(n).
3. For each query, performing a binary search on the prefix sum array takes O(log n). Since there are m queries, this step takes O(m log n).

Overall Time Complexity: O(n log n + m log n)

Space Complexity Analysis:
1. The `prefix_sum` array takes O(n) space.
2. The result array takes O(m) space.

Overall Space Complexity: O(n + m)

Topic: Arrays, Binary Search
"""