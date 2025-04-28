"""
LeetCode Problem #2439: Minimize Maximum of Array

Problem Statement:
You are given a 0-indexed array nums comprising n non-negative integers.

In one operation, you must:
- Choose an integer i such that 1 <= i < n and nums[i] > 0.
- Decrease nums[i] by 1.
- Increase nums[i - 1] by 1.

Return the minimum possible value of the maximum integer of nums after performing any number of operations.

Example 1:
Input: nums = [3, 7, 1, 6]
Output: 5
Explanation:
One set of optimal operations is as follows:
1. Choose i = 1, and nums becomes [4, 6, 1, 6].
2. Choose i = 3, and nums becomes [4, 6, 2, 5].
3. Choose i = 1, and nums becomes [5, 5, 2, 5].
The maximum integer of nums is 5. It can be shown that the maximum possible value is 5.

Example 2:
Input: nums = [10, 1]
Output: 10
Explanation:
It is optimal to leave nums as is, and the maximum value is 10.

Constraints:
- n == nums.length
- 2 <= n <= 10^5
- 0 <= nums[i] <= 10^9
"""

def minimizeArrayValue(nums):
    """
    Function to minimize the maximum value of the array after performing the operations.

    Args:
    nums (List[int]): The input array of non-negative integers.

    Returns:
    int: The minimum possible value of the maximum integer in the array.
    """
    prefix_sum = 0
    max_value = 0

    for i, num in enumerate(nums):
        prefix_sum += num
        max_value = max(max_value, (prefix_sum + i) // (i + 1))  # Ceiling of prefix_sum / (i + 1)

    return max_value

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [3, 7, 1, 6]
    print(minimizeArrayValue(nums1))  # Output: 5

    # Test Case 2
    nums2 = [10, 1]
    print(minimizeArrayValue(nums2))  # Output: 10

    # Test Case 3
    nums3 = [1, 2, 3, 4, 5]
    print(minimizeArrayValue(nums3))  # Output: 3

    # Test Case 4
    nums4 = [0, 0, 0, 0]
    print(minimizeArrayValue(nums4))  # Output: 0

    # Test Case 5
    nums5 = [1000000000, 1, 1, 1]
    print(minimizeArrayValue(nums5))  # Output: 250000000

"""
Time Complexity Analysis:
- The function iterates through the array once, performing O(1) operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the array.

Space Complexity Analysis:
- The function uses a constant amount of extra space for variables like `prefix_sum` and `max_value`.
- Therefore, the space complexity is O(1).

Topic: Arrays
"""