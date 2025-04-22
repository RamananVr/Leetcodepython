"""
LeetCode Problem #503: Next Greater Element II

Problem Statement:
Given a circular integer array `nums` (i.e., the next element of the last element is the first element of the array), 
return the next greater number for every element in `nums`.

The next greater number of a number `x` is the first greater number to its traversal order next in the array, 
which means you should search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

Example 1:
Input: nums = [1,2,1]
Output: [2,-1,2]

Example 2:
Input: nums = [3,8,4,1,2]
Output: [8,-1,8,2,3]

Constraints:
- 1 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
"""

# Solution
def nextGreaterElements(nums):
    """
    Finds the next greater element for each element in a circular array.

    Args:
    nums (List[int]): The input circular array.

    Returns:
    List[int]: A list of integers representing the next greater element for each input element.
    """
    n = len(nums)
    result = [-1] * n
    stack = []  # Monotonic stack to store indices

    # Iterate through the array twice to simulate circular behavior
    for i in range(2 * n):
        while stack and nums[stack[-1]] < nums[i % n]:
            index = stack.pop()
            result[index] = nums[i % n]
        if i < n:
            stack.append(i)

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 1]
    print(nextGreaterElements(nums1))  # Output: [2, -1, 2]

    # Test Case 2
    nums2 = [3, 8, 4, 1, 2]
    print(nextGreaterElements(nums2))  # Output: [8, -1, 8, 2, 3]

    # Test Case 3
    nums3 = [5, 4, 3, 2, 1]
    print(nextGreaterElements(nums3))  # Output: [-1, 5, 5, 5, 5]

    # Test Case 4
    nums4 = [1, 2, 3, 4, 5]
    print(nextGreaterElements(nums4))  # Output: [2, 3, 4, 5, -1]

    # Test Case 5
    nums5 = [1]
    print(nextGreaterElements(nums5))  # Output: [-1]

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates through the array twice, resulting in O(2n) = O(n) time complexity.
- Each element is pushed and popped from the stack at most once, so the stack operations are O(n).
- Overall time complexity: O(n).

Space Complexity:
- The `result` array takes O(n) space.
- The `stack` can hold at most n elements, so it also takes O(n) space.
- Overall space complexity: O(n).
"""

# Topic: Arrays, Monotonic Stack