"""
LeetCode Problem #967: Numbers With Same Consecutive Differences

Problem Statement:
Return all non-negative integers of length `n` such that the absolute difference 
between every two consecutive digits is `k`.

Note that every number in the answer must not have leading zeros. For example, 
01 has one leading zero and is invalid.

You may return the answer in any order.

Example 1:
Input: n = 3, k = 7
Output: [181, 292, 707, 818, 929]

Example 2:
Input: n = 2, k = 1
Output: [10, 12, 21, 23, 32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 89, 98]

Constraints:
- 2 <= n <= 9
- 0 <= k <= 9
"""

# Solution
from typing import List

def numsSameConsecDiff(n: int, k: int) -> List[int]:
    def dfs(num: int, length: int):
        # Base case: if the number has reached the desired length
        if length == n:
            result.append(num)
            return
        
        last_digit = num % 10
        # Try adding or subtracting k to the last digit
        next_digits = set([last_digit + k, last_digit - k])
        for next_digit in next_digits:
            if 0 <= next_digit <= 9:  # Ensure the next digit is valid
                dfs(num * 10 + next_digit, length + 1)
    
    result = []
    # Start DFS for each digit from 1 to 9 (no leading zeros allowed)
    for start_digit in range(1, 10):
        dfs(start_digit, 1)
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 3
    k = 7
    print(numsSameConsecDiff(n, k))  # Output: [181, 292, 707, 818, 929]

    # Test Case 2
    n = 2
    k = 1
    print(numsSameConsecDiff(n, k))  # Output: [10, 12, 21, 23, 32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 89, 98]

    # Test Case 3
    n = 2
    k = 0
    print(numsSameConsecDiff(n, k))  # Output: [11, 22, 33, 44, 55, 66, 77, 88, 99]

# Time and Space Complexity Analysis
"""
Time Complexity:
- The DFS explores all possible numbers of length `n` starting from digits 1 to 9.
- For each digit, there are at most 2 choices (adding or subtracting `k`).
- Therefore, the total number of recursive calls is approximately O(2^n).
- Since we start from 9 digits, the overall complexity is O(9 * 2^n).

Space Complexity:
- The space complexity is determined by the recursion stack, which can go up to `n` levels deep.
- Additionally, we store the result list, which can contain up to O(9 * 2^n) numbers.
- Therefore, the space complexity is O(n + 9 * 2^n).
"""

# Topic: Backtracking