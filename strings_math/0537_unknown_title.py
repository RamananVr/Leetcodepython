"""
LeetCode Problem #537: Complex Number Multiplication

Problem Statement:
A complex number can be represented as a string of the form "real+imaginaryi" where:
- real is the real part, and imaginary is the imaginary part of the complex number.
- i represents the imaginary unit.

You need to return the result of multiplying two complex numbers given as strings.

The input strings are guaranteed to be valid complex numbers.

Example:
Input: num1 = "1+1i", num2 = "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i + i + i^2 = 1 + 2i - 1 = 0 + 2i

Input: num1 = "1+-1i", num2 = "1+-1i"
Output: "0+-2i"
Explanation: (1 - i) * (1 - i) = 1 - i - i + i^2 = 1 - 2i - 1 = 0 - 2i

Constraints:
- num1 and num2 are valid complex numbers.
- There will be no extra spaces in the input strings.
- The input strings will not have leading or trailing zeros.

"""

def complexNumberMultiply(num1: str, num2: str) -> str:
    """
    Multiplies two complex numbers represented as strings and returns the result as a string.
    """
    # Parse the real and imaginary parts of num1
    real1, imag1 = map(int, num1[:-1].split('+'))
    # Parse the real and imaginary parts of num2
    real2, imag2 = map(int, num2[:-1].split('+'))
    
    # Perform the multiplication of complex numbers
    real_part = real1 * real2 - imag1 * imag2
    imag_part = real1 * imag2 + imag1 * real2
    
    # Return the result as a string
    return f"{real_part}+{imag_part}i"

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    num1 = "1+1i"
    num2 = "1+1i"
    print(complexNumberMultiply(num1, num2))  # Output: "0+2i"

    # Test Case 2
    num1 = "1+-1i"
    num2 = "1+-1i"
    print(complexNumberMultiply(num1, num2))  # Output: "0+-2i"

    # Test Case 3
    num1 = "2+3i"
    num2 = "4+-5i"
    print(complexNumberMultiply(num1, num2))  # Output: "23+2i"

    # Test Case 4
    num1 = "0+0i"
    num2 = "0+0i"
    print(complexNumberMultiply(num1, num2))  # Output: "0+0i"

# Time and Space Complexity Analysis
# Time Complexity: O(1)
# - Parsing the input strings and performing the arithmetic operations are constant-time operations.
# - The input size is fixed and small, so the complexity is O(1).

# Space Complexity: O(1)
# - The function uses a constant amount of extra space for variables to store intermediate results.
# - The output string is also of constant size.

# Topic: Strings, Math