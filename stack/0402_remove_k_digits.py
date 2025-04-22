"""
LeetCode Question #402: Remove K Digits

Problem Statement:
Given a string num representing a non-negative integer and an integer k, 
remove k digits from the number so that the new number is the smallest possible.

Note:
- The result should not contain any leading zeroes.
- If the result is an empty string, return "0".

Constraints:
- 1 <= num.length <= 10^5
- num consists of only digits.
- 0 <= k <= num.length

Example 1:
Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the smallest number "1219".

Example 2:
Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the digit 1 to form the smallest number "200".
Note that the result must not contain leading zeros.

Example 3:
Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and the result is "0".
"""

# Python Solution
def removeKdigits(num: str, k: int) -> str:
    stack = []
    
    # Iterate through each digit in the number
    for digit in num:
        # Remove digits from the stack if they are greater than the current digit
        # and we still need to remove more digits (k > 0)
        while stack and k > 0 and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    
    # Remove remaining digits from the end if k > 0
    while k > 0:
        stack.pop()
        k -= 1
    
    # Build the result and remove leading zeros
    result = ''.join(stack).lstrip('0')
    
    # Return "0" if the result is empty
    return result if result else "0"

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    num1 = "1432219"
    k1 = 3
    print(removeKdigits(num1, k1))  # Output: "1219"

    # Test Case 2
    num2 = "10200"
    k2 = 1
    print(removeKdigits(num2, k2))  # Output: "200"

    # Test Case 3
    num3 = "10"
    k3 = 2
    print(removeKdigits(num3, k3))  # Output: "0"

    # Test Case 4
    num4 = "1234567890"
    k4 = 9
    print(removeKdigits(num4, k4))  # Output: "0"

    # Test Case 5
    num5 = "7654321"
    k5 = 3
    print(removeKdigits(num5, k5))  # Output: "4321"

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through the digits of the input string `num` once, which takes O(n) time.
- Additionally, the stack operations (push and pop) are O(1) each, and in the worst case, we perform O(n) stack operations.
- Therefore, the overall time complexity is O(n), where n is the length of the input string `num`.

Space Complexity:
- The space complexity is O(n) due to the stack used to store the digits.
- In the worst case, the stack can contain all the digits of the input string.

Topic: Stack
"""