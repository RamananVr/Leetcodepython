"""
LeetCode Problem #2180: Count Integers With Even Digit Sum

Problem Statement:
Given a positive integer `num`, return the number of positive integers less than or equal to `num` whose digit sums are even.

The digit sum of a number is the sum of all its digits.

Example 1:
Input: num = 4
Output: 2
Explanation:
The only integers less than or equal to 4 whose digit sums are even are 2 and 4.

Example 2:
Input: num = 30
Output: 14
Explanation:
The integers less than or equal to 30 whose digit sums are even are:
2, 4, 6, 8, 11, 13, 15, 17, 19, 20, 22, 24, 26, and 28.

Constraints:
- 1 <= num <= 1000
"""

def countEven(num: int) -> int:
    """
    Function to count integers less than or equal to `num` whose digit sums are even.
    """
    def digit_sum(n: int) -> int:
        """Helper function to calculate the sum of digits of a number."""
        return sum(int(digit) for digit in str(n))
    
    count = 0
    for i in range(1, num + 1):
        if digit_sum(i) % 2 == 0:
            count += 1
    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    num1 = 4
    print(f"Input: {num1}, Output: {countEven(num1)}")  # Expected Output: 2

    # Test Case 2
    num2 = 30
    print(f"Input: {num2}, Output: {countEven(num2)}")  # Expected Output: 14

    # Test Case 3
    num3 = 1
    print(f"Input: {num3}, Output: {countEven(num3)}")  # Expected Output: 0

    # Test Case 4
    num4 = 1000
    print(f"Input: {num4}, Output: {countEven(num4)}")  # Expected Output: 499

"""
Time Complexity Analysis:
- The function iterates through all integers from 1 to `num`, so the loop runs `num` times.
- For each number, the `digit_sum` function is called, which converts the number to a string and sums its digits.
- The time complexity of summing the digits of a number is proportional to the number of digits, which is O(log10(n)).
- Therefore, the overall time complexity is O(num * log10(num)).

Space Complexity Analysis:
- The space complexity is O(log10(n)) for the string representation of the number in the `digit_sum` function.
- No additional data structures are used, so the overall space complexity is O(log10(num)).

Topic: Math
"""