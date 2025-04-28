"""
LeetCode Problem #2480: "Find the Pivot Integer"

Problem Statement:
Given a positive integer `n`, find the pivot integer `x` such that the sum of all integers from `1` to `x` is equal to the sum of all integers from `x` to `n`. If no such integer exists, return -1. The pivot integer is defined as the integer `x` that satisfies:

    sum(1, 2, ..., x) == sum(x, x+1, ..., n)

Constraints:
- 1 <= n <= 1000
"""

def pivotInteger(n: int) -> int:
    """
    Finds the pivot integer x such that the sum of integers from 1 to x equals the sum of integers from x to n.
    If no such integer exists, returns -1.
    """
    # Calculate the total sum of integers from 1 to n
    total_sum = n * (n + 1) // 2
    
    # Iterate through possible pivot values
    for x in range(1, n + 1):
        left_sum = x * (x + 1) // 2  # Sum of integers from 1 to x
        right_sum = total_sum - left_sum + x  # Sum of integers from x to n
        if left_sum == right_sum:
            return x
    
    return -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Pivot exists
    n = 8
    print(pivotInteger(n))  # Expected output: 6

    # Test Case 2: Pivot exists
    n = 1
    print(pivotInteger(n))  # Expected output: 1

    # Test Case 3: No pivot exists
    n = 4
    print(pivotInteger(n))  # Expected output: -1

    # Test Case 4: Larger input
    n = 10
    print(pivotInteger(n))  # Expected output: -1

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function iterates through all integers from 1 to n, performing constant-time calculations for each integer.
- Therefore, the time complexity is O(n).

Space Complexity:
- The function uses a constant amount of extra space for variables like `total_sum`, `left_sum`, and `right_sum`.
- Therefore, the space complexity is O(1).

Topic: Math
"""