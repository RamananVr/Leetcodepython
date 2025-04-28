"""
LeetCode Problem #1137: N-th Tribonacci Number

Problem Statement:
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

Example 1:
Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4

Example 2:
Input: n = 25
Output: 1389537

Constraints:
- 0 <= n <= 37
- The answer is guaranteed to fit within a 32-bit integer, i.e., answer <= 2^31 - 1.
"""

def tribonacci(n: int) -> int:
    """
    Calculate the n-th Tribonacci number using an iterative approach.

    :param n: The index of the Tribonacci number to compute.
    :return: The n-th Tribonacci number.
    """
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1

    # Initialize the first three Tribonacci numbers
    t0, t1, t2 = 0, 1, 1

    # Compute the Tribonacci numbers iteratively
    for _ in range(3, n + 1):
        t3 = t0 + t1 + t2
        t0, t1, t2 = t1, t2, t3

    return t2

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 4
    print(f"Tribonacci({n1}) = {tribonacci(n1)}")  # Expected Output: 4

    # Test Case 2
    n2 = 25
    print(f"Tribonacci({n2}) = {tribonacci(n2)}")  # Expected Output: 1389537

    # Test Case 3
    n3 = 0
    print(f"Tribonacci({n3}) = {tribonacci(n3)}")  # Expected Output: 0

    # Test Case 4
    n4 = 1
    print(f"Tribonacci({n4}) = {tribonacci(n4)}")  # Expected Output: 1

    # Test Case 5
    n5 = 2
    print(f"Tribonacci({n5}) = {tribonacci(n5)}")  # Expected Output: 1

"""
Time Complexity Analysis:
- The algorithm iterates from 3 to n, performing a constant amount of work in each iteration.
- Therefore, the time complexity is O(n).

Space Complexity Analysis:
- The algorithm uses only a constant amount of space to store the last three Tribonacci numbers.
- Therefore, the space complexity is O(1).

Topic: Dynamic Programming (DP)
"""