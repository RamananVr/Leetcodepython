"""
LeetCode Problem #1291: Sequential Digits

Problem Statement:
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

Example 1:
Input: low = 100, high = 300
Output: [123, 234]

Example 2:
Input: low = 1000, high = 13000
Output: [1234, 2345, 3456, 4567, 5678, 6789, 12345]

Constraints:
- 10 <= low <= high <= 10^9
"""

def sequentialDigits(low: int, high: int) -> list[int]:
    """
    Returns a sorted list of all integers in the range [low, high] that have sequential digits.
    """
    result = []
    digits = "123456789"  # All possible digits in sequential order
    n = len(digits)
    
    # Generate all sequential digit numbers
    for length in range(2, n + 1):  # Start with length 2 (minimum sequential digit number)
        for start in range(n - length + 1):  # Generate numbers of the current length
            num = int(digits[start:start + length])
            if low <= num <= high:
                result.append(num)
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    low = 100
    high = 300
    print(sequentialDigits(low, high))  # Output: [123, 234]

    # Test Case 2
    low = 1000
    high = 13000
    print(sequentialDigits(low, high))  # Output: [1234, 2345, 3456, 4567, 5678, 6789, 12345]

    # Test Case 3
    low = 10
    high = 100
    print(sequentialDigits(low, high))  # Output: [12, 23, 34, 45, 56, 67, 78, 89]

    # Test Case 4
    low = 58
    high = 155
    print(sequentialDigits(low, high))  # Output: [67, 78, 89, 123]

    # Test Case 5
    low = 100
    high = 1000
    print(sequentialDigits(low, high))  # Output: [123, 234, 345, 456, 567, 678, 789]

"""
Time Complexity:
- The outer loop iterates over possible lengths of sequential digit numbers (from 2 to 9), which is O(1) since the maximum length is fixed.
- The inner loop generates numbers of the current length, which is also bounded by a constant (at most 8 iterations for the longest length).
- Therefore, the overall time complexity is O(1), as the number of iterations is constant and does not depend on the input size.

Space Complexity:
- The space complexity is O(1) for the result list (excluding the output) and the constant string "123456789".
- The result list itself depends on the number of valid sequential digit numbers in the range, but this is part of the output.

Topic: String Manipulation, Sliding Window
"""