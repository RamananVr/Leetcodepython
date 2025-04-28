"""
LeetCode Problem #2200: Find All K-Distant Indices in an Array

Problem Statement:
You are given a 0-indexed integer array `nums` and two integers `key` and `k`. 
A k-distant index is an index `i` of `nums` for which there exists at least one index `j` such that:
    - `j` is in the range `[0, nums.length - 1]`,
    - `nums[j] == key`, and
    - `abs(i - j) <= k`.

Return a list of all k-distant indices sorted in increasing order.

Example:
Input: nums = [3,4,9,1,3,9,5], key = 9, k = 1
Output: [1,2,3,4,5,6]

Constraints:
- 1 <= nums.length <= 1000
- 1 <= nums[i] <= 1000
- key is an integer from the array `nums`.
- 1 <= k <= nums.length
"""

# Python Solution
def findKDistantIndices(nums, key, k):
    """
    Finds all k-distant indices in the array `nums` based on the given `key` and `k`.

    Args:
    nums (List[int]): The input array of integers.
    key (int): The key value to find k-distant indices for.
    k (int): The maximum distance for an index to be considered k-distant.

    Returns:
    List[int]: A sorted list of all k-distant indices.
    """
    n = len(nums)
    result = set()

    # Find all indices where nums[j] == key
    key_indices = [j for j in range(n) if nums[j] == key]

    # For each key index, add all indices within distance k
    for j in key_indices:
        for i in range(max(0, j - k), min(n, j + k + 1)):
            result.add(i)

    # Return the sorted list of indices
    return sorted(result)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [3, 4, 9, 1, 3, 9, 5]
    key1 = 9
    k1 = 1
    print(findKDistantIndices(nums1, key1, k1))  # Output: [1, 2, 3, 4, 5, 6]

    # Test Case 2
    nums2 = [2, 2, 2, 2, 2]
    key2 = 2
    k2 = 2
    print(findKDistantIndices(nums2, key2, k2))  # Output: [0, 1, 2, 3, 4]

    # Test Case 3
    nums3 = [1, 5, 9, 3, 5, 7, 5]
    key3 = 5
    k3 = 2
    print(findKDistantIndices(nums3, key3, k3))  # Output: [0, 1, 2, 3, 4, 5, 6]

    # Test Case 4
    nums4 = [1, 2, 3, 4, 5]
    key4 = 3
    k4 = 0
    print(findKDistantIndices(nums4, key4, k4))  # Output: [2]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Finding all key indices takes O(n), where n is the length of `nums`.
- For each key index, we iterate over a range of size at most `2k + 1`. In the worst case, this could be O(n * (2k + 1)).
- However, since `k` is bounded by `n`, the overall complexity is O(n^2) in the worst case.

Space Complexity:
- The `key_indices` list and `result` set both require O(n) space in the worst case.
- Thus, the space complexity is O(n).
"""

# Topic: Arrays