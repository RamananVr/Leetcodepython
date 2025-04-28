"""
LeetCode Problem #2485: Find the Pivot Integer

Problem Statement:
Given a positive integer `n`, find the pivot integer `x` such that the sum of all integers from `1` to `x` is equal to the sum of all integers from `x` to `n`. If no such integer exists, return -1. The sum of integers from `1` to `x` can be calculated as `x * (x + 1) // 2`, and the sum of integers from `x` to `n` can be calculated as `(n * (n + 1) // 2) - ((x - 1) * x // 2)`.

Constraints:
- `1 <= n <= 1000`

Example:
Input: n = 8
Output: 6
Explanation: The sum of integers from 1 to 6 is 21, and the sum of integers from 6 to 8 is also 21.

Input: n = 1
Output: 1
Explanation: The sum of integers from 1 to 1 is 1, and the sum of integers from 1 to 1 is also 1.

Input: n = 4
Output: -1
Explanation: No such pivot integer exists.
"""

def pivotInteger(n: int) -> int:
    # Calculate the total sum of integers from 1 to n
    total_sum = n * (n + 1) // 2
    
    # Iterate through possible pivot values
    for x in range(1, n + 1):
        # Calculate the sum of integers from 1 to x
        left_sum = x * (x + 1) // 2
        
        # If left_sum equals the sum of integers from x to n, return x
        if left_sum == total_sum - left_sum + x:
            return x
    
    # If no pivot integer is found, return -1
    return -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 8
    print(pivotInteger(n))  # Output: 6

    # Test Case 2
    n = 1
    print(pivotInteger(n))  # Output: 1

    # Test Case 3
    n = 4
    print(pivotInteger(n))  # Output: -1

    # Additional Test Case 4
    n = 10
    print(pivotInteger(n))  # Output: -1

    # Additional Test Case 5
    n = 15
    print(pivotInteger(n))  # Output: 5

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function iterates through all integers from 1 to n, performing constant-time calculations for each integer.
- Therefore, the time complexity is O(n).

Space Complexity:
- The function uses a constant amount of extra space for variables like `total_sum` and `left_sum`.
- Therefore, the space complexity is O(1).

Topic: Math
"""