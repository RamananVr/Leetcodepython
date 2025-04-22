"""
LeetCode Question #43: Multiply Strings

Problem Statement:
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note:
1. The input numbers are strings and may be arbitrarily large.
2. You must not use any built-in BigInteger library or convert the inputs to integers directly.
3. You are allowed to use only string manipulation and basic arithmetic operations.

Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"

Constraints:
- 1 <= num1.length, num2.length <= 200
- num1 and num2 consist of digits only.
- Both num1 and num2 do not contain any leading zero, except the number "0" itself.
"""

def multiplyStrings(num1: str, num2: str) -> str:
    # Edge case: if either number is "0", the result is "0"
    if num1 == "0" or num2 == "0":
        return "0"
    
    # Initialize a result array to store intermediate sums
    result = [0] * (len(num1) + len(num2))
    
    # Reverse both strings to simplify position calculations
    num1 = num1[::-1]
    num2 = num2[::-1]
    
    # Perform multiplication digit by digit
    for i in range(len(num1)):
        for j in range(len(num2)):
            # Multiply the digits and add to the corresponding position in the result array
            result[i + j] += int(num1[i]) * int(num2[j])
            # Handle carry
            result[i + j + 1] += result[i + j] // 10
            result[i + j] %= 10
    
    # Remove leading zeros and reverse the result array to form the final string
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    
    return ''.join(map(str, result[::-1]))

# Example test cases
if __name__ == "__main__":
    # Test case 1
    num1 = "2"
    num2 = "3"
    print(multiplyStrings(num1, num2))  # Output: "6"

    # Test case 2
    num1 = "123"
    num2 = "456"
    print(multiplyStrings(num1, num2))  # Output: "56088"

    # Test case 3
    num1 = "0"
    num2 = "12345"
    print(multiplyStrings(num1, num2))  # Output: "0"

    # Test case 4
    num1 = "999"
    num2 = "999"
    print(multiplyStrings(num1, num2))  # Output: "998001"

# Topic: Strings, Simulation