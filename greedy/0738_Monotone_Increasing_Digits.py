"""
LeetCode Problem #738: Monotone Increasing Digits

Problem Statement:
Given a non-negative integer `n`, find the largest number that is less than or equal to `n` 
and whose digits are in non-decreasing order (i.e., each digit is less than or equal to the next digit).

Example 1:
Input: n = 10
Output: 9

Example 2:
Input: n = 1234
Output: 1234

Example 3:
Input: n = 332
Output: 299

Constraints:
- 0 <= n <= 10^9
"""

def monotoneIncreasingDigits(n: int) -> int:
    """
    Finds the largest number less than or equal to n with digits in non-decreasing order.
    """
    digits = list(str(n))
    length = len(digits)
    marker = length  # Marker to track where digits need to be adjusted
    
    # Traverse the digits from right to left
    for i in range(length - 1, 0, -1):
        if digits[i] < digits[i - 1]:  # If current digit is less than the previous digit
            marker = i  # Update marker
            digits[i - 1] = str(int(digits[i - 1]) - 1)  # Decrease the previous digit
    
    # Replace all digits after the marker with '9'
    for i in range(marker, length):
        digits[i] = '9'
    
    return int("".join(digits))

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 10
    print(monotoneIncreasingDigits(n1))  # Output: 9

    # Test Case 2
    n2 = 1234
    print(monotoneIncreasingDigits(n2))  # Output: 1234

    # Test Case 3
    n3 = 332
    print(monotoneIncreasingDigits(n3))  # Output: 299

    # Additional Test Case 4
    n4 = 987654321
    print(monotoneIncreasingDigits(n4))  # Output: 899999999

    # Additional Test Case 5
    n5 = 0
    print(monotoneIncreasingDigits(n5))  # Output: 0

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through the digits of the number, which has at most log10(n) digits.
- Therefore, the time complexity is O(log10(n)).

Space Complexity:
- The algorithm uses a list to store the digits of the number, which requires O(log10(n)) space.
- No additional data structures are used, so the space complexity is O(log10(n)).

Topic: Greedy
"""