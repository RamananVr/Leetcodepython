"""
LeetCode Problem #2597: The Number of Beautiful Subsets

Problem Statement:
You are given an integer array `nums` and a positive integer `k`.

A subset of the array `nums` is called beautiful if it satisfies both of the following conditions:
1. The subset is non-empty.
2. For every pair of integers `a` and `b` in the subset, `|a - b| != k`.

Return the number of beautiful subsets of the array `nums`.

A subset of `nums` is an array that can be obtained by deleting some (possibly none) elements from `nums`. Two subsets are different if and only if the chosen indices to delete are different.

Constraints:
- 1 <= nums.length <= 20
- 1 <= nums[i], k <= 1000
"""

# Solution
from collections import Counter

def beautifulSubsets(nums, k):
    def backtrack(index, freq):
        # Base case: if we've processed all elements
        if index == len(nums):
            return 1  # Count the empty subset

        # Skip the current element
        count = backtrack(index + 1, freq)

        # Include the current element if it doesn't violate the condition
        if freq[nums[index] - k] == 0 and freq[nums[index] + k] == 0:
            freq[nums[index]] += 1
            count += backtrack(index + 1, freq)
            freq[nums[index]] -= 1  # Backtrack

        return count

    # Start the backtracking process
    freq = Counter()
    return backtrack(0, freq) - 1  # Subtract 1 to exclude the empty subset

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 4, 6]
    k1 = 2
    print("Test Case 1 Output:", beautifulSubsets(nums1, k1))  # Expected Output: 4

    # Test Case 2
    nums2 = [1]
    k2 = 1
    print("Test Case 2 Output:", beautifulSubsets(nums2, k2))  # Expected Output: 1

    # Test Case 3
    nums3 = [4, 5, 6, 7]
    k3 = 3
    print("Test Case 3 Output:", beautifulSubsets(nums3, k3))  # Expected Output: 8

"""
Time Complexity Analysis:
- The total number of subsets of an array of size `n` is `2^n`.
- For each subset, we perform constant-time checks to ensure the subset is valid.
- Therefore, the time complexity is O(2^n), where `n` is the length of the input array `nums`.

Space Complexity Analysis:
- The space complexity is O(n) due to the recursion stack and the frequency counter.

Topic: Backtracking
"""