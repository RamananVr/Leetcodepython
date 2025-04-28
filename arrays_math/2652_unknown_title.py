"""
LeetCode Problem #2652: Sum Multiples

Problem Statement:
Given a positive integer `n`, find the sum of all integers in the range `[1, n]` that are divisible by 3, 5, or 7.

Return the sum of all such integers.

Constraints:
- 1 <= n <= 10^3
"""

def sum_of_multiples(n: int) -> int:
    """
    Calculate the sum of all integers in the range [1, n] that are divisible by 3, 5, or 7.

    :param n: The upper limit of the range (inclusive).
    :return: The sum of all integers divisible by 3, 5, or 7.
    """
    total_sum = 0
    for i in range(1, n + 1):
        if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
            total_sum += i
    return total_sum

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 7
    print(f"Sum of multiples for n={n}: {sum_of_multiples(n)}")  # Expected Output: 21

    # Test Case 2
    n = 10
    print(f"Sum of multiples for n={n}: {sum_of_multiples(n)}")  # Expected Output: 33

    # Test Case 3
    n = 15
    print(f"Sum of multiples for n={n}: {sum_of_multiples(n)}")  # Expected Output: 60

    # Test Case 4
    n = 1
    print(f"Sum of multiples for n={n}: {sum_of_multiples(n)}")  # Expected Output: 0

    # Test Case 5
    n = 20
    print(f"Sum of multiples for n={n}: {sum_of_multiples(n)}")  # Expected Output: 98

"""
Time Complexity:
- The function iterates through all integers from 1 to n, performing a constant-time operation (modulus and addition) for each integer.
- Therefore, the time complexity is O(n).

Space Complexity:
- The function uses a constant amount of extra space, regardless of the input size.
- Therefore, the space complexity is O(1).

Topic: Arrays / Math
"""