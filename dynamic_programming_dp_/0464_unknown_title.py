"""
LeetCode Problem #464: Can I Win

Problem Statement:
In the "100 game," two players take turns adding, to a running total, any integer from 1 to maxChoosableInteger. 
The player who first causes the running total to reach or exceed the desiredTotal wins.

What if we change the game so that players cannot re-use integers?

You are given two integers, maxChoosableInteger and desiredTotal. Return true if the first player to move can 
force a win, assuming both players play optimally. Otherwise, return false.

You can always assume that maxChoosableInteger will not be larger than 20 and desiredTotal will not be larger 
than 300.

Example:
Input: maxChoosableInteger = 10, desiredTotal = 11
Output: false

Constraints:
- 1 <= maxChoosableInteger <= 20
- 0 <= desiredTotal <= 300
"""

# Solution
from functools import lru_cache

def canIWin(maxChoosableInteger: int, desiredTotal: int) -> bool:
    # If the sum of all numbers is less than the desiredTotal, no one can win
    if sum(range(1, maxChoosableInteger + 1)) < desiredTotal:
        return False
    
    # Use memoization to store results of subproblems
    @lru_cache(None)
    def helper(used_numbers: int, current_total: int) -> bool:
        for i in range(maxChoosableInteger):
            # Check if the i-th number is already used
            if not (used_numbers & (1 << i)):
                # If choosing this number causes the current player to win
                if current_total + i + 1 >= desiredTotal:
                    return True
                # Otherwise, check if the opponent loses in the next turn
                if not helper(used_numbers | (1 << i), current_total + i + 1):
                    return True
        return False
    
    return helper(0, 0)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    maxChoosableInteger = 10
    desiredTotal = 11
    print(canIWin(maxChoosableInteger, desiredTotal))  # Output: False

    # Test Case 2
    maxChoosableInteger = 10
    desiredTotal = 0
    print(canIWin(maxChoosableInteger, desiredTotal))  # Output: True

    # Test Case 3
    maxChoosableInteger = 10
    desiredTotal = 1
    print(canIWin(maxChoosableInteger, desiredTotal))  # Output: True

    # Test Case 4
    maxChoosableInteger = 5
    desiredTotal = 15
    print(canIWin(maxChoosableInteger, desiredTotal))  # Output: False

# Time and Space Complexity Analysis
"""
Time Complexity:
- The number of states is bounded by 2^maxChoosableInteger (since we use a bitmask to represent used numbers).
- For each state, we iterate over maxChoosableInteger numbers.
- Therefore, the time complexity is O(2^maxChoosableInteger * maxChoosableInteger).

Space Complexity:
- The space complexity is O(2^maxChoosableInteger) due to the memoization cache.
- Additionally, the recursion stack can go up to O(maxChoosableInteger) depth.
- Overall space complexity is O(2^maxChoosableInteger).
"""

# Topic: Dynamic Programming (DP)