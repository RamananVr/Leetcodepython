"""
LeetCode Problem #2160: Minimum Sum of Four Digit Number After Splitting Digits

Problem Statement:
You are given a positive integer num consisting of exactly four digits. Split num into two new integers new1 and new2 by using the digits of num. 
The number new1 and new2 can have different lengths. Return the minimum possible sum of new1 and new2.

Note:
- Each digit of num must be used exactly once when forming new1 and new2.
- new1 and new2 may not contain leading zeros unless the number itself is 0.

Example:
Input: num = 2932
Output: 52
Explanation: Split num into new1 = 29 and new2 = 23, then the sum is 29 + 23 = 52.

Constraints:
- 1000 <= num <= 9999
"""

# Solution
def minimumSum(num: int) -> int:
    # Convert the number into a sorted list of its digits
    digits = sorted([int(d) for d in str(num)])
    
    # Form two numbers by pairing the smallest digits
    new1 = digits[0] * 10 + digits[2]
    new2 = digits[1] * 10 + digits[3]
    
    # Return the sum of the two numbers
    return new1 + new2

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    num = 2932
    print(minimumSum(num))  # Output: 52

    # Test Case 2
    num = 4009
    print(minimumSum(num))  # Output: 13

    # Test Case 3
    num = 1234
    print(minimumSum(num))  # Output: 37

    # Test Case 4
    num = 9876
    print(minimumSum(num))  # Output: 165

# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting the digits takes O(4 * log(4)) = O(1) since the number has exactly 4 digits.
- Forming the two numbers and calculating their sum takes O(1).
- Overall, the time complexity is O(1).

Space Complexity:
- The space used to store the digits array is O(4) = O(1).
- Overall, the space complexity is O(1).
"""

# Topic: Arrays