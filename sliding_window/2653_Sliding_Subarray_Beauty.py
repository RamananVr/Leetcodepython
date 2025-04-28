"""
LeetCode Problem #2653: Sliding Subarray Beauty

Problem Statement:
You are given an integer array `nums` containing `n` integers, and two integers `k` and `x`.
A subarray is called beautiful if the number of negative integers in the subarray is at least `x`.
Return an array `result` of size `n - k + 1` where `result[i]` is the smallest integer in the 
beautiful subarray starting at index `i` (0-indexed). If the subarray is not beautiful, 
set `result[i]` to 0.

A subarray is a contiguous non-empty sequence of elements within an array.

Constraints:
- `1 <= n <= 10^5`
- `1 <= k <= n`
- `1 <= x <= k`
- `-10^4 <= nums[i] <= 10^4`
"""

# Solution
from collections import deque

def getSubarrayBeauty(nums, k, x):
    """
    Function to calculate the smallest integer in beautiful subarrays of size k.
    
    Args:
    nums (List[int]): The input array of integers.
    k (int): The size of the subarray.
    x (int): Minimum number of negative integers required for a subarray to be beautiful.
    
    Returns:
    List[int]: An array containing the smallest integer in each beautiful subarray or 0 if not beautiful.
    """
    result = []
    negative_count = deque()  # To store indices of negative numbers in the current window
    for i in range(len(nums)):
        # Add current number to the window
        if nums[i] < 0:
            negative_count.append(i)
        
        # Remove elements that are out of the current window
        if i >= k and negative_count and negative_count[0] < i - k + 1:
            negative_count.popleft()
        
        # Check if the current window is valid
        if i >= k - 1:
            if len(negative_count) >= x:
                # Find the smallest number in the current window
                result.append(min(nums[i - k + 1:i + 1]))
            else:
                result.append(0)
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums = [-1, -2, -3, -4, -5]
    k = 3
    x = 2
    print(getSubarrayBeauty(nums, k, x))  # Expected Output: [-3, -4, -5]

    # Test Case 2
    nums = [1, -1, -2, 3, -4]
    k = 2
    x = 1
    print(getSubarrayBeauty(nums, k, x))  # Expected Output: [-1, -2, 0, -4]

    # Test Case 3
    nums = [1, 2, 3, 4, 5]
    k = 3
    x = 1
    print(getSubarrayBeauty(nums, k, x))  # Expected Output: [0, 0, 0]

    # Test Case 4
    nums = [-5, -6, -7, 8, 9]
    k = 4
    x = 3
    print(getSubarrayBeauty(nums, k, x))  # Expected Output: [-7, 0]

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates through the array once, performing constant-time operations for each element.
- The deque operations (append, popleft) are O(1).
- Finding the minimum in a subarray of size k is O(k) for each valid window.
- Overall complexity: O(n * k), where n is the size of the array.

Space Complexity:
- The space used by the deque is proportional to the number of negative numbers in the current window, which is O(k) in the worst case.
- Overall space complexity: O(k).
"""

# Topic: Sliding Window