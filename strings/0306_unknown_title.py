"""
LeetCode Problem #306: Additive Number

Problem Statement:
An additive number is a string whose digits can form an additive sequence. A valid additive sequence should contain at least three numbers. 
Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

Given a string containing only digits, return true if it is an additive number, or false otherwise.

Note:
- Numbers in the additive sequence cannot have leading zeros, so "01" or "1" are valid numbers, but "00" or "02" are not.

Example 1:
Input: "112358"
Output: true
Explanation: The digits can form the additive sequence: 1, 1, 2, 3, 5, 8.
             1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8

Example 2:
Input: "199100199"
Output: true
Explanation: The additive sequence is: 1, 99, 100, 199.
             1 + 99 = 100, 99 + 100 = 199

Constraints:
- 1 <= num.length <= 35
- num consists only of digits.

Follow-up:
How would you handle overflow for very large input numbers?
"""

def isAdditiveNumber(num: str) -> bool:
    def is_valid_sequence(num1: int, num2: int, remaining: str) -> bool:
        while remaining:
            next_num = num1 + num2
            next_num_str = str(next_num)
            if not remaining.startswith(next_num_str):
                return False
            remaining = remaining[len(next_num_str):]
            num1, num2 = num2, next_num
        return True

    n = len(num)
    for i in range(1, n):
        for j in range(i + 1, n):
            num1, num2 = num[:i], num[i:j]
            # Skip if numbers have leading zeros
            if (len(num1) > 1 and num1[0] == '0') or (len(num2) > 1 and num2[0] == '0'):
                continue
            if is_valid_sequence(int(num1), int(num2), num[j:]):
                return True
    return False

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    num1 = "112358"
    print(isAdditiveNumber(num1))  # Output: True

    # Test Case 2
    num2 = "199100199"
    print(isAdditiveNumber(num2))  # Output: True

    # Test Case 3
    num3 = "123"
    print(isAdditiveNumber(num3))  # Output: True

    # Test Case 4
    num4 = "1023"
    print(isAdditiveNumber(num4))  # Output: False

    # Test Case 5
    num5 = "000"
    print(isAdditiveNumber(num5))  # Output: True

"""
Time and Space Complexity Analysis:

Time Complexity:
- The outer loop iterates over the first number's length (up to n-2), and the inner loop iterates over the second number's length (up to n-1).
- For each pair of numbers, we check the remaining string to see if it forms a valid additive sequence.
- In the worst case, this involves O(n^3) operations, where n is the length of the input string.

Space Complexity:
- The space complexity is O(1) since we are not using any additional data structures apart from a few variables.

Topic: Strings
"""