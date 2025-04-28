"""
LeetCode Problem #2283: Check if Number Has Equal Digit Count and Digit Value

Problem Statement:
You are given a 0-indexed string num of length n consisting of digits.

Return true if for every index i in the range 0 <= i < n, the digit i occurs num[i] times in num, otherwise return false.

Example 1:
Input: num = "1210"
Output: true
Explanation:
- The digit 0 occurs 1 time in num.
- The digit 1 occurs 2 times in num.
- The digit 2 occurs 1 time in num.
- The digit 3 occurs 0 times in num.
Thus, num is valid.

Example 2:
Input: num = "030"
Output: false
Explanation:
- The digit 0 occurs 1 time in num.
- The digit 1 occurs 0 times in num.
- The digit 2 occurs 0 times in num.
- The digit 3 occurs 1 time in num.
Thus, num is not valid since num[0] != 1.

Constraints:
- n == num.length
- 1 <= n <= 10
- num consists of digits.

"""

def digitCount(num: str) -> bool:
    """
    Function to check if the number has equal digit count and digit value.

    Args:
    num (str): A string representing the number.

    Returns:
    bool: True if the condition is satisfied, False otherwise.
    """
    for i in range(len(num)):
        # Count the occurrences of digit `i` in the string
        count = num.count(str(i))
        # Check if the count matches the value at index `i`
        if count != int(num[i]):
            return False
    return True

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    num1 = "1210"
    print(digitCount(num1))  # Output: True

    # Test Case 2
    num2 = "030"
    print(digitCount(num2))  # Output: False

    # Test Case 3
    num3 = "2020"
    print(digitCount(num3))  # Output: True

    # Test Case 4
    num4 = "3211000"
    print(digitCount(num4))  # Output: True

    # Test Case 5
    num5 = "12345"
    print(digitCount(num5))  # Output: False

"""
Time Complexity Analysis:
- The `count` method is called for each digit in the string `num`.
- The `count` method itself has a time complexity of O(n), where n is the length of the string.
- Since we iterate over the string of length n and call `count` for each digit, the overall time complexity is O(n^2).

Space Complexity Analysis:
- The space complexity is O(1) as we are not using any additional data structures that scale with the input size.

Topic: Strings
"""