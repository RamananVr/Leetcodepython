"""
LeetCode Problem #2169: Count Operations to Obtain Zero

Problem Statement:
You are given two non-negative integers `num1` and `num2`.

In one operation, if `num1 >= num2`, you subtract `num2` from `num1`, 
otherwise, you subtract `num1` from `num2`.

Return the number of operations required to make either `num1 = 0` or `num2 = 0`.

Constraints:
- 0 <= num1, num2 <= 10^5
"""

def countOperations(num1: int, num2: int) -> int:
    """
    Function to count the number of operations required to make either num1 or num2 equal to zero.
    """
    operations = 0
    while num1 > 0 and num2 > 0:
        if num1 >= num2:
            num1 -= num2
        else:
            num2 -= num1
        operations += 1
    return operations

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    num1, num2 = 2, 3
    print(f"countOperations({num1}, {num2}) = {countOperations(num1, num2)}")  # Expected: 3

    # Test Case 2
    num1, num2 = 10, 10
    print(f"countOperations({num1}, {num2}) = {countOperations(num1, num2)}")  # Expected: 1

    # Test Case 3
    num1, num2 = 0, 5
    print(f"countOperations({num1}, {num2}) = {countOperations(num1, num2)}")  # Expected: 0

    # Test Case 4
    num1, num2 = 7, 3
    print(f"countOperations({num1}, {num2}) = {countOperations(num1, num2)}")  # Expected: 5

    # Test Case 5
    num1, num2 = 100, 25
    print(f"countOperations({num1}, {num2}) = {countOperations(num1, num2)}")  # Expected: 4

"""
Time Complexity Analysis:
- In each operation, the larger of the two numbers is reduced by the smaller number.
- This is similar to the Euclidean algorithm for finding the greatest common divisor (GCD), 
  which has a time complexity of O(log(min(num1, num2))).
- Therefore, the time complexity of this solution is O(log(min(num1, num2))).

Space Complexity Analysis:
- The solution uses a constant amount of extra space (only a few variables).
- Therefore, the space complexity is O(1).

Topic: Math, Simulation
"""