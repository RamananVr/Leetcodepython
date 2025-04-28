"""
LeetCode Problem #1006: Clumsy Factorial

Problem Statement:
The factorial of a positive integer n is the product of all positive integers less than or equal to n. 
For example, factorial(10) = 10 * 9 * 8 * ... * 1.

However, we sometimes use a "clumsy" factorial instead. In this variant, the integers are put into 
groups of four in reverse order, and each group is evaluated in the following way:
- The first number is multiplied by the second number.
- The result is divided by the third number (integer division).
- The fourth number is added to the result.

For example, clumsy(10) is calculated as:
- 10 * 9 / 8 + 7
- 6 * 5 / 4 + 3
- 2 * 1

Note that the division is integer division, so 10 * 9 / 8 equals 11. This process continues until 
there are no more numbers left.

Given an integer n, return the clumsy factorial of n.

Constraints:
- 1 <= n <= 10^4
"""

def clumsy(n: int) -> int:
    """
    Calculate the clumsy factorial of a given integer n.
    """
    # Initialize result and a stack to simulate the operations
    stack = []
    # Define the operations in order: multiplication, division, addition, subtraction
    operations = ['*', '//', '+', '-']
    index = 0  # To cycle through operations
    
    # Iterate through numbers from n down to 1
    for i in range(n, 0, -1):
        if not stack:
            # Push the first number onto the stack
            stack.append(i)
        else:
            # Perform the operation based on the current index
            op = operations[index % 4]
            if op == '*':
                stack[-1] *= i
            elif op == '//':
                stack[-1] //= i
            elif op == '+':
                stack.append(i)
            elif op == '-':
                stack.append(-i)
            index += 1
    
    # Sum up all the values in the stack to get the result
    return sum(stack)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Small input
    print(clumsy(4))  # Expected output: 7 (4 * 3 // 2 + 1)
    
    # Test Case 2: Larger input
    print(clumsy(10))  # Expected output: 12 (10 * 9 // 8 + 7 - 6 * 5 // 4 + 3 - 2 * 1)
    
    # Test Case 3: Edge case (minimum input)
    print(clumsy(1))  # Expected output: 1
    
    # Test Case 4: Edge case (small input)
    print(clumsy(2))  # Expected output: 2 (2 * 1)
    
    # Test Case 5: Edge case (small input)
    print(clumsy(3))  # Expected output: 6 (3 * 2 // 1)

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through the numbers from n down to 1, performing constant-time operations 
  (multiplication, division, addition, subtraction) for each number. Thus, the time complexity is O(n).

Space Complexity:
- The algorithm uses a stack to store intermediate results. In the worst case, the stack will contain 
  all n numbers, so the space complexity is O(n).

Topic: Math, Simulation
"""