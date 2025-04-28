"""
LeetCode Problem #728: Self Dividing Numbers

Problem Statement:
A self-dividing number is a number that is divisible by every digit it contains.

- For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

A self-dividing number cannot contain the digit zero.

Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right].

Constraints:
- 1 <= left <= right <= 10^4
"""

def selfDividingNumbers(left: int, right: int) -> list[int]:
    def is_self_dividing(num: int) -> bool:
        """
        Helper function to check if a number is self-dividing.
        """
        original = num
        while num > 0:
            digit = num % 10
            if digit == 0 or original % digit != 0:
                return False
            num //= 10
        return True

    result = []
    for num in range(left, right + 1):
        if is_self_dividing(num):
            result.append(num)
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    left = 1
    right = 22
    print(f"Self-dividing numbers between {left} and {right}: {selfDividingNumbers(left, right)}")
    # Expected Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

    # Test Case 2
    left = 47
    right = 85
    print(f"Self-dividing numbers between {left} and {right}: {selfDividingNumbers(left, right)}")
    # Expected Output: [48, 55, 66, 77]

    # Test Case 3
    left = 10
    right = 15
    print(f"Self-dividing numbers between {left} and {right}: {selfDividingNumbers(left, right)}")
    # Expected Output: [11, 12, 15]

"""
Time Complexity:
- The outer loop iterates over all numbers in the range [left, right], so it runs O(right - left + 1) times.
- For each number, the helper function `is_self_dividing` processes all digits of the number. In the worst case, a number has log10(n) digits.
- Therefore, the overall time complexity is O((right - left + 1) * log10(n)), where n is the largest number in the range.

Space Complexity:
- The space complexity is O(1) because we are using a constant amount of extra space.

Topic: Math
"""