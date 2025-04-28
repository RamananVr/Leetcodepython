"""
LeetCode Problem #2165: Smallest Value of the Rearranged Number

Problem Statement:
You are given an integer `num`. Rearrange the digits of `num` such that its value is minimized and it does not contain any leading zeros.

- If `num` is positive, rearrange its digits to form the smallest possible number.
- If `num` is negative, rearrange its digits to form the largest possible negative number.

Return the rearranged number with the same sign as `num`.

Constraints:
- -10^15 <= num <= 10^15

Example 1:
Input: num = 310
Output: 103

Example 2:
Input: num = -7605
Output: -7650

Example 3:
Input: num = 0
Output: 0
"""

def smallestNumber(num: int) -> int:
    """
    Rearranges the digits of the given number to form the smallest possible value
    while maintaining the sign of the number.
    """
    if num == 0:
        return 0

    # Handle positive numbers
    if num > 0:
        # Sort digits in ascending order
        digits = sorted(str(num))
        # Ensure no leading zeros by moving the first non-zero digit to the front
        if digits[0] == '0':
            for i in range(len(digits)):
                if digits[i] != '0':
                    digits[0], digits[i] = digits[i], '0'
                    break
        return int("".join(digits))

    # Handle negative numbers
    else:
        # Sort digits in descending order
        digits = sorted(str(-num), reverse=True)
        return -int("".join(digits))


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Positive number
    num1 = 310
    print(smallestNumber(num1))  # Output: 103

    # Test Case 2: Negative number
    num2 = -7605
    print(smallestNumber(num2))  # Output: -7650

    # Test Case 3: Zero
    num3 = 0
    print(smallestNumber(num3))  # Output: 0

    # Test Case 4: Positive number with leading zeros
    num4 = 1020
    print(smallestNumber(num4))  # Output: 1002

    # Test Case 5: Negative number with repeated digits
    num5 = -9001
    print(smallestNumber(num5))  # Output: -9100


"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - Sorting the digits of the number takes O(n log n), where n is the number of digits in `num`.
   - Rearranging the digits (e.g., swapping to avoid leading zeros) takes O(n).
   - Overall time complexity: O(n log n).

2. Space Complexity:
   - The space required to store the digits of the number is O(n), where n is the number of digits in `num`.
   - Overall space complexity: O(n).

Topic: Sorting
"""