"""
LeetCode Problem #1017: Convert to Base -2

Problem Statement:
Given an integer n, return a string representation of its representation in base -2.

Base -2 is a numeral system with a negative base. A number is represented in base -2 using digits 0 and 1. The rules of base -2 are similar to those of other numeral systems, except that the base is negative.

The representation of each number in base -2 is unique.

Example 1:
Input: n = 2
Output: "110"
Explanation: (-2)^2 + (-2)^1 + (-2)^0 = 4 - 2 + 0 = 2

Example 2:
Input: n = 3
Output: "111"
Explanation: (-2)^2 + (-2)^1 + (-2)^0 = 4 - 2 + 1 = 3

Example 3:
Input: n = 4
Output: "100"
Explanation: (-2)^2 + (-2)^1 + (-2)^0 = 4 + 0 + 0 = 4

Constraints:
- 0 <= n <= 10^9
"""

def baseNeg2(n: int) -> str:
    """
    Convert an integer n to its representation in base -2.

    :param n: Integer to be converted (0 <= n <= 10^9)
    :return: String representation of n in base -2
    """
    if n == 0:
        return "0"
    
    result = []
    while n != 0:
        remainder = n % -2
        n //= -2
        
        # Adjust remainder and n if remainder is negative
        if remainder < 0:
            remainder += 2
            n += 1
        
        result.append(str(remainder))
    
    return ''.join(result[::-1])

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 2
    print(baseNeg2(n1))  # Output: "110"

    # Test Case 2
    n2 = 3
    print(baseNeg2(n2))  # Output: "111"

    # Test Case 3
    n3 = 4
    print(baseNeg2(n3))  # Output: "100"

    # Test Case 4
    n4 = 0
    print(baseNeg2(n4))  # Output: "0"

    # Test Case 5
    n5 = 7
    print(baseNeg2(n5))  # Output: "11011"

"""
Time and Space Complexity Analysis:

Time Complexity:
The algorithm repeatedly divides n by -2 until n becomes 0. The number of iterations is proportional to the number of digits in the base -2 representation of n. 
Since the number of digits in base -2 is approximately O(log(n)), the time complexity is O(log(n)).

Space Complexity:
The space complexity is O(log(n)) as well, because we store the digits of the base -2 representation in a list before reversing and joining them into a string.

Topic: Math, Number Systems
"""