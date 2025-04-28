"""
LeetCode Question #2569: Handling Queries in a Multi-Level Array

Problem Statement:
You are given a 0-indexed array `nums` consisting of `n` integers. You are also given a 0-indexed array `queries` where `queries[i] = [type, x, y]`.

There are three types of queries:
1. If `type == 1`, flip the values of `nums[x]` to `nums[y]` (inclusive). Flipping means changing `0` to `1` and `1` to `0`.
2. If `type == 2`, calculate the sum of the values in `nums[x]` to `nums[y]` (inclusive) and return it.
3. If `type == 3`, return the current state of the array `nums`.

Implement a function `handleQueries(nums: List[int], queries: List[List[int]]) -> List[int]` that processes the queries and returns a list of results for queries of type `2` and `3`.

Constraints:
- `1 <= nums.length <= 10^5`
- `1 <= queries.length <= 10^5`
- `queries[i].length == 3`
- `0 <= x <= y < nums.length`
- `type` is one of {1, 2, 3}.
"""

from typing import List

def handleQueries(nums: List[int], queries: List[List[int]]) -> List[int]:
    results = []
    for query in queries:
        query_type, x, y = query
        if query_type == 1:
            # Flip values in the range [x, y]
            for i in range(x, y + 1):
                nums[i] = 1 - nums[i]
        elif query_type == 2:
            # Calculate the sum in the range [x, y]
            results.append(sum(nums[x:y + 1]))
        elif query_type == 3:
            # Return the current state of the array
            results.append(nums[:])
    return results

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums = [0, 1, 0, 1, 0]
    queries = [
        [1, 1, 3],  # Flip nums[1] to nums[3]
        [2, 0, 4],  # Sum nums[0] to nums[4]
        [3, 0, 4],  # Return the current state of nums
    ]
    print(handleQueries(nums, queries))  # Expected Output: [3, [0, 0, 1, 0, 0]]

    # Test Case 2
    nums = [1, 0, 1, 0, 1]
    queries = [
        [2, 0, 2],  # Sum nums[0] to nums[2]
        [1, 2, 4],  # Flip nums[2] to nums[4]
        [3, 0, 4],  # Return the current state of nums
    ]
    print(handleQueries(nums, queries))  # Expected Output: [2, [1, 0, 0, 1, 0]]

    # Test Case 3
    nums = [1, 1, 1, 1, 1]
    queries = [
        [1, 0, 4],  # Flip nums[0] to nums[4]
        [2, 0, 4],  # Sum nums[0] to nums[4]
        [3, 0, 4],  # Return the current state of nums
    ]
    print(handleQueries(nums, queries))  # Expected Output: [0, [0, 0, 0, 0, 0]]

# Time and Space Complexity Analysis
"""
Time Complexity:
- For each query:
  - Type 1 (flip): O(y - x + 1), where y - x + 1 is the range of indices to flip.
  - Type 2 (sum): O(y - x + 1), where y - x + 1 is the range of indices to sum.
  - Type 3 (return array): O(n), where n is the length of nums.
- In the worst case, all queries are of type 1 or type 2, and the range spans the entire array. Thus, the total time complexity is O(n * q), where q is the number of queries.

Space Complexity:
- The space complexity is O(n + q), where n is the size of nums and q is the number of queries. This accounts for the storage of the nums array and the results list.

Topic: Arrays
"""