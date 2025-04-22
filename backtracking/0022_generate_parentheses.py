"""
LeetCode Question #22: Generate Parentheses

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

# Solution
def generateParenthesis(n: int) -> list[str]:
    """
    Generate all combinations of well-formed parentheses.

    :param n: Number of pairs of parentheses
    :return: List of all valid combinations
    """
    result = []

    def backtrack(current: str, open_count: int, close_count: int):
        # If the current string has reached the maximum length, add it to the result
        if len(current) == 2 * n:
            result.append(current)
            return
        
        # Add an open parenthesis if we haven't used all of them
        if open_count < n:
            backtrack(current + "(", open_count + 1, close_count)
        
        # Add a close parenthesis if it won't make the string invalid
        if close_count < open_count:
            backtrack(current + ")", open_count, close_count + 1)
    
    # Start the backtracking process
    backtrack("", 0, 0)
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 3
    print(f"Input: n = {n1}")
    print(f"Output: {generateParenthesis(n1)}")
    # Expected Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]

    # Test Case 2
    n2 = 1
    print(f"Input: n = {n2}")
    print(f"Output: {generateParenthesis(n2)}")
    # Expected Output: ["()"]

    # Test Case 3
    n3 = 2
    print(f"Input: n = {n3}")
    print(f"Output: {generateParenthesis(n3)}")
    # Expected Output: ["(())", "()()"]

"""
Time Complexity Analysis:
- The total number of valid parentheses combinations for `n` pairs is given by the nth Catalan number, which is approximately (4^n) / (n * sqrt(n)) for large `n`.
- The backtracking algorithm generates each valid combination exactly once, and each combination takes O(n) time to construct.
- Therefore, the time complexity is O((4^n) / sqrt(n)).

Space Complexity Analysis:
- The space complexity is determined by the recursion stack and the space required to store the result.
- The recursion stack can go as deep as 2n (the length of the string being constructed).
- The result list will store all valid combinations, which is proportional to the nth Catalan number.
- Thus, the space complexity is O((4^n) / sqrt(n)).

Topic: Backtracking
"""