"""
LeetCode Problem #640: Solve the Equation

Problem Statement:
Solve a given equation and return the value of 'x' in the form of a string "x=#value". 
The equation contains only '+', '-', the variable 'x', and integers. The equation will 
always have exactly one '='. You may assume that the equation is always valid.

If there is no solution for the equation, return "No solution".
If there are infinite solutions for the equation, return "Infinite solutions".

Example:
Input: equation = "x+5-3+x=6+x-2"
Output: "x=2"

Input: equation = "x=x"
Output: "Infinite solutions"

Input: equation = "2x=x"
Output: "x=0"

Constraints:
- The equation contains only integers, '+', '-', 'x', and '='.
- The equation will always be valid.
- The length of the equation will not exceed 1000.
"""

# Python Solution
def solveEquation(equation: str) -> str:
    def parse_side(side: str):
        """Helper function to parse one side of the equation."""
        coeff, constant = 0, 0
        i, n = 0, len(side)
        while i < n:
            sign = 1
            if side[i] == '+':
                i += 1
            elif side[i] == '-':
                sign = -1
                i += 1
            
            if i < n and side[i] == 'x':
                coeff += sign
                i += 1
            else:
                num = 0
                while i < n and side[i].isdigit():
                    num = num * 10 + int(side[i])
                    i += 1
                if i < n and side[i] == 'x':
                    coeff += sign * num
                    i += 1
                else:
                    constant += sign * num
        return coeff, constant

    left, right = equation.split('=')
    left_coeff, left_const = parse_side(left)
    right_coeff, right_const = parse_side(right)

    # Combine coefficients and constants
    total_coeff = left_coeff - right_coeff
    total_const = right_const - left_const

    # Solve for x
    if total_coeff == 0:
        if total_const == 0:
            return "Infinite solutions"
        else:
            return "No solution"
    else:
        return f"x={total_const // total_coeff}"

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    equation = "x+5-3+x=6+x-2"
    print(solveEquation(equation))  # Output: "x=2"

    # Test Case 2
    equation = "x=x"
    print(solveEquation(equation))  # Output: "Infinite solutions"

    # Test Case 3
    equation = "2x=x"
    print(solveEquation(equation))  # Output: "x=0"

    # Test Case 4
    equation = "x+3=3+x"
    print(solveEquation(equation))  # Output: "Infinite solutions"

    # Test Case 5
    equation = "x+2=3"
    print(solveEquation(equation))  # Output: "x=1"

# Time and Space Complexity Analysis
"""
Time Complexity:
- Parsing each side of the equation takes O(n), where n is the length of the equation.
- Combining coefficients and constants is O(1).
- Overall, the time complexity is O(n).

Space Complexity:
- The space complexity is O(1) since we only use a few variables to store coefficients and constants.
"""

# Topic: String Parsing