"""
LeetCode Problem #2836: Maximize Value of Function in a Range

Problem Statement:
You are given an array `nums` of integers and an integer `k`. Your task is to maximize the value of a function `f(i, j)` defined as:

    f(i, j) = nums[i] + nums[j] + (j - i)

where `0 <= i < j < len(nums)` and `j - i <= k`.

Return the maximum value of the function `f(i, j)`.

Constraints:
- 2 <= len(nums) <= 10^5
- -10^4 <= nums[i] <= 10^4
- 1 <= k < len(nums)
"""

def maximizeFunctionValue(nums, k):
    """
    Function to maximize the value of f(i, j) = nums[i] + nums[j] + (j - i)
    under the constraint that j - i <= k.
    
    Args:
    nums (List[int]): The input array of integers.
    k (int): The maximum allowed difference between indices i and j.
    
    Returns:
    int: The maximum value of the function f(i, j).
    """
    max_value = float('-inf')
    max_prefix = float('-inf')  # To store the maximum value of nums[i] + i seen so far

    for j in range(len(nums)):
        if j > k:
            # Update max_prefix to consider only valid i's where j - i <= k
            max_prefix = max(max_prefix, nums[j - k - 1] + (j - k - 1))
        
        # Calculate f(i, j) using the current max_prefix
        max_value = max(max_value, max_prefix + nums[j] - j)
        
        # Update max_prefix for the current index
        max_prefix = max(max_prefix, nums[j] + j)
    
    return max_value

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 3, -1, 2]
    k1 = 2
    print(maximizeFunctionValue(nums1, k1))  # Expected Output: 7 (f(1, 3) = 3 + 2 + (3 - 1) = 7)

    # Test Case 2
    nums2 = [5, 1, 2, 10, 6]
    k2 = 3
    print(maximizeFunctionValue(nums2, k2))  # Expected Output: 18 (f(0, 3) = 5 + 10 + (3 - 0) = 18)

    # Test Case 3
    nums3 = [-5, -2, 0, 3, 7]
    k3 = 2
    print(maximizeFunctionValue(nums3, k3))  # Expected Output: 10 (f(2, 4) = 0 + 7 + (4 - 2) = 10)

    # Test Case 4
    nums4 = [1, 2]
    k4 = 1
    print(maximizeFunctionValue(nums4, k4))  # Expected Output: 4 (f(0, 1) = 1 + 2 + (1 - 0) = 4)

"""
Time Complexity Analysis:
- The algorithm iterates through the array once, performing constant-time operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the array.

Space Complexity Analysis:
- The algorithm uses a constant amount of extra space for variables like `max_value` and `max_prefix`.
- Therefore, the space complexity is O(1).

Topic: Arrays, Sliding Window
"""