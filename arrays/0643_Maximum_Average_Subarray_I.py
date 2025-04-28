"""
LeetCode Problem #643: Maximum Average Subarray I

Problem Statement:
You are given an integer array `nums` consisting of `n` elements, and an integer `k`.
Find the maximum average value of a subarray of length `k`. You need to output the maximum average value as a float.

Constraints:
- 1 <= k <= n <= 30,000
- -10,000 <= nums[i] <= 10,000

Example:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12 + -5 + -6 + 50) / 4 = 51 / 4 = 12.75.

Follow-up:
Can you solve the problem in O(n) time complexity?
"""

# Solution
def findMaxAverage(nums, k):
    """
    Finds the maximum average of a subarray of length k.

    :param nums: List[int] - The input array of integers.
    :param k: int - The length of the subarray.
    :return: float - The maximum average value.
    """
    # Initialize the sum of the first window
    current_sum = sum(nums[:k])
    max_sum = current_sum

    # Slide the window across the array
    for i in range(k, len(nums)):
        current_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, current_sum)

    # Return the maximum average
    return max_sum / k

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 12, -5, -6, 50, 3]
    k1 = 4
    print(findMaxAverage(nums1, k1))  # Expected Output: 12.75

    # Test Case 2
    nums2 = [5, 5, 5, 5, 5]
    k2 = 2
    print(findMaxAverage(nums2, k2))  # Expected Output: 5.0

    # Test Case 3
    nums3 = [-1, -12, -5, -6, -50, -3]
    k3 = 3
    print(findMaxAverage(nums3, k3))  # Expected Output: -4.666666666666667

    # Test Case 4
    nums4 = [10, 20, 30, 40, 50]
    k4 = 5
    print(findMaxAverage(nums4, k4))  # Expected Output: 30.0

    # Test Case 5
    nums5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    k5 = 3
    print(findMaxAverage(nums5, k5))  # Expected Output: 8.0

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm uses a sliding window approach, where we iterate through the array once.
- Calculating the sum of the first window takes O(k), and sliding the window across the array takes O(n - k).
- Overall, the time complexity is O(n).

Space Complexity:
- The algorithm uses a constant amount of extra space for variables like `current_sum` and `max_sum`.
- Therefore, the space complexity is O(1).
"""

# Topic: Arrays