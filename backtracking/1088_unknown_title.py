"""
LeetCode Problem #1088: Confusing Number II

Problem Statement:
A confusing number is a number that when rotated 180 degrees becomes a different number with each digit valid. 
We can rotate digits of a number by 180 degrees to form new digits. When 0, 1, 6, 8, and 9 are rotated 180 degrees, 
they become 0, 1, 9, 8, and 6 respectively. A confusing number cannot have invalid digits like 2, 3, 4, 5, or 7.

Given an integer n, return the total number of confusing numbers between 1 and n inclusive.

Example 1:
Input: n = 20
Output: 6
Explanation: The confusing numbers are [6, 9, 10, 16, 18, 19].

Example 2:
Input: n = 100
Output: 19

Constraints:
- 1 <= n <= 10^9
"""

# Solution
class Solution:
    def confusingNumberII(self, n: int) -> int:
        # Valid digits and their rotated counterparts
        valid_digits = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
        self.result = 0

        def is_confusing(num: int) -> bool:
            """Check if a number is confusing."""
            original = num
            rotated = 0
            while num > 0:
                digit = num % 10
                if digit not in valid_digits:
                    return False
                rotated = rotated * 10 + valid_digits[digit]
                num //= 10
            return rotated != original

        def dfs(current: int):
            """Perform DFS to generate numbers and check if they are confusing."""
            if current > n:
                return
            if current != 0 and is_confusing(current):
                self.result += 1
            for digit in valid_digits.keys():
                next_num = current * 10 + digit
                if next_num != 0:  # Avoid leading zeros
                    dfs(next_num)

        # Start DFS with an initial number of 0
        dfs(0)
        return self.result


# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    n1 = 20
    print(f"Confusing numbers count for n = {n1}: {solution.confusingNumberII(n1)}")  # Output: 6

    # Test Case 2
    n2 = 100
    print(f"Confusing numbers count for n = {n2}: {solution.confusingNumberII(n2)}")  # Output: 19

    # Test Case 3
    n3 = 50
    print(f"Confusing numbers count for n = {n3}: {solution.confusingNumberII(n3)}")  # Output: 12

    # Test Case 4
    n4 = 1
    print(f"Confusing numbers count for n = {n4}: {solution.confusingNumberII(n4)}")  # Output: 0

    # Test Case 5
    n5 = 10
    print(f"Confusing numbers count for n = {n5}: {solution.confusingNumberII(n5)}")  # Output: 2


# Time and Space Complexity Analysis
"""
Time Complexity:
- The DFS explores all possible numbers that can be formed using the valid digits (0, 1, 6, 8, 9).
- The number of such numbers is bounded by the number of digits in `n`. For a number with `d` digits, there are at most 5^d numbers.
- Checking if a number is confusing takes O(d), where `d` is the number of digits in the number.
- Therefore, the overall time complexity is O(5^d * d), where `d` is the number of digits in `n`.

Space Complexity:
- The space complexity is O(d) due to the recursion stack in the DFS, where `d` is the number of digits in `n`.
"""

# Topic: Backtracking