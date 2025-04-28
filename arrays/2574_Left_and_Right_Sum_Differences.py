"""
LeetCode Problem #2574: Left and Right Sum Differences

Problem Statement:
Given a 0-indexed integer array `nums`, find a 0-indexed integer array `answer` where:

- `answer[i]` is the absolute difference between the sum of elements to the left of index `i` in the array (`leftSum[i]`) and the sum of elements to the right of index `i` in the array (`rightSum[i]`).

More formally:
- `leftSum[i]` is the sum of elements `nums[0]` through `nums[i-1]`. If there are no elements to the left of `i`, `leftSum[i] = 0`.
- `rightSum[i]` is the sum of elements `nums[i+1]` through `nums[nums.length - 1]`. If there are no elements to the right of `i`, `rightSum[i] = 0`.

Return the array `answer`.

Example 1:
Input: nums = [10, 4, 8, 3]
Output: [15, 1, 11, 22]
Explanation:
- For index 0, leftSum = 0, rightSum = 15, answer[0] = |0 - 15| = 15
- For index 1, leftSum = 10, rightSum = 11, answer[1] = |10 - 11| = 1
- For index 2, leftSum = 14, rightSum = 3, answer[2] = |14 - 3| = 11
- For index 3, leftSum = 22, rightSum = 0, answer[3] = |22 - 0| = 22

Example 2:
Input: nums = [1]
Output: [0]
Explanation:
- For index 0, leftSum = 0, rightSum = 0, answer[0] = |0 - 0| = 0

Constraints:
- 1 <= nums.length <= 1000
- 1 <= nums[i] <= 10^5
"""

def leftRightDifference(nums):
    """
    Calculate the absolute difference between left and right sums for each index in the array.

    :param nums: List[int] - The input array of integers.
    :return: List[int] - The resulting array of absolute differences.
    """
    n = len(nums)
    left_sum = [0] * n
    right_sum = [0] * n
    answer = [0] * n

    # Compute left sums
    for i in range(1, n):
        left_sum[i] = left_sum[i - 1] + nums[i - 1]

    # Compute right sums
    for i in range(n - 2, -1, -1):
        right_sum[i] = right_sum[i + 1] + nums[i + 1]

    # Compute the answer array
    for i in range(n):
        answer[i] = abs(left_sum[i] - right_sum[i])

    return answer

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [10, 4, 8, 3]
    print(leftRightDifference(nums1))  # Output: [15, 1, 11, 22]

    # Test Case 2
    nums2 = [1]
    print(leftRightDifference(nums2))  # Output: [0]

    # Test Case 3
    nums3 = [2, 3, 5, 1, 6]
    print(leftRightDifference(nums3))  # Output: [15, 9, 3, 7, 17]

    # Test Case 4
    nums4 = [5, 5, 5, 5]
    print(leftRightDifference(nums4))  # Output: [15, 5, 5, 15]

"""
Time Complexity:
- Computing the left sums takes O(n) time.
- Computing the right sums takes O(n) time.
- Computing the answer array takes O(n) time.
- Overall time complexity: O(n).

Space Complexity:
- We use three additional arrays (left_sum, right_sum, and answer), each of size n.
- Overall space complexity: O(n).

Topic: Arrays
"""