"""
LeetCode Problem #2219: Maximum Sum Score of Array

Problem Statement:
You are given a 0-indexed integer array `nums` of length `n`.

The sum score of `nums` at an index `i` is the maximum of:
    - The sum of the first `i + 1` elements, i.e., `nums[0] + nums[1] + ... + nums[i]`
    - The sum of the last `n - i` elements, i.e., `nums[i] + nums[i + 1] + ... + nums[n - 1]`

Return the maximum sum score of `nums` at any index.

Example:
Input: nums = [4, 3, -2, 5]
Output: 10
Explanation:
- For index 0, the sum score is max(4, 10) = 10.
- For index 1, the sum score is max(7, 6) = 7.
- For index 2, the sum score is max(5, 3) = 5.
- For index 3, the sum score is max(10, 5) = 10.
The maximum sum score is 10.

Constraints:
- `n == nums.length`
- `1 <= n <= 10^5`
- `-10^6 <= nums[i] <= 10^6`
"""

def maximumSumScore(nums):
    """
    Function to calculate the maximum sum score of the array at any index.

    Args:
    nums (List[int]): The input array.

    Returns:
    int: The maximum sum score.
    """
    n = len(nums)
    total_sum = sum(nums)
    prefix_sum = 0
    max_score = float('-inf')

    for i in range(n):
        prefix_sum += nums[i]
        suffix_sum = total_sum - prefix_sum + nums[i]
        max_score = max(max_score, max(prefix_sum, suffix_sum))

    return max_score

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [4, 3, -2, 5]
    print(maximumSumScore(nums1))  # Output: 10

    # Test Case 2
    nums2 = [-1, -2, -3, -4]
    print(maximumSumScore(nums2))  # Output: -1

    # Test Case 3
    nums3 = [1, 2, 3, 4, 5]
    print(maximumSumScore(nums3))  # Output: 15

    # Test Case 4
    nums4 = [10]
    print(maximumSumScore(nums4))  # Output: 10

    # Test Case 5
    nums5 = [1, -1, 1, -1, 1]
    print(maximumSumScore(nums5))  # Output: 1

"""
Time Complexity Analysis:
- Calculating the total sum of the array takes O(n).
- Iterating through the array to calculate prefix and suffix sums takes O(n).
- Overall time complexity: O(n).

Space Complexity Analysis:
- We use a constant amount of extra space for variables like `total_sum`, `prefix_sum`, and `max_score`.
- Overall space complexity: O(1).

Topic: Arrays
"""