"""
LeetCode Problem #13: Roman to Integer

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

For example, 2 is written as II in Roman numeral, just two ones added together. 
12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. 
Instead, the number four is written as IV. Because the one is before the five, we subtract it making four. 
The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

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
Explanation: L = 50, V= 5, III = 3.

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
    # Define a mapping of Roman numerals to their integer values
    roman_to_int = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    # Iterate through the Roman numeral string in reverse
    for char in reversed(s):
        current_value = roman_to_int[char]
        
        # If the current value is less than the previous value, subtract it
        if current_value < prev_value:
            total -= current_value
        else:
            # Otherwise, add it to the total
            total += current_value
        
        # Update the previous value
        prev_value = current_value
    
    return total

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "III"
    print(f"Input: {s1}, Output: {romanToInt(s1)}")  # Output: 3

    # Test Case 2
    s2 = "LVIII"
    print(f"Input: {s2}, Output: {romanToInt(s2)}")  # Output: 58

    # Test Case 3
    s3 = "MCMXCIV"
    print(f"Input: {s3}, Output: {romanToInt(s3)}")  # Output: 1994

    # Test Case 4
    s4 = "IV"
    print(f"Input: {s4}, Output: {romanToInt(s4)}")  # Output: 4

    # Test Case 5
    s5 = "CM"
    print(f"Input: {s5}, Output: {romanToInt(s5)}")  # Output: 900

"""
Time Complexity Analysis:
- The function iterates through the string `s` once, performing constant-time operations for each character.
- Let n be the length of the string `s`. The time complexity is O(n).

Space Complexity Analysis:
- The function uses a fixed-size dictionary to store the Roman numeral mappings and a few integer variables.
- The space complexity is O(1) (constant space).

Topic: Strings
"""