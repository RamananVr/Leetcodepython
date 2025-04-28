"""
LeetCode Problem #972: Equal Rational Numbers

Problem Statement:
Given two strings `s1` and `s2`, each of which represents a decimal number, return true if the two numbers are equal. The decimal numbers may contain the following parts:
1. An integer part (non-negative, may be empty).
2. A fractional part (non-negative, may be empty).
3. A repeating part (enclosed in parentheses, may be empty).

The repeating part of a decimal expansion is the part of the decimal that repeats infinitely. For example:
- "0.333(3)" means 0.333333... (the 3 repeats infinitely).
- "2.5(0)" means 2.50000... (the 0 repeats infinitely).
- "0.1666(6)" means 0.166666... (the 6 repeats infinitely).

A decimal number can be represented in multiple ways. For example:
- "0.1(6)" -> "0.166666..."
- "0.166(66)" -> "0.166666..."
- "0.1666(6)" -> "0.166666..."

Return true if the two decimal numbers represented by `s1` and `s2` are the same, otherwise return false.

Constraints:
- Each string `s1` and `s2` consists of digits, '.', '(', ')', and is non-empty.
- Each string is a valid representation of a decimal number.
"""

from fractions import Fraction

def isRationalEqual(s1: str, s2: str) -> bool:
    """
    Determines if two rational numbers represented as strings are equal.
    """
    def convert_to_fraction(s: str) -> Fraction:
        if '(' not in s:
            # If there's no repeating part, directly convert to Fraction
            return Fraction(s)
        
        # Split into non-repeating and repeating parts
        non_repeating, repeating = s.split('(')
        repeating = repeating.rstrip(')')
        
        if '.' not in non_repeating:
            non_repeating += '.'
        
        # Calculate the fraction for the non-repeating part
        integer_part, fractional_part = non_repeating.split('.')
        base_fraction = Fraction(int(integer_part + fractional_part), 10 ** len(fractional_part))
        
        # Calculate the fraction for the repeating part
        if repeating:
            repeating_length = len(repeating)
            repeating_value = int(repeating)
            repeating_fraction = Fraction(repeating_value, (10 ** repeating_length - 1) * (10 ** len(fractional_part)))
        else:
            repeating_fraction = Fraction(0)
        
        return base_fraction + repeating_fraction

    # Convert both strings to fractions and compare
    return convert_to_fraction(s1) == convert_to_fraction(s2)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Simple equality
    assert isRationalEqual("0.1(6)", "0.1666(6)") == True

    # Test Case 2: Different representations of the same number
    assert isRationalEqual("0.9(9)", "1.0") == True

    # Test Case 3: No repeating part
    assert isRationalEqual("2.5", "2.5") == True

    # Test Case 4: Different numbers
    assert isRationalEqual("0.1", "0.2") == False

    # Test Case 5: Complex repeating parts
    assert isRationalEqual("0.(52)", "0.5(25)") == True

    # Test Case 6: No fractional part
    assert isRationalEqual("3", "3.0") == True

    print("All test cases passed!")

"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - Parsing the input string and splitting it into non-repeating and repeating parts takes O(n), where n is the length of the string.
   - Converting the non-repeating and repeating parts into fractions involves basic arithmetic operations, which are O(1) for small numbers.
   - Overall, the time complexity for each string is O(n), and since we process two strings, the total time complexity is O(n1 + n2), where n1 and n2 are the lengths of `s1` and `s2`.

2. Space Complexity:
   - The space required to store the intermediate non-repeating and repeating parts is proportional to the length of the input string.
   - The space complexity is O(n1 + n2), where n1 and n2 are the lengths of `s1` and `s2`.

Topic: Strings, Math, Fractions
"""