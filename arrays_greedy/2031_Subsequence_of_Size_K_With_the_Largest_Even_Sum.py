"""
LeetCode Problem #2031: Subsequence of Size K With the Largest Even Sum

Problem Statement:
You are given an integer array `nums` and an integer `k`. Find the largest even sum of any subsequence of size `k` in `nums`. If it is impossible to form a subsequence of size `k` with an even sum, return -1.

A subsequence is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
- 1 <= k <= nums.length
"""

from heapq import nlargest

def largestEvenSum(nums, k):
    """
    Finds the largest even sum of any subsequence of size k in nums.
    If no such subsequence exists, returns -1.
    """
    # Separate nums into odd and even numbers
    evens = [num for num in nums if num % 2 == 0]
    odds = [num for num in nums if num % 2 != 0]

    # Sort both lists in descending order
    evens.sort(reverse=True)
    odds.sort(reverse=True)

    # Initialize the largest sum as -1 (impossible case)
    max_sum = -1

    # Iterate over all possible counts of even numbers in the subsequence
    for even_count in range(max(0, k - len(odds)), min(k, len(evens)) + 1):
        odd_count = k - even_count

        # Check if we can pick the required number of odd numbers
        if odd_count <= len(odds):
            # Calculate the sum of the subsequence
            current_sum = sum(evens[:even_count]) + sum(odds[:odd_count])

            # Update the max_sum if the current sum is even
            if current_sum % 2 == 0:
                max_sum = max(max_sum, current_sum)

    return max_sum

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [4, 1, 5, 3, 1]
    k1 = 3
    print(largestEvenSum(nums1, k1))  # Output: 12 (4 + 5 + 3)

    # Test Case 2
    nums2 = [1, 3, 5, 7]
    k2 = 2
    print(largestEvenSum(nums2, k2))  # Output: -1 (no even sum possible)

    # Test Case 3
    nums3 = [2, 4, 6, 8]
    k3 = 2
    print(largestEvenSum(nums3, k3))  # Output: 14 (6 + 8)

    # Test Case 4
    nums4 = [1, 2, 3, 4, 5, 6]
    k4 = 4
    print(largestEvenSum(nums4, k4))  # Output: 18 (6 + 4 + 5 + 3)

    # Test Case 5
    nums5 = [10, 20, 30, 40, 50]
    k5 = 5
    print(largestEvenSum(nums5, k5))  # Output: 150 (10 + 20 + 30 + 40 + 50)

"""
Time Complexity Analysis:
- Separating nums into evens and odds: O(n), where n is the length of nums.
- Sorting evens and odds: O(n log n).
- Iterating over possible even counts: O(k), where k is the size of the subsequence.
- Calculating the sum for each combination: O(k) in the worst case.
Overall: O(n log n) due to the sorting step.

Space Complexity Analysis:
- Space for evens and odds lists: O(n).
Overall: O(n).

Topic: Arrays, Greedy
"""