"""
LeetCode Problem #22: Generate Parentheses

Problem Statement:
Given `n` pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]

Example 2:
Input: n = 1
Output: ["()"]

Constraints:
- 1 <= n <= 8
"""

def generateParenthesis(n):
    """
    Generate all combinations of well-formed parentheses.

    :param n: int - Number of pairs of parentheses
    :return: List[str] - All valid combinations of parentheses
    """
    def backtrack(s, open_count, close_count):
        # If the current string is valid and complete, add it to the result
        if len(s) == 2 * n:
            result.append(s)
            return
        
        # Add an open parenthesis if we haven't used all of them
        if open_count < n:
            backtrack(s + "(", open_count + 1, close_count)
        
        # Add a close parenthesis if it won't make the string invalid
        if close_count < open_count:
            backtrack(s + ")", open_count, close_count + 1)
    
    result = []
    backtrack("", 0, 0)
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 3
    print(f"Input: n = {n}")
    print(f"Output: {generateParenthesis(n)}")
    # Expected Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]

    # Test Case 2
    n = 1
    print(f"Input: n = {n}")
    print(f"Output: {generateParenthesis(n)}")
    # Expected Output: ["()"]

    # Test Case 3
    n = 2
    print(f"Input: n = {n}")
    print(f"Output: {generateParenthesis(n)}")
    # Expected Output: ["(())", "()()"]

"""
Topic: Backtracking
"""