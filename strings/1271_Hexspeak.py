"""
LeetCode Problem #1271: Hexspeak

Problem Statement:
A decimal number can be converted to its Hexspeak representation by first converting it to an uppercase hexadecimal string, 
then replacing all occurrences of the digit 0 with the letter "O", and the digit 1 with the letter "I". 
Such a representation is valid if and only if it consists only of the letters in the set {"A", "B", "C", "D", "E", "F", "I", "O"}.

Given a string `num` representing a decimal integer `N`, return the Hexspeak representation of `N` if it is valid, or "ERROR" if it is not.

Constraints:
- 1 <= num.length <= 12
- num does not contain leading zeros.
- num is guaranteed to represent a positive integer.

Example 1:
Input: num = "257"
Output: "IOI"
Explanation: 257 in hexadecimal is 101. Replace the digit 1 with "I" and the digit 0 with "O".

Example 2:
Input: num = "3"
Output: "ERROR"
Explanation: 3 in hexadecimal is 3. It contains a digit other than 0, 1, A-F.

"""

def toHexspeak(num: str) -> str:
    # Convert the number to hexadecimal and make it uppercase
    hex_representation = hex(int(num))[2:].upper()
    
    # Replace '0' with 'O' and '1' with 'I'
    hex_representation = hex_representation.replace('0', 'O').replace('1', 'I')
    
    # Check if the resulting string contains only valid characters
    valid_chars = set("ABCDEFIO")
    if all(char in valid_chars for char in hex_representation):
        return hex_representation
    else:
        return "ERROR"

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    num1 = "257"
    print(toHexspeak(num1))  # Output: "IOI"

    # Test Case 2
    num2 = "3"
    print(toHexspeak(num2))  # Output: "ERROR"

    # Test Case 3
    num3 = "16"
    print(toHexspeak(num3))  # Output: "IO"

    # Test Case 4
    num4 = "170"
    print(toHexspeak(num4))  # Output: "AA"

    # Test Case 5
    num5 = "123456789"
    print(toHexspeak(num5))  # Output: "ERROR"

"""
Time and Space Complexity Analysis:

Time Complexity:
- Converting the number to an integer and then to hexadecimal takes O(log(N)) time, where N is the value of the number.
- Replacing characters in the string and checking for valid characters takes O(L) time, where L is the length of the hexadecimal string.
- Overall, the time complexity is O(log(N)).

Space Complexity:
- The space required for the hexadecimal string and the modified string is O(L), where L is the length of the hexadecimal string.
- The set of valid characters is constant in size, so it takes O(1) space.
- Overall, the space complexity is O(L).

Topic: Strings
"""