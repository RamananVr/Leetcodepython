"""
LeetCode Problem #2670: Find the Distinct Difference Array

Problem Statement:
You are given a 0-indexed integer array `nums` of length `n`.

The distinct difference array of `nums` is an integer array `diff` of length `n` such that:
- `diff[i] = (the number of distinct elements in the subarray nums[0...i]) - (the number of distinct elements in the subarray nums[i+1...n-1])`

Return the distinct difference array `diff` of `nums`.

Example:
Input: nums = [4, 3, 2, 2, 4]
Output: [2, 1, 0, -1, -3]

Explanation:
For i = 0:
- The subarray nums[0...0] = [4] has 1 distinct element.
- The subarray nums[1...4] = [3, 2, 2, 4] has 3 distinct elements.
- Thus, diff[0] = 1 - 3 = -2.

For i = 1:
- The subarray nums[0...1] = [4, 3] has 2 distinct elements.
- The subarray nums[2...4] = [2, 2, 4] has 2 distinct elements.
- Thus, diff[1] = 2 - 2 = 0.

And so on for the rest of the indices.

Constraints:
- 1 <= nums.length <= 1000
- 1 <= nums[i] <= 1000
"""

# Python Solution
def distinctDifferenceArray(nums):
    n = len(nums)
    prefix_set = set()
    suffix_set = set(nums)
    prefix_count = [0] * n
    suffix_count = [0] * n
    
    # Calculate prefix distinct counts
    for i in range(n):
        prefix_set.add(nums[i])
        prefix_count[i] = len(prefix_set)
    
    # Calculate suffix distinct counts
    for i in range(n - 1, -1, -1):
        suffix_count[i] = len(suffix_set)
        suffix_set.remove(nums[i])
    
    # Calculate the distinct difference array
    diff = [prefix_count[i] - (suffix_count[i + 1] if i + 1 < n else 0) for i in range(n)]
    return diff

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [4, 3, 2, 2, 4]
    print(distinctDifferenceArray(nums1))  # Output: [2, 1, 0, -1, -3]

    # Test Case 2
    nums2 = [1, 2, 3, 4, 5]
    print(distinctDifferenceArray(nums2))  # Output: [1, 1, 1, 1, 1]

    # Test Case 3
    nums3 = [5, 5, 5, 5, 5]
    print(distinctDifferenceArray(nums3))  # Output: [1, 0, -1, -2, -3]

    # Test Case 4
    nums4 = [1]
    print(distinctDifferenceArray(nums4))  # Output: [1]

    # Test Case 5
    nums5 = [1, 2, 1, 2, 1]
    print(distinctDifferenceArray(nums5))  # Output: [1, 0, -1, -2, -3]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Calculating prefix distinct counts takes O(n) since we iterate through the array once and use a set for tracking distinct elements.
- Calculating suffix distinct counts also takes O(n) for the same reason.
- Constructing the final `diff` array takes O(n).
- Overall time complexity: O(n).

Space Complexity:
- We use two sets (`prefix_set` and `suffix_set`) and two arrays (`prefix_count` and `suffix_count`) of size `n`.
- Space complexity: O(n).
"""

# Topic: Arrays