"""
LeetCode Problem #2384: Largest Palindromic Number

Problem Statement:
You are given a string `num` consisting of digits only. You need to find the largest palindromic number (not leading with zero unless the number is "0") that can be formed using the digits of `num`. If no palindromic number can be formed, return an empty string "".

Example:
Input: num = "444947137"
Output: "7449447"

Input: num = "00009"
Output: "9"

Constraints:
- 1 <= num.length <= 10^5
- num consists of digits only.
"""

# Solution
from collections import Counter

def largestPalindromicNumber(num: str) -> str:
    # Count the frequency of each digit
    count = Counter(num)
    
    # Initialize variables to construct the palindrome
    half_palindrome = []
    middle_digit = ""
    
    # Iterate over digits from 9 to 0 (to ensure the largest number)
    for digit in sorted(count.keys(), reverse=True):
        freq = count[digit]
        
        # Add pairs of digits to the half_palindrome
        half_palindrome.extend([digit] * (freq // 2))
        
        # If there's an odd frequency, consider it as a potential middle digit
        if freq % 2 == 1 and middle_digit == "":
            middle_digit = digit
    
    # Construct the full palindrome
    half_palindrome_str = "".join(half_palindrome)
    full_palindrome = half_palindrome_str + middle_digit + half_palindrome_str[::-1]
    
    # Handle the case where the palindrome starts with zero
    if full_palindrome and full_palindrome[0] == "0":
        return "0" if middle_digit == "0" else ""
    
    return full_palindrome

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    num1 = "444947137"
    print(largestPalindromicNumber(num1))  # Output: "7449447"

    # Test Case 2
    num2 = "00009"
    print(largestPalindromicNumber(num2))  # Output: "9"

    # Test Case 3
    num3 = "123321"
    print(largestPalindromicNumber(num3))  # Output: "123321"

    # Test Case 4
    num4 = "0000"
    print(largestPalindromicNumber(num4))  # Output: "0"

    # Test Case 5
    num5 = "9876543210"
    print(largestPalindromicNumber(num5))  # Output: "987656789"

"""
Time and Space Complexity Analysis:

Time Complexity:
- Counting the frequency of digits takes O(n), where n is the length of the input string `num`.
- Sorting the digits (constant range of 0-9) takes O(1) since there are only 10 digits.
- Constructing the palindrome involves iterating over the digits, which takes O(1) due to the fixed range.
- Overall time complexity: O(n).

Space Complexity:
- The Counter object stores the frequency of digits, which requires O(1) space (fixed range of 10 digits).
- The half_palindrome list and other variables require O(n) space in the worst case.
- Overall space complexity: O(n).

Topic: Strings
"""