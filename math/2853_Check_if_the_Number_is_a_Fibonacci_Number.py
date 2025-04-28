"""
LeetCode Problem #2853: Check if the Number is a Fibonacci Number

Problem Statement:
------------------
Given an integer `n`, determine if it is a Fibonacci number. A Fibonacci number is a number that appears in the Fibonacci sequence, 
where the sequence is defined as follows:
- F(0) = 0, F(1) = 1
- F(n) = F(n-1) + F(n-2) for n > 1

Return `True` if `n` is a Fibonacci number, otherwise return `False`.

Constraints:
------------
- 0 <= n <= 10^10
"""

def is_fibonacci_number(n: int) -> bool:
    """
    Determines if a given number `n` is a Fibonacci number.

    A number is a Fibonacci number if and only if one of the following is true:
    - 5 * n^2 + 4 is a perfect square
    - 5 * n^2 - 4 is a perfect square

    Args:
    - n (int): The number to check.

    Returns:
    - bool: True if `n` is a Fibonacci number, False otherwise.
    """
    import math

    def is_perfect_square(x: int) -> bool:
        """Helper function to check if a number is a perfect square."""
        s = int(math.sqrt(x))
        return s * s == x

    # Check the two conditions for Fibonacci numbers
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: n is a Fibonacci number
    n1 = 21
    print(is_fibonacci_number(n1))  # Expected: True

    # Test Case 2: n is not a Fibonacci number
    n2 = 22
    print(is_fibonacci_number(n2))  # Expected: False

    # Test Case 3: n is 0 (edge case)
    n3 = 0
    print(is_fibonacci_number(n3))  # Expected: True

    # Test Case 4: n is 1 (edge case)
    n4 = 1
    print(is_fibonacci_number(n4))  # Expected: True

    # Test Case 5: Large Fibonacci number
    n5 = 144
    print(is_fibonacci_number(n5))  # Expected: True

    # Test Case 6: Large non-Fibonacci number
    n6 = 150
    print(is_fibonacci_number(n6))  # Expected: False


"""
Time Complexity Analysis:
-------------------------
- The function `is_perfect_square` computes the square root of a number, which takes O(log(x)) time, where x is the input to the square root function.
- In this problem, the input to the square root function is proportional to `5 * n^2`, which is O(log(n^2)) = O(log(n)).
- Since we call `is_perfect_square` twice, the overall time complexity is O(log(n)).

Space Complexity Analysis:
--------------------------
- The function uses a constant amount of extra space, so the space complexity is O(1).

Topic: Math
"""