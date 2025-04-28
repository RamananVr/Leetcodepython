"""
LeetCode Problem #2035: Partition Array Into Two Arrays to Minimize Sum Difference

Problem Statement:
You are given an integer array `nums` of length `2 * n`. You need to partition the array into two arrays of length `n` to minimize the absolute difference of their sums.

Formally, if the two arrays are `nums1` and `nums2`, where:
- `nums1` is a subset of `nums` with length `n`.
- `nums2` is the complement of `nums1` (i.e., every element of `nums` that is not in `nums1`).

Return the minimum possible value of `|sum(nums1) - sum(nums2)|`.

Constraints:
- `1 <= n <= 15`
- `nums.length == 2 * n`
- `-10^7 <= nums[i] <= 10^7`
"""

from itertools import combinations

def minimumDifference(nums):
    """
    Function to minimize the absolute difference between the sums of two partitions of the array.

    Args:
    nums (List[int]): The input array of integers.

    Returns:
    int: The minimum possible absolute difference between the sums of the two partitions.
    """
    n = len(nums) // 2
    total_sum = sum(nums)
    target = total_sum // 2

    # Helper function to generate all possible sums of subsets of size k
    def generate_subset_sums(arr):
        subset_sums = {}
        for k in range(len(arr) + 1):
            subset_sums[k] = [sum(comb) for comb in combinations(arr, k)]
        return subset_sums

    # Split the array into two halves
    left, right = nums[:n], nums[n:]

    # Generate all subset sums for both halves
    left_sums = generate_subset_sums(left)
    right_sums = generate_subset_sums(right)

    # Initialize the minimum difference
    min_diff = float('inf')

    # Iterate over all possible subset sizes
    for k in range(n + 1):
        left_k_sums = left_sums[k]
        right_k_sums = sorted(right_sums[n - k])  # Sort for binary search

        # For each sum in left_k_sums, find the closest sum in right_k_sums
        for left_sum in left_k_sums:
            remaining = target - left_sum

            # Binary search to find the closest sum in right_k_sums
            low, high = 0, len(right_k_sums) - 1
            while low <= high:
                mid = (low + high) // 2
                if right_k_sums[mid] < remaining:
                    low = mid + 1
                else:
                    high = mid - 1

            # Check the closest sums
            for idx in [high, low]:
                if 0 <= idx < len(right_k_sums):
                    right_sum = right_k_sums[idx]
                    sum1 = left_sum + right_sum
                    sum2 = total_sum - sum1
                    min_diff = min(min_diff, abs(sum1 - sum2))

    return min_diff

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [3, 9, 7, 3]
    print(minimumDifference(nums1))  # Output: 2

    # Test Case 2
    nums2 = [-36, 36]
    print(minimumDifference(nums2))  # Output: 72

    # Test Case 3
    nums3 = [1, 2, 3, 4, 5, 6]
    print(minimumDifference(nums3))  # Output: 1

    # Test Case 4
    nums4 = [1, 2]
    print(minimumDifference(nums4))  # Output: 1

"""
Time and Space Complexity Analysis:

Time Complexity:
- Generating all subset sums for each half takes O(2^(n/2) * n), where n is the size of one half of the array.
- Sorting the subset sums for the right half takes O(2^(n/2) * log(2^(n/2))) = O(2^(n/2) * (n/2)).
- For each subset sum in the left half, performing a binary search on the right half takes O(log(2^(n/2))) = O(n/2).
- Overall, the time complexity is O(2^(n/2) * n + 2^(n/2) * (n/2) + 2^(n/2) * n) = O(2^(n/2) * n).

Space Complexity:
- Storing all subset sums for both halves takes O(2^(n/2) + 2^(n/2)) = O(2^(n/2)).

Primary Topic: Backtracking / Combinatorics
"""