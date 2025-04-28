"""
LeetCode Problem #1323: Maximum 69 Number

Problem Statement:
You are given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

Example 1:
Input: num = 9669
Output: 9969
Explanation:
Changing the first digit results in 9969.
Changing the second digit results in 9969.
Changing the third digit results in 9699.
Changing the fourth digit results in 9666.
The maximum number is 9969.

Example 2:
Input: num = 9996
Output: 9999
Explanation:
Changing the last digit 6 to 9 results in 9999.

Example 3:
Input: num = 9999
Output: 9999
Explanation:
There is no 6 in the number, so no change is needed.

Constraints:
- 1 <= num <= 10^4
- num consists of only the digits 6 and 9.
"""

# Solution
def maximum69Number(num: int) -> int:
    """
    This function takes an integer num consisting of digits 6 and 9,
    and returns the maximum number obtainable by changing at most one digit.
    """
    # Convert the number to a string to manipulate digits
    num_str = str(num)
    
    # Replace the first occurrence of '6' with '9'
    max_num_str = num_str.replace('6', '9', 1)
    
    # Convert back to integer and return
    return int(max_num_str)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    num1 = 9669
    print(f"Input: {num1}, Output: {maximum69Number(num1)}")  # Expected Output: 9969

    # Test Case 2
    num2 = 9996
    print(f"Input: {num2}, Output: {maximum69Number(num2)}")  # Expected Output: 9999

    # Test Case 3
    num3 = 9999
    print(f"Input: {num3}, Output: {maximum69Number(num3)}")  # Expected Output: 9999

    # Test Case 4
    num4 = 6
    print(f"Input: {num4}, Output: {maximum69Number(num4)}")  # Expected Output: 9

    # Test Case 5
    num5 = 69
    print(f"Input: {num5}, Output: {maximum69Number(num5)}")  # Expected Output: 99

# Time and Space Complexity Analysis
"""
Time Complexity:
- Converting the integer to a string takes O(d), where d is the number of digits in num.
- Replacing the first occurrence of '6' with '9' takes O(d) in the worst case.
- Converting the string back to an integer takes O(d).
- Overall, the time complexity is O(d), where d is the number of digits in num.

Space Complexity:
- The space complexity is O(d) due to the string representation of the number.
- No additional data structures are used, so the space complexity is O(d).
"""

# Topic: Strings