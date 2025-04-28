"""
LeetCode Problem #1413: Minimum Value to Get Positive Step by Step Sum

Problem Statement:
Given an array of integers `nums`, you start with an initial positive value `startValue`.
In each step, you add the current number from the array to your step-by-step sum.
The step-by-step sum is the cumulative sum of the array elements plus the initial value `startValue`.

Return the minimum positive value of `startValue` such that the step-by-step sum is always positive.

Example:
Input: nums = [-3, 2, -3, 4, 2]
Output: 5
Explanation:
If you choose startValue = 4, the step-by-step sum will be:
step-by-step sum = [4 + (-3), 1 + 2, 3 + (-3), 0 + 4, 4 + 2] = [1, 3, 0, 4, 6].
This is not always positive.
If you choose startValue = 5, the step-by-step sum will be:
step-by-step sum = [5 + (-3), 2 + 2, 4 + (-3), 1 + 4, 5 + 2] = [2, 4, 1, 5, 7].
This is always positive.

Constraints:
- 1 <= nums.length <= 100
- -100 <= nums[i] <= 100
"""

# Clean, Correct Python Solution
def minStartValue(nums):
    """
    Finds the minimum positive startValue such that the step-by-step sum is always positive.

    :param nums: List[int] - List of integers
    :return: int - Minimum positive startValue
    """
    step_sum = 0
    min_sum = 0

    for num in nums:
        step_sum += num
        min_sum = min(min_sum, step_sum)

    # To ensure the step-by-step sum is always positive, startValue must be at least 1 - min_sum
    return 1 - min_sum


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [-3, 2, -3, 4, 2]
    print(minStartValue(nums1))  # Output: 5

    # Test Case 2
    nums2 = [1, 2]
    print(minStartValue(nums2))  # Output: 1

    # Test Case 3
    nums3 = [1, -2, -3]
    print(minStartValue(nums3))  # Output: 5

    # Test Case 4
    nums4 = [-1, -2, -3]
    print(minStartValue(nums4))  # Output: 7

    # Test Case 5
    nums5 = [3, -6, 5, -2, 1]
    print(minStartValue(nums5))  # Output: 4


# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates through the array once to calculate the cumulative sum and track the minimum sum.
- This results in a time complexity of O(n), where n is the length of the array.

Space Complexity:
- The algorithm uses a constant amount of extra space to store `step_sum` and `min_sum`.
- This results in a space complexity of O(1).

Overall, the solution is efficient with O(n) time complexity and O(1) space complexity.
"""

# Topic: Arrays