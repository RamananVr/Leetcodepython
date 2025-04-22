"""
LeetCode Question #400: Nth Digit

Problem Statement:
Given an integer n, return the nth digit of the infinite integer sequence [1, 2, 3, 4, ...].

The sequence of digits is formed by concatenating the positive integers:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

For example, the sequence starts with the digits:
1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 0, 1, 1, ...

Constraints:
- 1 <= n <= 2 * 10^9
"""

def findNthDigit(n: int) -> int:
    """
    Finds the nth digit in the infinite integer sequence.
    """
    # Step 1: Determine the range of numbers where the nth digit lies
    digit_length = 1  # Number of digits in the current range
    count = 9         # Total number of digits in the current range

    while n > digit_length * count:
        n -= digit_length * count
        digit_length += 1
        count *= 10

    # Step 2: Find the actual number containing the nth digit
    start = 10 ** (digit_length - 1)  # Starting number of the current range
    number = start + (n - 1) // digit_length

    # Step 3: Find the specific digit within the number
    digit_index = (n - 1) % digit_length
    return int(str(number)[digit_index])

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Small input
    print(findNthDigit(3))  # Output: 3

    # Test Case 2: Transition from single-digit to double-digit numbers
    print(findNthDigit(11))  # Output: 0

    # Test Case 3: Larger input
    print(findNthDigit(15))  # Output: 2

    # Test Case 4: Edge case for large n
    print(findNthDigit(1000))  # Output: 3

"""
Time and Space Complexity Analysis:

Time Complexity:
- The while loop iterates over the ranges of numbers with increasing digit lengths (1-digit, 2-digit, etc.).
  Since the number of digits grows exponentially, the loop runs in O(log(n)) time.
- Extracting the digit from the number is a constant-time operation.
- Overall time complexity: O(log(n)).

Space Complexity:
- The algorithm uses a constant amount of space for variables and calculations.
- No additional data structures are used.
- Overall space complexity: O(1).

Topic: Math
"""