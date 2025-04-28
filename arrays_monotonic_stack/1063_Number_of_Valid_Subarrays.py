"""
LeetCode Problem #1063: Number of Valid Subarrays

Problem Statement:
Given an integer array `nums`, a subarray is called valid if for every pair of indices `(i, j)` in the subarray 
where `i <= j`, `nums[i] <= nums[j]`. Return the number of valid subarrays of `nums`.

Constraints:
- 1 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^9
"""

def validSubarrays(nums):
    """
    Function to calculate the number of valid subarrays in the given array.

    Args:
    nums (List[int]): The input array of integers.

    Returns:
    int: The number of valid subarrays.
    """
    stack = []
    result = 0

    for num in nums:
        # Maintain a monotonic stack where elements are in non-decreasing order
        while stack and stack[-1] > num:
            stack.pop()
        stack.append(num)
        result += len(stack)

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 4, 2, 5, 3]
    print(validSubarrays(nums1))  # Expected Output: 11

    # Test Case 2
    nums2 = [3, 2, 1]
    print(validSubarrays(nums2))  # Expected Output: 3

    # Test Case 3
    nums3 = [2, 2, 2]
    print(validSubarrays(nums3))  # Expected Output: 6

    # Test Case 4
    nums4 = [1]
    print(validSubarrays(nums4))  # Expected Output: 1

"""
Time Complexity Analysis:
- Each element is pushed and popped from the stack at most once.
- Therefore, the time complexity is O(n), where n is the length of the input array.

Space Complexity Analysis:
- The space complexity is O(n) in the worst case, as the stack can hold up to n elements.

Topic: Arrays, Monotonic Stack
"""