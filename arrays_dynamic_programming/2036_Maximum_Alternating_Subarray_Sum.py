"""
LeetCode Problem #2036: Maximum Alternating Subarray Sum

Problem Statement:
You are given an integer array `nums`. The alternating subarray sum of a subarray is defined as:
    nums[i] - nums[i+1] + nums[i+2] - nums[i+3] + ... (alternating between addition and subtraction).

Return the maximum alternating subarray sum of any subarray of `nums`.

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
"""

def maximumAlternatingSubarraySum(nums):
    """
    Function to calculate the maximum alternating subarray sum.

    Args:
    nums (List[int]): The input array of integers.

    Returns:
    int: The maximum alternating subarray sum.
    """
    n = len(nums)
    max_odd = max_even = float('-inf')
    curr_odd = curr_even = 0

    for i in range(n):
        if i % 2 == 0:  # Even index
            curr_even = max(nums[i], curr_even + nums[i])
            curr_odd = curr_odd - nums[i] if curr_odd != 0 else float('-inf')
        else:  # Odd index
            curr_odd = max(nums[i], curr_even - nums[i])
            curr_even = curr_even + nums[i] if curr_even != 0 else float('-inf')

        max_odd = max(max_odd, curr_odd)
        max_even = max(max_even, curr_even)

    return max(max_odd, max_even)


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [3, -1, 1, 2]
    print("Test Case 1:", maximumAlternatingSubarraySum(nums1))  # Expected Output: 5

    # Test Case 2
    nums2 = [2, 3, -2, 4]
    print("Test Case 2:", maximumAlternatingSubarraySum(nums2))  # Expected Output: 5

    # Test Case 3
    nums3 = [-1, -2, -3, -4]
    print("Test Case 3:", maximumAlternatingSubarraySum(nums3))  # Expected Output: -1

    # Test Case 4
    nums4 = [1]
    print("Test Case 4:", maximumAlternatingSubarraySum(nums4))  # Expected Output: 1

    # Test Case 5
    nums5 = [1, 2, 3, 4, 5]
    print("Test Case 5:", maximumAlternatingSubarraySum(nums5))  # Expected Output: 5


"""
Time Complexity Analysis:
- The algorithm iterates through the array once, performing constant-time operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the input array.

Space Complexity Analysis:
- The algorithm uses a constant amount of extra space for variables like `curr_odd`, `curr_even`, `max_odd`, and `max_even`.
- Therefore, the space complexity is O(1).

Topic: Arrays, Dynamic Programming
"""