"""
LeetCode Problem #1802: Maximum Value at a Given Index in a Bounded Array

Problem Statement:
You are given three positive integers: n, index, and maxSum. You want to construct an array nums (0-indexed) of length n such that:
- nums[i] is a positive integer where 1 <= nums[i].
- The absolute difference between any two adjacent elements of nums is at most 1.
- The sum of all the elements of nums does not exceed maxSum.
- nums[index] is maximized.

Return the maximum possible value of nums[index].

Constraints:
- 1 <= n <= 10^9
- 0 <= index < n
- n <= maxSum <= 10^9
"""

def maxValue(n: int, index: int, maxSum: int) -> int:
    def sum_of_elements(value: int, length: int) -> int:
        """
        Helper function to calculate the sum of elements in a subarray of length `length`
        where the maximum value is `value` and the values decrease by 1 until reaching 1.
        """
        if value >= length:
            # Full decreasing sequence fits within the length
            return (value + (value - length + 1)) * length // 2
        else:
            # Partial decreasing sequence, then fill the rest with 1s
            return (value * (value + 1)) // 2 + (length - value)

    def is_valid(mid: int) -> bool:
        """
        Check if it's possible to construct an array with nums[index] = mid
        while satisfying the constraints.
        """
        left_sum = sum_of_elements(mid - 1, index + 1)  # Left side of the array
        right_sum = sum_of_elements(mid - 1, n - index)  # Right side of the array
        total_sum = left_sum + right_sum - (mid - 1)  # Avoid double-counting mid
        return total_sum <= maxSum

    # Binary search to find the maximum value of nums[index]
    low, high = 1, maxSum
    result = 1
    while low <= high:
        mid = (low + high) // 2
        if is_valid(mid):
            result = mid  # Update result and try for a larger value
            low = mid + 1
        else:
            high = mid - 1
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 4
    index = 2
    maxSum = 6
    print(maxValue(n, index, maxSum))  # Expected Output: 2

    # Test Case 2
    n = 6
    index = 1
    maxSum = 10
    print(maxValue(n, index, maxSum))  # Expected Output: 3

    # Test Case 3
    n = 3
    index = 0
    maxSum = 815
    print(maxValue(n, index, maxSum))  # Expected Output: 407

"""
Time Complexity:
- The binary search runs in O(log(maxSum)).
- The helper function `sum_of_elements` runs in O(1) since it uses arithmetic formulas.
- The `is_valid` function is called in each iteration of the binary search, and it also runs in O(1).
- Therefore, the overall time complexity is O(log(maxSum)).

Space Complexity:
- The space complexity is O(1) since we are using a constant amount of extra space.

Topic: Binary Search
"""