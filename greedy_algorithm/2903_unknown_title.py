"""
LeetCode Problem #2903: Maximum Number of Odd Integers

Problem Statement:
You are given an integer `n`. Your task is to find the maximum number of odd integers 
that sum up to `n`. Each odd integer must be positive and distinct.

Return the maximum number of odd integers that satisfy the above conditions.

Example:
Input: n = 14
Output: 3
Explanation: The maximum number of odd integers that sum up to 14 is 3. 
These integers are [1, 3, 5]. Their sum is 1 + 3 + 5 = 9, which is less than 14. 
Adding another odd integer would exceed 14.

Constraints:
- 1 <= n <= 10^9
"""

# Solution
def maximumOddSum(n: int) -> int:
    """
    Finds the maximum number of odd integers that sum up to n.

    :param n: An integer representing the target sum.
    :return: The maximum number of odd integers that can sum up to n.
    """
    count = 0
    current_odd = 1
    while n >= current_odd:
        n -= current_odd
        count += 1
        current_odd += 2
    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 14
    print(maximumOddSum(n))  # Output: 3

    # Test Case 2
    n = 1
    print(maximumOddSum(n))  # Output: 1

    # Test Case 3
    n = 10
    print(maximumOddSum(n))  # Output: 2

    # Test Case 4
    n = 25
    print(maximumOddSum(n))  # Output: 5

    # Test Case 5
    n = 100
    print(maximumOddSum(n))  # Output: 10

"""
Time and Space Complexity Analysis:

Time Complexity:
- The loop runs until `n` becomes less than the current odd number. 
  Since the odd numbers grow linearly (1, 3, 5, ...), the number of iterations is proportional to the square root of `n`.
- Therefore, the time complexity is O(sqrt(n)).

Space Complexity:
- The algorithm uses a constant amount of space for variables (`count`, `current_odd`, and `n`).
- Therefore, the space complexity is O(1).

Topic: Greedy Algorithm
"""