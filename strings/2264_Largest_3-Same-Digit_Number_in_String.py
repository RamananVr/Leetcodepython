"""
LeetCode Problem #2264: Largest 3-Same-Digit Number in String

Problem Statement:
You are given a string `num` representing a large integer. Return the largest 3-digit number that is a substring of `num` and consists of the same digit. If no such substring exists, return an empty string.

Example:
Input: num = "6777133339"
Output: "777"
Explanation: There are two substrings with 3 same digits: "777" and "333". The largest is "777".

Constraints:
- 3 <= num.length <= 1000
- num consists of only digits.
"""

# Python Solution
def largest_good_integer(num: str) -> str:
    largest = ""
    for i in range(len(num) - 2):
        # Check if the current substring is a 3-same-digit number
        if num[i] == num[i + 1] == num[i + 2]:
            largest = max(largest, num[i:i + 3])
    return largest

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    num1 = "6777133339"
    print(largest_good_integer(num1))  # Output: "777"

    # Test Case 2
    num2 = "2300019"
    print(largest_good_integer(num2))  # Output: "000"

    # Test Case 3
    num3 = "42352338"
    print(largest_good_integer(num3))  # Output: ""

    # Test Case 4
    num4 = "111222333444"
    print(largest_good_integer(num4))  # Output: "444"

    # Test Case 5
    num5 = "999999999"
    print(largest_good_integer(num5))  # Output: "999"

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function iterates through the string `num` with a sliding window of size 3.
- The loop runs for `len(num) - 2` iterations, where `len(num)` is the length of the input string.
- Each iteration performs constant-time operations (comparison and slicing).
- Therefore, the time complexity is O(n), where n is the length of the string.

Space Complexity:
- The function uses a single variable `largest` to store the result, which requires O(1) space.
- No additional data structures are used.
- Therefore, the space complexity is O(1).

Topic: Strings
"""