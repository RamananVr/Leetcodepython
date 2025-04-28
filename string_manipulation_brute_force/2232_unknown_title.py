"""
LeetCode Problem #2232: Minimize Result by Adding Parentheses to Expression

Problem Statement:
You are given a 0-indexed string expression of the form "num1+num2" where num1 and num2 represent positive integers.

Add a pair of parentheses to the expression such that after the addition of parentheses, 
num1 and num2 are still valid positive integers, and the value of the new expression is minimized.

The result of the expression should be calculated as follows:
- Evaluate the expression inside the parentheses first.
- Multiply the result by the part of the expression to its left, if it exists.
- Multiply the result by the part of the expression to its right, if it exists.

Return the expression after adding a pair of parentheses such that the value of the expression is minimized.
If there are multiple answers that yield the same result, return any of them.

Example 1:
Input: expression = "247+38"
Output: "2(47+38)"
Explanation: The value of the expression is minimized to 2 * (47 + 38) = 2 * 85 = 170.

Example 2:
Input: expression = "12+34"
Output: "1(2+34)"
Explanation: The value of the expression is minimized to 1 * (2 + 34) = 1 * 36 = 36.

Example 3:
Input: expression = "999+999"
Output: "(999+999)"
Explanation: The value of the expression is minimized to (999 + 999) = 1998.

Constraints:
- 3 <= expression.length <= 50
- expression consists of digits '+' and digits only.
- All the integers represented in the input expression are positive integers with no leading zeros.
"""

def minimizeResult(expression: str) -> str:
    # Split the expression into num1 and num2
    num1, num2 = expression.split('+')
    n1_len, n2_len = len(num1), len(num2)
    
    # Initialize variables to track the minimum value and the corresponding result
    min_value = float('inf')
    result = ""
    
    # Iterate over all possible positions to place the opening and closing parentheses
    for i in range(n1_len):  # Position to place '(' in num1
        for j in range(1, n2_len + 1):  # Position to place ')' in num2
            # Split num1 and num2 into parts
            left = int(num1[:i]) if i > 0 else 1  # Left multiplier (default to 1 if no left part)
            middle = int(num1[i:]) + int(num2[:j])  # Sum inside parentheses
            right = int(num2[j:]) if j < n2_len else 1  # Right multiplier (default to 1 if no right part)
            
            # Calculate the value of the expression
            value = left * middle * right
            
            # Update the result if a smaller value is found
            if value < min_value:
                min_value = value
                result = f"{num1[:i]}({num1[i:]}+{num2[:j]}){num2[j:]}"
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    expression1 = "247+38"
    print(minimizeResult(expression1))  # Expected Output: "2(47+38)"
    
    # Test Case 2
    expression2 = "12+34"
    print(minimizeResult(expression2))  # Expected Output: "1(2+34)"
    
    # Test Case 3
    expression3 = "999+999"
    print(minimizeResult(expression3))  # Expected Output: "(999+999)"

# Time Complexity Analysis:
# Let n1 = len(num1) and n2 = len(num2).
# The algorithm iterates over all possible positions for '(' in num1 (n1 options) 
# and ')' in num2 (n2 options), resulting in O(n1 * n2) iterations.
# Each iteration involves simple arithmetic operations, which take O(1) time.
# Therefore, the overall time complexity is O(n1 * n2).

# Space Complexity Analysis:
# The algorithm uses a constant amount of extra space for variables and intermediate calculations.
# Therefore, the space complexity is O(1).

# Topic: String Manipulation, Brute Force