"""
LeetCode Problem #1997: First Day Where You Have Been in All the Rooms

Problem Statement:
There are `n` rooms you need to visit, labeled from `0` to `n - 1`. Each day, you visit exactly one room. 
You start in room `0` on day `0`. You cannot visit the same room two days in a row.

You are given a 0-indexed integer array `nextVisit` of length `n` where `nextVisit[i]` indicates that if 
you visit room `i` on some day, you must visit room `nextVisit[i]` on the next day.

Return the first day where you have been in all the rooms. Since the answer may be very large, return it modulo `10^9 + 7`.

Constraints:
- `2 <= n <= 10^5`
- `0 <= nextVisit[i] <= i`

Example:
Input: nextVisit = [0,0,2]
Output: 6
Explanation:
- On day 0, you visit room 0. The next room you visit will be room nextVisit[0] = 0.
- On day 1, you visit room 0 again. The next room you visit will be room nextVisit[0] = 0.
- On day 2, you visit room 0 again. The next room you visit will be room nextVisit[0] = 0.
- On day 3, you visit room 1. The next room you visit will be room nextVisit[1] = 0.
- On day 4, you visit room 0 again. The next room you visit will be room nextVisit[0] = 0.
- On day 5, you visit room 2. The next room you visit will be room nextVisit[2] = 2.
- On day 6, you visit room 2 again. This is the first day where you have been in all the rooms.

Topic: Dynamic Programming
"""

# Python Solution
def firstDayBeenInAllRooms(nextVisit):
    MOD = 10**9 + 7
    n = len(nextVisit)
    dp = [0] * n  # dp[i] represents the first day you can leave room i after visiting it

    for i in range(1, n):
        dp[i] = (dp[i - 1] + 1 + (dp[i - 1] - dp[nextVisit[i]] + 1) % MOD) % MOD

    return dp[-1]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nextVisit = [0, 0, 2]
    print(firstDayBeenInAllRooms(nextVisit))  # Output: 6

    # Test Case 2
    nextVisit = [0, 0, 1, 2]
    print(firstDayBeenInAllRooms(nextVisit))  # Output: 8

    # Test Case 3
    nextVisit = [0, 0]
    print(firstDayBeenInAllRooms(nextVisit))  # Output: 2

"""
Time Complexity:
- The solution iterates through the `nextVisit` array once, performing constant-time operations for each room.
- Therefore, the time complexity is O(n), where n is the number of rooms.

Space Complexity:
- The solution uses an array `dp` of size n to store intermediate results.
- Therefore, the space complexity is O(n).

Topic: Dynamic Programming
"""