"""
LeetCode Problem #172: Factorial Trailing Zeroes

Problem Statement:
Given an integer `n`, return the number of trailing zeroes in `n!`.

Note:
- A trailing zero is created with a factor of 10.
- Since 10 = 2 × 5, and there are usually more factors of 2 than factors of 5 in a factorial, 
  the number of trailing zeroes is determined by the number of factors of 5 in `n!`.

Constraints:
- 0 <= n <= 10^4
"""

def trailingZeroes(n: int) -> int:
    """
    This function calculates the number of trailing zeroes in the factorial of n.
    """
    count = 0
    while n > 0:
        n //= 5
        count += n
    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Small input
    n1 = 5
    print(f"Trailing zeroes in {n1}! = {trailingZeroes(n1)}")  # Expected: 1

    # Test Case 2: Larger input
    n2 = 10
    print(f"Trailing zeroes in {n2}! = {trailingZeroes(n2)}")  # Expected: 2

    # Test Case 3: Edge case (n = 0)
    n3 = 0
    print(f"Trailing zeroes in {n3}! = {trailingZeroes(n3)}")  # Expected: 0

    # Test Case 4: Larger input
    n4 = 100
    print(f"Trailing zeroes in {n4}! = {trailingZeroes(n4)}")  # Expected: 24

    # Test Case 5: Very large input
    n5 = 10000
    print(f"Trailing zeroes in {n5}! = {trailingZeroes(n5)}")  # Expected: 2499

"""
Time Complexity Analysis:
- The while loop runs as long as n > 0, and in each iteration, n is divided by 5.
- The number of iterations is approximately log_5(n), so the time complexity is O(log n).

Space Complexity Analysis:
- The function uses a constant amount of space (only a few variables), so the space complexity is O(1).

Topic: Math
"""