"""
LeetCode Question #13: Roman to Integer

Problem Statement:
Roman numerals are represented by seven different symbols: I, V, X, L, C, D, and M.

Symbol       Value
I            1
V            5
X            10
L            50
C            100
D            500
M            1000

For example, 2 is written as "II" in Roman numeral, just two ones added together. 
12 is written as "XII", which is simply X + II. The number 27 is written as "XXVII", which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not "IIII". 
Instead, the number four is written as "IV". Because the one is before the five, we subtract it making four. 
The same principle applies to the number nine, which is written as "IX". There are six instances where subtraction is used:

- I can be placed before V (5) and X (10) to make 4 and 9. 
- X can be placed before L (50) and C (100) to make 40 and 90. 
- C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

Example 1:
Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V = 5, III = 3.

Example 3:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90, IV = 4.

Constraints:
- 1 <= s.length <= 15
- s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
- It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""

def romanToInt(s: str) -> int:
    # Define a dictionary to map Roman numerals to their integer values
    roman_to_int = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 
        'C': 100, 'D': 500, 'M': 1000
    }
    
    # Initialize the result variable
    result = 0
    
    # Iterate through the string
    for i in range(len(s)):
        # If the current numeral is smaller than the next numeral, subtract it
        if i < len(s) - 1 and roman_to_int[s[i]] < roman_to_int[s[i + 1]]:
            result -= roman_to_int[s[i]]
        else:
            # Otherwise, add its value to the result
            result += roman_to_int[s[i]]
    
    return result

# Example test cases
if __name__ == "__main__":
    # Test case 1
    s1 = "III"
    print(f"Input: {s1}, Output: {romanToInt(s1)}")  # Expected Output: 3

    # Test case 2
    s2 = "LVIII"
    print(f"Input: {s2}, Output: {romanToInt(s2)}")  # Expected Output: 58

    # Test case 3
    s3 = "MCMXCIV"
    print(f"Input: {s3}, Output: {romanToInt(s3)}")  # Expected Output: 1994

    # Test case 4
    s4 = "IX"
    print(f"Input: {s4}, Output: {romanToInt(s4)}")  # Expected Output: 9

    # Test case 5
    s5 = "XL"
    print(f"Input: {s5}, Output: {romanToInt(s5)}")  # Expected Output: 40

# Topic: Strings