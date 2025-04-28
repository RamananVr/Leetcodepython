"""
LeetCode Problem #2885: Minimum Sum of Four Digit Number After Splitting Digits

Problem Statement:
You are given a positive integer `num` consisting of exactly four digits. Split the digits of `num` into two new integers `num1` and `num2` such that:
- All the digits of `num` are used to form `num1` and `num2`.
- Each integer can contain any number of digits.
- Leading zeros are allowed in `num1` and `num2`, and they are still considered valid integers.

Return the minimum possible sum of `num1` and `num2`.

Example:
Input: num = 2932
Output: 52
Explanation: Split num into [2, 9] and [3, 2]. num1 = 29 and num2 = 23, so the sum is 29 + 23 = 52.

Constraints:
- 1000 <= num <= 9999
"""

# Solution
def minimumSum(num: int) -> int:
    # Convert the number into a sorted list of its digits
    digits = sorted([int(d) for d in str(num)])
    
    # Form two numbers by interleaving the sorted digits
    num1 = digits[0] * 10 + digits[2]
    num2 = digits[1] * 10 + digits[3]
    
    # Return the sum of the two numbers
    return num1 + num2

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    num = 2932
    print(f"Input: {num}, Output: {minimumSum(num)}")  # Expected Output: 52

    # Test Case 2
    num = 4009
    print(f"Input: {num}, Output: {minimumSum(num)}")  # Expected Output: 13

    # Test Case 3
    num = 1234
    print(f"Input: {num}, Output: {minimumSum(num)}")  # Expected Output: 37

    # Test Case 4
    num = 9876
    print(f"Input: {num}, Output: {minimumSum(num)}")  # Expected Output: 165

# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting the digits takes O(4 * log(4)) = O(1) since the number of digits is fixed at 4.
- Forming the two numbers and calculating their sum takes O(1).
- Overall time complexity: O(1).

Space Complexity:
- The space required to store the digits is O(4) = O(1).
- Overall space complexity: O(1).
"""

# Topic: Arrays, Greedy