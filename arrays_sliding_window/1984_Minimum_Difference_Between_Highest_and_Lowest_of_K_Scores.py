"""
LeetCode Problem #1984: Minimum Difference Between Highest and Lowest of K Scores

Problem Statement:
You are given a 0-indexed integer array `nums`, where `nums[i]` represents the score of the ith student. 
You are also given an integer `k`.

Pick the scores of any `k` students from the array so that the difference between the highest and lowest 
of the `k` scores is minimized.

Return the minimum possible difference.

Example:
Input: nums = [90], k = 1
Output: 0
Explanation: There is only one score, so the difference is 0.

Input: nums = [9, 4, 1, 7], k = 2
Output: 2
Explanation: The chosen scores are [9, 7]. The difference between the highest and lowest is 2.

Constraints:
- 1 <= k <= nums.length <= 1000
- 0 <= nums[i] <= 10^5
"""

# Solution
def minimumDifference(nums: list[int], k: int) -> int:
    """
    Finds the minimum difference between the highest and lowest scores of k students.

    :param nums: List of integers representing scores.
    :param k: Number of students to pick.
    :return: Minimum possible difference between the highest and lowest scores.
    """
    if k == 1:
        return 0  # If k is 1, the difference is always 0.

    # Sort the array to make it easier to find the minimum difference.
    nums.sort()

    # Initialize the minimum difference to a large value.
    min_diff = float('inf')

    # Iterate through the sorted array to find the minimum difference between k consecutive elements.
    for i in range(len(nums) - k + 1):
        diff = nums[i + k - 1] - nums[i]
        min_diff = min(min_diff, diff)

    return min_diff


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [90]
    k1 = 1
    print(minimumDifference(nums1, k1))  # Output: 0

    # Test Case 2
    nums2 = [9, 4, 1, 7]
    k2 = 2
    print(minimumDifference(nums2, k2))  # Output: 2

    # Test Case 3
    nums3 = [1, 3, 6, 10, 15]
    k3 = 3
    print(minimumDifference(nums3, k3))  # Output: 5

    # Test Case 4
    nums4 = [100, 200, 300, 400]
    k4 = 2
    print(minimumDifference(nums4, k4))  # Output: 100

    # Test Case 5
    nums5 = [1, 1, 1, 1]
    k5 = 4
    print(minimumDifference(nums5, k5))  # Output: 0


# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting the array takes O(n log n), where n is the length of nums.
- The sliding window iteration takes O(n - k), which is O(n) in the worst case.
- Overall time complexity: O(n log n).

Space Complexity:
- The sorting operation is in-place, so it uses O(1) additional space.
- Overall space complexity: O(1).
"""

# Topic: Arrays, Sliding Window