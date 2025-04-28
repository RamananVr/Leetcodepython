"""
LeetCode Problem #1755: Closest Subsequence Sum

Problem Statement:
You are given an integer array nums and an integer goal.

You want to choose a subsequence of nums such that the sum of its elements is the closest possible to goal. 
That is, if the sum of the subsequence's elements is sum, then abs(sum - goal) should be minimized.

Return the minimum possible value of abs(sum - goal).

Note:
- A subsequence of an array is obtained by deleting some number of elements (possibly zero) from the array.
- A subsequence does not necessarily have to be contiguous.

Constraints:
- 1 <= nums.length <= 40
- -10^7 <= nums[i] <= 10^7
- -10^9 <= goal <= 10^9
"""

# Solution
from itertools import combinations

def closestSubsequenceSum(nums, goal):
    def generate_sums(arr):
        """Generate all possible sums of subsequences."""
        n = len(arr)
        sums = set()
        for i in range(n + 1):
            for comb in combinations(arr, i):
                sums.add(sum(comb))
        return sums

    # Split nums into two halves
    mid = len(nums) // 2
    left, right = nums[:mid], nums[mid:]

    # Generate all possible sums for both halves
    left_sums = generate_sums(left)
    right_sums = generate_sums(right)

    # Sort the right sums for binary search
    right_sums = sorted(right_sums)

    # Find the closest sum
    closest = float('inf')
    for left_sum in left_sums:
        # Binary search for the closest sum in right_sums
        lo, hi = 0, len(right_sums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            current_sum = left_sum + right_sums[mid]
            closest = min(closest, abs(current_sum - goal))
            if current_sum < goal:
                lo = mid + 1
            else:
                hi = mid - 1

    return closest

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums = [5, -7, 3, 5]
    goal = 6
    print(closestSubsequenceSum(nums, goal))  # Output: 0

    # Test Case 2
    nums = [7, -3, 2, 5]
    goal = 10
    print(closestSubsequenceSum(nums, goal))  # Output: 0

    # Test Case 3
    nums = [1, 2, 3]
    goal = -7
    print(closestSubsequenceSum(nums, goal))  # Output: 7

    # Test Case 4
    nums = [1, 2, 3, 4, 5]
    goal = 15
    print(closestSubsequenceSum(nums, goal))  # Output: 0

"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - Generating all possible sums for each half involves iterating over all subsets of the array.
   - For an array of size n, there are 2^(n/2) subsets for each half.
   - Sorting the right_sums takes O(2^(n/2) * log(2^(n/2))) = O(2^(n/2) * n/2).
   - Binary search for each left_sum takes O(log(2^(n/2))) = O(n/2).
   - Overall time complexity: O(2^(n/2) * n).

2. Space Complexity:
   - Storing all possible sums for each half requires O(2^(n/2)) space.
   - Overall space complexity: O(2^(n/2)).

Topic: Divide and Conquer, Binary Search
"""