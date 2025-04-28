"""
LeetCode Problem #902: Numbers At Most N Given Digit Set

Problem Statement:
Given an array of `digits` which is a sorted array of unique digits (each digit is a string), and an integer `n`, 
return the number of positive integers that can be generated that are less than or equal to `n` using only digits 
from the given `digits`.

Example:
Input: digits = ["1", "3", "5", "7"], n = 100
Output: 20
Explanation:
The 20 numbers that can be written are:
1, 3, 5, 7, 11, 13, 15, 17, 31, 33, 35, 37, 51, 53, 55, 57, 71, 73, 75, 77.

Constraints:
1. 1 <= digits.length <= 9
2. digits[i].length == 1
3. digits[i] is a digit from '1' to '9'.
4. All the values in digits are unique.
5. digits is sorted in non-decreasing order.
6. 1 <= n <= 10^9
"""

def atMostNGivenDigitSet(digits, n):
    """
    Function to calculate the number of positive integers less than or equal to n
    that can be formed using the given digit set.

    :param digits: List[str] - A sorted list of unique digits as strings.
    :param n: int - The upper limit for the numbers to be formed.
    :return: int - The count of numbers that can be formed.
    """
    n_str = str(n)
    n_len = len(n_str)
    digits_len = len(digits)
    
    # Count numbers with fewer digits than n
    count = 0
    for i in range(1, n_len):
        count += digits_len ** i

    # Count numbers with the same number of digits as n
    for i in range(n_len):
        has_same_prefix = False
        for digit in digits:
            if digit < n_str[i]:
                count += digits_len ** (n_len - i - 1)
            elif digit == n_str[i]:
                has_same_prefix = True
                break
        if not has_same_prefix:
            return count

    # Include n itself if all its digits are in the digit set
    return count + 1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    digits = ["1", "3", "5", "7"]
    n = 100
    print(atMostNGivenDigitSet(digits, n))  # Output: 20

    # Test Case 2
    digits = ["1", "4", "9"]
    n = 1000000000
    print(atMostNGivenDigitSet(digits, n))  # Output: 29523

    # Test Case 3
    digits = ["7"]
    n = 8
    print(atMostNGivenDigitSet(digits, n))  # Output: 1

    # Test Case 4
    digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    n = 123
    print(atMostNGivenDigitSet(digits, n))  # Output: 123

"""
Time Complexity:
- Let `d` be the length of the `digits` array and `L` be the number of digits in `n`.
- Calculating numbers with fewer digits than `n` takes O(L).
- For each digit in `n`, we iterate over the `digits` array, which takes O(L * d).
- Overall time complexity: O(L * d).

Space Complexity:
- The space complexity is O(L) due to the string representation of `n`.

Topic: Dynamic Programming, Combinatorics
"""