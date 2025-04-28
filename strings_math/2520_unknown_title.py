"""
LeetCode Problem #2520: Count the Digits That Divide a Number

Problem Statement:
You are given a positive integer `num`. Let `count` be the number of digits in `num` that divide `num`.

A digit `d` divides `num` if `num % d == 0`.

Return the number of digits in `num` that divide `num`.

Note:
- The input `num` is guaranteed to be a positive integer.
- A digit is a single character in the decimal representation of `num`.

Constraints:
- 1 <= num <= 10^9
"""

def countDigits(num: int) -> int:
    """
    Function to count the digits in `num` that divide `num`.

    Args:
    num (int): A positive integer.

    Returns:
    int: The count of digits in `num` that divide `num`.
    """
    count = 0
    for digit in str(num):
        d = int(digit)
        if d != 0 and num % d == 0:
            count += 1
    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    num = 121
    print(f"Input: {num}, Output: {countDigits(num)}")  # Expected Output: 2

    # Test Case 2
    num = 1248
    print(f"Input: {num}, Output: {countDigits(num)}")  # Expected Output: 4

    # Test Case 3
    num = 101
    print(f"Input: {num}, Output: {countDigits(num)}")  # Expected Output: 1

    # Test Case 4
    num = 7
    print(f"Input: {num}, Output: {countDigits(num)}")  # Expected Output: 1

    # Test Case 5
    num = 10
    print(f"Input: {num}, Output: {countDigits(num)}")  # Expected Output: 1

"""
Time Complexity Analysis:
- Converting `num` to a string takes O(log10(num)) time, as the number of digits in `num` is proportional to log10(num).
- Iterating through each digit in the string representation of `num` takes O(log10(num)) time.
- For each digit, the modulo operation takes O(1) time.
- Overall, the time complexity is O(log10(num)).

Space Complexity Analysis:
- The space required to store the string representation of `num` is O(log10(num)).
- No additional data structures are used, so the overall space complexity is O(log10(num)).

Topic: Strings, Math
"""