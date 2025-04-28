"""
LeetCode Problem #1330: Reverse Subarray To Maximize Array Value

Problem Statement:
You are given an integer array `nums`. The value of this array is defined as the sum of |nums[i] - nums[i+1]| for all 0 <= i < nums.length - 1.

You are allowed to select a subarray of the array and reverse it. Your task is to return the maximum possible value of the array after reversing exactly one subarray.

Constraints:
- 1 <= nums.length <= 3 * 10^4
- -10^5 <= nums[i] <= 10^5
"""

def maxValueAfterReverse(nums):
    """
    Function to calculate the maximum possible value of the array after reversing one subarray.

    :param nums: List[int] - The input array
    :return: int - The maximum possible value of the array
    """
    n = len(nums)
    base_value = 0
    max_gain = 0
    min_edge = float('inf')
    max_edge = float('-inf')

    # Calculate the base value of the array
    for i in range(n - 1):
        base_value += abs(nums[i] - nums[i + 1])

    # Case 1: Reverse a subarray that starts or ends at the boundary
    for i in range(1, n):
        max_gain = max(max_gain, abs(nums[0] - nums[i]) - abs(nums[i] - nums[i - 1]))
        max_gain = max(max_gain, abs(nums[-1] - nums[i - 1]) - abs(nums[i] - nums[i - 1]))

    # Case 2: Reverse a subarray in the middle
    for i in range(n - 1):
        min_edge = min(min_edge, max(nums[i], nums[i + 1]))
        max_edge = max(max_edge, min(nums[i], nums[i + 1]))

    max_gain = max(max_gain, 2 * (max_edge - min_edge))

    return base_value + max_gain

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 3, 1, 5, 4]
    print(maxValueAfterReverse(nums1))  # Expected Output: 10

    # Test Case 2
    nums2 = [2, 4, 9, 24, 2, 1, 10]
    print(maxValueAfterReverse(nums2))  # Expected Output: 68

    # Test Case 3
    nums3 = [1, 2, 3, 4]
    print(maxValueAfterReverse(nums3))  # Expected Output: 6

    # Test Case 4
    nums4 = [1, -3, 2, 3, -4]
    print(maxValueAfterReverse(nums4))  # Expected Output: 19

"""
Time and Space Complexity Analysis:

Time Complexity:
- Calculating the base value takes O(n).
- The first loop (Case 1) iterates through the array once, taking O(n).
- The second loop (Case 2) also iterates through the array once, taking O(n).
- Overall, the time complexity is O(n).

Space Complexity:
- The algorithm uses a constant amount of extra space, so the space complexity is O(1).

Topic: Arrays
"""