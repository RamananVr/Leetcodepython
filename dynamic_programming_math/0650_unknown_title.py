"""
LeetCode Problem #650: 2 Keys Keyboard

Problem Statement:
You have a text editor with only two operations:
1. Copy All: You can copy all the characters present on the notepad (the entire string).
2. Paste: You can paste the characters that were last copied.

Initially, you have a single character 'A' on the notepad. You want to get exactly `n` 'A's on the notepad using the minimum number of operations. Write a function to calculate the minimum number of operations required to achieve this.

Constraints:
- 1 <= n <= 1000
"""

def minSteps(n: int) -> int:
    """
    Function to calculate the minimum number of operations to get exactly n 'A's on the notepad.
    """
    # Initialize the result (number of operations)
    result = 0
    # Start dividing n by its smallest prime factors
    factor = 2
    while n > 1:
        while n % factor == 0:
            result += factor
            n //= factor
        factor += 1
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 3
    print(f"Minimum steps to get {n} 'A's: {minSteps(n)}")  # Expected Output: 3

    # Test Case 2
    n = 1
    print(f"Minimum steps to get {n} 'A's: {minSteps(n)}")  # Expected Output: 0

    # Test Case 3
    n = 6
    print(f"Minimum steps to get {n} 'A's: {minSteps(n)}")  # Expected Output: 5

    # Test Case 4
    n = 9
    print(f"Minimum steps to get {n} 'A's: {minSteps(n)}")  # Expected Output: 6

    # Test Case 5
    n = 15
    print(f"Minimum steps to get {n} 'A's: {minSteps(n)}")  # Expected Output: 8

"""
Time Complexity Analysis:
- The algorithm iterates through all possible factors of `n` starting from 2.
- In the worst case, the number of iterations is proportional to the square root of `n` (for prime factorization).
- Thus, the time complexity is O(sqrt(n)).

Space Complexity Analysis:
- The algorithm uses a constant amount of extra space.
- Thus, the space complexity is O(1).

Topic: Dynamic Programming, Math
"""