"""
LeetCode Problem #2460: Apply Operations to an Array

Problem Statement:
You are given a 0-indexed array `nums` of size `n` consisting of non-negative integers.

You need to apply the following operations to `nums`:

1. For every index `i` in the array where `nums[i] == nums[i + 1]` (0 <= i < n - 1), set `nums[i] = 2 * nums[i]` and `nums[i + 1] = 0`.
2. After performing all the operations, shift all the `0`s to the end of the array.

Return the resulting array.

Example:
Input: nums = [1,2,2,1,1,0]
Output: [1,4,2,0,0,0]

Constraints:
- 2 <= nums.length <= 2000
- 0 <= nums[i] <= 1000
"""

# Python Solution
def apply_operations(nums):
    """
    Apply operations to the array as described in the problem statement.

    Args:
    nums (List[int]): The input array of non-negative integers.

    Returns:
    List[int]: The resulting array after applying the operations.
    """
    n = len(nums)
    
    # Step 1: Apply the doubling and zeroing operation
    for i in range(n - 1):
        if nums[i] == nums[i + 1]:
            nums[i] *= 2
            nums[i + 1] = 0
    
    # Step 2: Shift all zeros to the end
    result = [num for num in nums if num != 0]  # Collect non-zero elements
    result.extend([0] * (n - len(result)))      # Append zeros to the end
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 2, 1, 1, 0]
    print(apply_operations(nums1))  # Output: [1, 4, 2, 0, 0, 0]

    # Test Case 2
    nums2 = [0, 0, 0, 0]
    print(apply_operations(nums2))  # Output: [0, 0, 0, 0]

    # Test Case 3
    nums3 = [2, 2, 2, 2]
    print(apply_operations(nums3))  # Output: [4, 4, 0, 0]

    # Test Case 4
    nums4 = [1, 1, 1, 1, 1]
    print(apply_operations(nums4))  # Output: [2, 2, 1, 0, 0]

    # Test Case 5
    nums5 = [5, 5, 10, 10, 0, 0]
    print(apply_operations(nums5))  # Output: [10, 20, 0, 0, 0, 0]

# Time and Space Complexity Analysis
"""
Time Complexity:
- The first loop iterates through the array once, performing constant-time operations for each pair of elements. This takes O(n) time.
- The second step involves filtering out zeros and appending zeros to the result, which also takes O(n) time.
- Overall, the time complexity is O(n).

Space Complexity:
- The space complexity is O(n) due to the creation of the `result` list, which stores the non-zero elements and appended zeros.
- No additional data structures are used beyond the input and output arrays.
"""

# Topic: Arrays