"""
LeetCode Question #227: Basic Calculator II

Problem Statement:
Given a string `s` which represents an expression, evaluate this expression and return its value. 
The integer division should truncate toward zero.

You may assume that the given string is always valid. All intermediate results will be in the range of 
[-2^31, 2^31 - 1].

Note:
- You are not allowed to use any built-in library function which evaluates strings as mathematical expressions, such as `eval()`.

Constraints:
- 1 <= s.length <= 3 * 10^5
- `s` consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
- `s` represents a valid expression.
- All the integers in the expression are non-negative integers in the range [0, 2^31 - 1].
- The answer is guaranteed to fit in a 32-bit integer.

Example 1:
Input: s = "3+2*2"
Output: 7

Example 2:
Input: s = " 3/2 "
Output: 1

Example 3:
Input: s = " 3+5 / 2 "
Output: 5
"""

def calculate(s: str) -> int:
    """
    Evaluate the given mathematical expression string and return the result.
    """
    # Initialize variables
    stack = []
    current_num = 0
    operation = '+'
    s = s.replace(" ", "")  # Remove all spaces for easier processing

    for i, char in enumerate(s):
        if char.isdigit():
            current_num = current_num * 10 + int(char)  # Build the current number
        # If the character is an operator or we are at the end of the string
        if char in "+-*/" or i == len(s) - 1:
            if operation == '+':
                stack.append(current_num)
            elif operation == '-':
                stack.append(-current_num)
            elif operation == '*':
                stack.append(stack.pop() * current_num)
            elif operation == '/':
                # Perform integer division truncating toward zero
                stack.append(int(stack.pop() / current_num))
            # Update operation and reset current_num
            operation = char
            current_num = 0

    # Sum up all the values in the stack to get the result
    return sum(stack)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "3+2*2"
    print(f"Input: {s1} -> Output: {calculate(s1)}")  # Expected Output: 7

    # Test Case 2
    s2 = " 3/2 "
    print(f"Input: {s2} -> Output: {calculate(s2)}")  # Expected Output: 1

    # Test Case 3
    s3 = " 3+5 / 2 "
    print(f"Input: {s3} -> Output: {calculate(s3)}")  # Expected Output: 5

    # Test Case 4
    s4 = "14-3/2"
    print(f"Input: {s4} -> Output: {calculate(s4)}")  # Expected Output: 13

    # Test Case 5
    s5 = "0-2147483647"
    print(f"Input: {s5} -> Output: {calculate(s5)}")  # Expected Output: -2147483647

"""
Time Complexity:
- O(n), where n is the length of the string `s`. We iterate through the string once, and each operation (push, pop, arithmetic) takes O(1) time.

Space Complexity:
- O(n), where n is the length of the string `s`. In the worst case, the stack can store all numbers in the expression.

Topic: Stack
"""