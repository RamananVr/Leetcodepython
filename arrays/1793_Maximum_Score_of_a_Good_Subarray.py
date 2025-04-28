"""
LeetCode Problem #1793: Maximum Score of a Good Subarray

Problem Statement:
You are given an array of integers `nums` (0-indexed) and an integer `k`. The score of a subarray (i, j) is defined as:
    - min(nums[i], nums[i+1], ..., nums[j]) * (j - i + 1)
A "good subarray" is a subarray where `k` is within its range [i, j].

Return the maximum possible score of a good subarray.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
- 0 <= k < nums.length
"""

# Solution
def maximumScore(nums, k):
    n = len(nums)
    left = right = k
    min_val = nums[k]
    max_score = 0

    while left >= 0 and right < n:
        # Expand the window to include the larger side
        if left > 0 and (right == n - 1 or nums[left - 1] >= nums[right + 1]):
            left -= 1
        else:
            right += 1

        # Update the minimum value in the current window
        min_val = min(min_val, nums[left], nums[right])

        # Calculate the score for the current window
        max_score = max(max_score, min_val * (right - left + 1))

    return max_score

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 4, 3, 7, 4, 5]
    k1 = 3
    print(maximumScore(nums1, k1))  # Expected Output: 15

    # Test Case 2
    nums2 = [5, 5, 4, 5, 5]
    k2 = 2
    print(maximumScore(nums2, k2))  # Expected Output: 20

    # Test Case 3
    nums3 = [2, 1, 5, 6, 2, 3]
    k3 = 2
    print(maximumScore(nums3, k3))  # Expected Output: 10

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates through the array while expanding the window to the left or right.
- Each expansion step involves updating the minimum value and calculating the score.
- Since the window expands at most `n` times (where `n` is the length of the array), the time complexity is O(n).

Space Complexity:
- The algorithm uses a constant amount of extra space for variables like `left`, `right`, `min_val`, and `max_score`.
- Therefore, the space complexity is O(1).
"""

# Topic: Arrays