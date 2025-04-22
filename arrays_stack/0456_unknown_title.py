"""
LeetCode Problem #456: 132 Pattern

Problem Statement:
Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j], nums[k] such that 
i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise return false.

Example 1:
Input: nums = [1, 2, 3, 4]
Output: false
Explanation: There is no 132 pattern in the sequence.

Example 2:
Input: nums = [3, 1, 4, 2]
Output: true
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].

Example 3:
Input: nums = [-1, 3, 2, 0]
Output: true
Explanation: There are multiple 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0], and [-1, 2, 0].

Constraints:
- n == nums.length
- 1 <= n <= 2 * 10^4
- -10^9 <= nums[i] <= 10^9
"""

# Python Solution
def find132pattern(nums):
    """
    Function to determine if there exists a 132 pattern in the given array.

    :param nums: List[int] - Input array of integers
    :return: bool - True if a 132 pattern exists, False otherwise
    """
    n = len(nums)
    if n < 3:
        return False

    # Initialize a stack and a variable to track the second element in the 132 pattern
    stack = []
    second = float('-inf')  # This will represent nums[k] in the 132 pattern

    # Traverse the array from right to left
    for i in range(n - 1, -1, -1):
        # Check if we found a valid 132 pattern
        if nums[i] < second:
            return True

        # Update the stack and second element
        while stack and nums[i] > stack[-1]:
            second = stack.pop()

        stack.append(nums[i])

    return False

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3, 4]
    print(find132pattern(nums1))  # Output: False

    # Test Case 2
    nums2 = [3, 1, 4, 2]
    print(find132pattern(nums2))  # Output: True

    # Test Case 3
    nums3 = [-1, 3, 2, 0]
    print(find132pattern(nums3))  # Output: True

    # Test Case 4
    nums4 = [6, 12, 3, 4, 6, 11, 20]
    print(find132pattern(nums4))  # Output: True

    # Test Case 5
    nums5 = [1, 0, 1, -4, -3]
    print(find132pattern(nums5))  # Output: False

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm traverses the array once from right to left, which is O(n).
- The stack operations (push and pop) are O(1) each, and in the worst case, every element is pushed and popped once.
- Therefore, the overall time complexity is O(n).

Space Complexity:
- The space complexity is O(n) due to the stack used to store elements.
- The additional variables (e.g., `second`) use constant space, so the total space complexity is O(n).

Topic: Arrays, Stack
"""