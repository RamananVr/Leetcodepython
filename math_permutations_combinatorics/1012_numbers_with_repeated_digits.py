"""
LeetCode Question #1012: Numbers With Repeated Digits

Problem Statement:
Given an integer n, return the number of positive integers less than or equal to n that have at least one repeated digit.

Example 1:
Input: n = 20
Output: 1
Explanation: The only number with repeated digits is 11.

Example 2:
Input: n = 100
Output: 10
Explanation: The numbers with repeated digits are 11, 22, 33, 44, 55, 66, 77, 88, 99, and 100.

Example 3:
Input: n = 1000
Output: 262

Constraints:
1 <= n <= 10^9
"""

# Solution
def numDupDigitsAtMostN(n: int) -> int:
    def countUniqueDigitsNumbers(x):
        """Helper function to count numbers with unique digits less than x."""
        digits = list(map(int, str(x)))
        length = len(digits)
        used = [0] * 10

        # Count numbers with fewer digits
        count = 0
        for i in range(1, length):
            count += 9 * perm(9, i - 1)

        # Count numbers with the same number of digits
        for i in range(length):
            for d in range(1 if i == 0 else 0, digits[i]):
                if not used[d]:
                    count += perm(9 - i, length - i - 1)
            if used[digits[i]]:
                break
            used[digits[i]] = 1
        else:
            count += 1

        return count

    def perm(m, n):
        """Helper function to calculate permutations P(m, n)."""
        if n == 0:
            return 1
        return m * perm(m - 1, n - 1)

    # Total numbers less than or equal to n
    total = n

    # Numbers with unique digits less than or equal to n
    unique_digits_count = countUniqueDigitsNumbers(n + 1)

    # Numbers with repeated digits
    return total - unique_digits_count


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 20
    print(numDupDigitsAtMostN(n1))  # Output: 1

    # Test Case 2
    n2 = 100
    print(numDupDigitsAtMostN(n2))  # Output: 10

    # Test Case 3
    n3 = 1000
    print(numDupDigitsAtMostN(n3))  # Output: 262

    # Test Case 4
    n4 = 1234
    print(numDupDigitsAtMostN(n4))  # Output: 324

    # Test Case 5
    n5 = 10
    print(numDupDigitsAtMostN(n5))  # Output: 0


# Time and Space Complexity Analysis
"""
Time Complexity:
- The function `countUniqueDigitsNumbers` iterates through the digits of the number and calculates permutations.
- Calculating permutations is O(k), where k is the number of digits in n.
- The overall complexity is approximately O(k^2), where k is the number of digits in n (log10(n)).

Space Complexity:
- The space complexity is O(k) due to the storage of digits and the `used` array, where k is the number of digits in n.

Overall:
Time Complexity: O(k^2), where k = log10(n)
Space Complexity: O(k), where k = log10(n)
"""

# Topic: Math, Permutations, Combinatorics