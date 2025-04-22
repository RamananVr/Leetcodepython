"""
LeetCode Problem #788: Rotated Digits

Problem Statement:
An integer x is a "good" number if after rotating each digit individually by 180 degrees, 
we get a valid number that is different from x. Each digit must be rotated - we cannot 
choose to leave it alone.

A number is valid if each digit remains a digit after rotation. For example:
- 0, 1, and 8 remain the same after rotation.
- 2 and 5 rotate to each other (i.e., 2 becomes 5 and vice versa).
- 6 and 9 rotate to each other (i.e., 6 becomes 9 and vice versa).

The digits 3, 4, and 7 are invalid after rotation.

Given an integer n, return the number of "good" integers in the range [1, n].

Example:
Input: n = 10
Output: 4
Explanation: There are four good numbers in the range [1, 10]: 2, 5, 6, and 9.

Constraints:
- 1 <= n <= 10^4
"""

# Solution
def rotatedDigits(n: int) -> int:
    def is_good_number(x: int) -> bool:
        valid_digits = {'0', '1', '8', '2', '5', '6', '9'}
        must_change_digits = {'2', '5', '6', '9'}
        
        digits = set(str(x))
        # Check if all digits are valid
        if not digits.issubset(valid_digits):
            return False
        # Check if at least one digit must change
        return any(d in must_change_digits for d in digits)
    
    count = 0
    for i in range(1, n + 1):
        if is_good_number(i):
            count += 1
    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 10
    print(rotatedDigits(n))  # Output: 4

    # Test Case 2
    n = 20
    print(rotatedDigits(n))  # Output: 9

    # Test Case 3
    n = 1
    print(rotatedDigits(n))  # Output: 0

    # Test Case 4
    n = 100
    print(rotatedDigits(n))  # Output: 40

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function iterates through all numbers from 1 to n, so the loop runs O(n) times.
- For each number, we check its digits, which takes O(d) time, where d is the number of digits in the number.
- In the worst case, d = log10(n), so the overall time complexity is O(n * log10(n)).

Space Complexity:
- The space complexity is O(d) for the set of digits of the current number, where d is the number of digits.
- In the worst case, d = log10(n), so the space complexity is O(log10(n)).

Topic: Math, String Manipulation
"""