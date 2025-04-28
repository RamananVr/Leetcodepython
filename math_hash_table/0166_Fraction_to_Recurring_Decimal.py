"""
LeetCode Problem #166: Fraction to Recurring Decimal

Problem Statement:
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

If multiple answers are possible, return any of them.

It is guaranteed that the absolute value of the numerator and denominator will fit within a 32-bit integer.

Example 1:
Input: numerator = 1, denominator = 2
Output: "0.5"

Example 2:
Input: numerator = 2, denominator = 1
Output: "2"

Example 3:
Input: numerator = 2, denominator = 3
Output: "0.(6)"

Constraints:
- -2^31 <= numerator, denominator <= 2^31 - 1
- denominator != 0
"""

def fractionToDecimal(numerator: int, denominator: int) -> str:
    # Handle the case of zero numerator
    if numerator == 0:
        return "0"
    
    # Determine the sign of the result
    result = []
    if (numerator < 0) ^ (denominator < 0):
        result.append("-")
    
    # Work with absolute values for simplicity
    numerator, denominator = abs(numerator), abs(denominator)
    
    # Append the integer part
    result.append(str(numerator // denominator))
    remainder = numerator % denominator
    
    # If there is no fractional part, return the result
    if remainder == 0:
        return "".join(result)
    
    # Otherwise, handle the fractional part
    result.append(".")
    remainder_map = {}
    
    while remainder != 0:
        # If the remainder is already seen, we have a repeating fraction
        if remainder in remainder_map:
            result.insert(remainder_map[remainder], "(")
            result.append(")")
            break
        
        # Store the position of this remainder
        remainder_map[remainder] = len(result)
        
        # Perform the division
        remainder *= 10
        result.append(str(remainder // denominator))
        remainder %= denominator
    
    return "".join(result)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    numerator = 1
    denominator = 2
    print(fractionToDecimal(numerator, denominator))  # Output: "0.5"

    # Test Case 2
    numerator = 2
    denominator = 1
    print(fractionToDecimal(numerator, denominator))  # Output: "2"

    # Test Case 3
    numerator = 2
    denominator = 3
    print(fractionToDecimal(numerator, denominator))  # Output: "0.(6)"

    # Test Case 4
    numerator = 4
    denominator = 333
    print(fractionToDecimal(numerator, denominator))  # Output: "0.(012)"

    # Test Case 5
    numerator = 1
    denominator = 5
    print(fractionToDecimal(numerator, denominator))  # Output: "0.2"

"""
Time Complexity Analysis:
- The integer division and modulus operations take O(1).
- The while loop iterates at most once for each unique remainder. Since the remainder can only take values between 0 and (denominator - 1), the loop runs at most O(denominator) times.
- Therefore, the time complexity is O(denominator).

Space Complexity Analysis:
- The space complexity is O(denominator) due to the `remainder_map` dictionary, which stores at most one entry for each unique remainder.

Topic: Math, Hash Table
"""