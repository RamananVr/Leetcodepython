"""
LeetCode Problem #592: Fraction Addition and Subtraction

Problem Statement:
Given a string expression representing an expression of fractions, you need to return the result of the calculation in the form of a reduced fraction. If the result is an integer, represent it as a fraction with a denominator of 1. The input string contains fractions separated by '+' or '-' signs. Each fraction consists of a numerator and a denominator separated by '/'.

Example:
Input: expression = "-1/2+1/2"
Output: "0/1"

Input: expression = "-1/2+1/2+1/3"
Output: "1/3"

Input: expression = "1/3-1/2"
Output: "-1/6"

Constraints:
- The input string only contains valid fractions and operators.
- The string is non-empty and contains valid operations.
- The numerator and denominator of each fraction will be in the range [-10^6, 10^6].
"""

from math import gcd

def fractionAddition(expression: str) -> str:
    """
    Function to compute the result of fraction addition and subtraction.
    """
    def lcm(a, b):
        """Helper function to compute the least common multiple."""
        return abs(a * b) // gcd(a, b)
    
    fractions = []
    i = 0
    n = len(expression)
    
    # Parse the input expression into fractions
    while i < n:
        # Determine the sign
        sign = 1
        if expression[i] == '-':
            sign = -1
            i += 1
        elif expression[i] == '+':
            i += 1
        
        # Parse the numerator
        numerator = 0
        while i < n and expression[i].isdigit():
            numerator = numerator * 10 + int(expression[i])
            i += 1
        
        # Skip the '/' character
        i += 1
        
        # Parse the denominator
        denominator = 0
        while i < n and expression[i].isdigit():
            denominator = denominator * 10 + int(expression[i])
            i += 1
        
        # Add the fraction to the list
        fractions.append((sign * numerator, denominator))
    
    # Initialize the result fraction
    result_numerator = 0
    result_denominator = 1
    
    # Compute the result fraction
    for numerator, denominator in fractions:
        # Find the least common multiple of the denominators
        result_denominator = lcm(result_denominator, denominator)
    
    for numerator, denominator in fractions:
        result_numerator += numerator * (result_denominator // denominator)
    
    # Simplify the result fraction
    common_divisor = gcd(result_numerator, result_denominator)
    result_numerator //= common_divisor
    result_denominator //= common_divisor
    
    return f"{result_numerator}/{result_denominator}"

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    expression = "-1/2+1/2"
    print(fractionAddition(expression))  # Output: "0/1"
    
    # Test Case 2
    expression = "-1/2+1/2+1/3"
    print(fractionAddition(expression))  # Output: "1/3"
    
    # Test Case 3
    expression = "1/3-1/2"
    print(fractionAddition(expression))  # Output: "-1/6"
    
    # Test Case 4
    expression = "5/6+7/8-3/4"
    print(fractionAddition(expression))  # Output: "59/24"

"""
Time and Space Complexity Analysis:

Time Complexity:
- Parsing the input expression takes O(n), where n is the length of the input string.
- Computing the least common multiple (LCM) for all denominators takes O(k), where k is the number of fractions.
- Adding the fractions and simplifying the result takes O(k).
- Overall, the time complexity is O(n + k).

Space Complexity:
- The space required to store the fractions is O(k), where k is the number of fractions.
- Additional space is used for intermediate calculations, but it is negligible.
- Overall, the space complexity is O(k).

Topic: Math, String Parsing
"""