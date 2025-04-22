"""
LeetCode Question #12: Integer to Roman

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

For example, 2 is written as II in Roman numeral, just two one's added together. 
12 is written as XII, which is simply X + II. The number 27 is written as XXVII, 
which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. 
However, the numeral for four is not IIII. Instead, the number four is written as IV. 
Because the one is before the five we subtract it making four. The same principle 
applies to the number nine, which is written as IX. There are six instances where 
subtraction is used:

- I can be placed before V (5) and X (10) to make 4 and 9. 
- X can be placed before L (50) and C (100) to make 40 and 90. 
- C can be placed before D (500) and M (1000) to make 400 and 900.

Given an integer, convert it to a Roman numeral.

Example 1:
Input: num = 3
Output: "III"

Example 2:
Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.

Example 3:
Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90, IV = 4.

Constraints:
- 1 <= num <= 3999
"""

def intToRoman(num: int) -> str:
    """
    Convert an integer to a Roman numeral.
    
    :param num: Integer to be converted (1 <= num <= 3999)
    :return: Roman numeral representation of the integer
    """
    # Define the Roman numeral mappings
    roman_map = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I")
    ]
    
    # Initialize the result string
    result = ""
    
    # Iterate through the Roman numeral mappings
    for value, symbol in roman_map:
        # Append the symbol while the number is greater than or equal to the value
        while num >= value:
            result += symbol
            num -= value
    
    return result

# Example test cases
if __name__ == "__main__":
    # Test case 1
    num1 = 3
    print(f"Input: {num1}, Output: {intToRoman(num1)}")  # Expected: "III"
    
    # Test case 2
    num2 = 58
    print(f"Input: {num2}, Output: {intToRoman(num2)}")  # Expected: "LVIII"
    
    # Test case 3
    num3 = 1994
    print(f"Input: {num3}, Output: {intToRoman(num3)}")  # Expected: "MCMXCIV"
    
    # Test case 4
    num4 = 3999
    print(f"Input: {num4}, Output: {intToRoman(num4)}")  # Expected: "MMMCMXCIX"
    
    # Test case 5
    num5 = 1
    print(f"Input: {num5}, Output: {intToRoman(num5)}")  # Expected: "I"

# Topic: Strings