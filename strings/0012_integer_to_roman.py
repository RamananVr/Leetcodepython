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

For example, 2 is written as II in Roman numeral, just two ones added together. 
12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. 
Instead, the number four is written as IV. Because the one is before the five, we subtract it making four. 
The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

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
    :return: Roman numeral as a string
    """
    # Define the Roman numeral symbols and their corresponding values
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
    
    # Iterate through the Roman numeral map
    for value, symbol in roman_map:
        # While the current value can be subtracted from num
        while num >= value:
            result += symbol  # Append the Roman numeral symbol
            num -= value      # Subtract the value from num
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    print(intToRoman(3))  # Output: "III"
    
    # Test Case 2
    print(intToRoman(58))  # Output: "LVIII"
    
    # Test Case 3
    print(intToRoman(1994))  # Output: "MCMXCIV"
    
    # Test Case 4
    print(intToRoman(4))  # Output: "IV"
    
    # Test Case 5
    print(intToRoman(3999))  # Output: "MMMCMXCIX"

"""
Time and Space Complexity Analysis:

Time Complexity:
The time complexity of this solution is O(1). 
This is because the input number `num` is bounded by the constraint 1 <= num <= 3999, 
and the Roman numeral map has a fixed size of 13. 
The number of iterations in the while loop is proportional to the number of Roman numeral symbols required, 
which is constant for the given range.

Space Complexity:
The space complexity is O(1) as well. 
We use a fixed amount of extra space for the Roman numeral map and the result string, 
which grows linearly with the number of Roman numeral symbols but is bounded by the constraints.

Topic: Strings
"""