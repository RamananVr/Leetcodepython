"""
LeetCode Question #241: Different Ways to Add Parentheses

Problem Statement:
Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, -, and *.

You may return the answer in any order.

Example 1:
Input: expression = "2-1-1"
Output: [0, 2]
Explanation:
((2-1)-1) = 0 
(2-(1-1)) = 2

Example 2:
Input: expression = "2*3-4*5"
Output: [-34, -14, -10, -10, 10]
Explanation:
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10

Constraints:
- 1 <= expression.length <= 20
- expression consists of digits and the operator '+', '-', and '*'.
- All the integer values in the input expression are in the range [0, 99].
"""

# Solution
def diffWaysToCompute(expression):
    """
    Function to compute all possible results from different ways to group numbers and operators.

    :param expression: str, the input mathematical expression
    :return: List[int], all possible results
    """
    # Base case: if the expression is a single number, return it as a result
    if expression.isdigit():
        return [int(expression)]
    
    results = []
    # Iterate through the expression to find operators
    for i, char in enumerate(expression):
        if char in "+-*":
            # Split the expression into left and right parts
            left = diffWaysToCompute(expression[:i])
            right = diffWaysToCompute(expression[i+1:])
            
            # Compute results for all combinations of left and right parts
            for l in left:
                for r in right:
                    if char == '+':
                        results.append(l + r)
                    elif char == '-':
                        results.append(l - r)
                    elif char == '*':
                        results.append(l * r)
    
    return results

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    expression1 = "2-1-1"
    print(f"Input: {expression1}")
    print(f"Output: {diffWaysToCompute(expression1)}")  # Expected Output: [0, 2]

    # Test Case 2
    expression2 = "2*3-4*5"
    print(f"Input: {expression2}")
    print(f"Output: {diffWaysToCompute(expression2)}")  # Expected Output: [-34, -14, -10, -10, 10]

    # Test Case 3
    expression3 = "3"
    print(f"Input: {expression3}")
    print(f"Output: {diffWaysToCompute(expression3)}")  # Expected Output: [3]

# Time and Space Complexity Analysis
"""
Time Complexity:
The time complexity is exponential, O(2^n), where n is the number of operators in the expression. This is because for each operator, we recursively compute results for the left and right subexpressions, leading to a combinatorial explosion of possibilities.

Space Complexity:
The space complexity is O(n), where n is the length of the expression. This is due to the recursive call stack depth, which can go up to the number of operators in the worst case.

Topic: Divide and Conquer
"""