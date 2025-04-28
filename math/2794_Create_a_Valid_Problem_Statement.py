"""
LeetCode Problem #2794: Create a Valid Problem Statement

Problem Statement:
You are given a problem statement for LeetCode Question #2794. Unfortunately, the exact problem statement is not available in the current context. Please replace this placeholder with the actual problem statement from LeetCode.

For the purpose of this template, we will assume a hypothetical problem statement:
"Given an integer `n`, return the number of ways to write `n` as the sum of two or more consecutive positive integers."

Example:
Input: n = 9
Output: 2
Explanation: 9 can be written as:
- 2 + 3 + 4
- 4 + 5

Input: n = 15
Output: 3
Explanation: 15 can be written as:
- 1 + 2 + 3 + 4 + 5
- 4 + 5 + 6
- 7 + 8

Constraints:
- 1 <= n <= 10^9
"""

def consecutiveNumbersSum(n: int) -> int:
    """
    Function to calculate the number of ways to write `n` as the sum of two or more consecutive positive integers.
    """
    count = 0
    k = 1  # k is the number of terms in the sequence
    while k * (k + 1) // 2 <= n:
        if (n - k * (k + 1) // 2) % k == 0:
            count += 1
        k += 1
    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 9
    print(f"Input: {n}, Output: {consecutiveNumbersSum(n)}")  # Expected Output: 2

    # Test Case 2
    n = 15
    print(f"Input: {n}, Output: {consecutiveNumbersSum(n)}")  # Expected Output: 3

    # Test Case 3
    n = 1
    print(f"Input: {n}, Output: {consecutiveNumbersSum(n)}")  # Expected Output: 1

    # Test Case 4
    n = 100
    print(f"Input: {n}, Output: {consecutiveNumbersSum(n)}")  # Expected Output: 3

    # Test Case 5
    n = 1000
    print(f"Input: {n}, Output: {consecutiveNumbersSum(n)}")  # Expected Output: 6

"""
Time Complexity Analysis:
- The while loop runs as long as k * (k + 1) // 2 <= n. This means k grows approximately as O(sqrt(n)).
- Inside the loop, the operations are constant time (arithmetic and modulo operations).
- Therefore, the overall time complexity is O(sqrt(n)).

Space Complexity Analysis:
- The space complexity is O(1) since we are using a constant amount of extra space.

Topic: Math
"""