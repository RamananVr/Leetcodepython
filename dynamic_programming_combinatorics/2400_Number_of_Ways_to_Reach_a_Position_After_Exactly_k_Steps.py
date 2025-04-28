"""
LeetCode Problem #2400: Number of Ways to Reach a Position After Exactly k Steps

Problem Statement:
You are given two integers `startPos` and `endPos` representing the starting and ending positions on an infinite number line. 
You are also given a positive integer `k`.

Return the number of ways to reach the position `endPos` starting from `startPos` after exactly `k` steps. 
Each step, you can either move one position to the left or one position to the right.

Since the answer may be very large, return it modulo 10^9 + 7.

Example 1:
Input: startPos = 1, endPos = 2, k = 3
Output: 3
Explanation: We can reach position 2 from position 1 in exactly 3 steps in three ways:
- 1 -> 2 -> 1 -> 2.
- 1 -> 0 -> 1 -> 2.
- 1 -> 2 -> 3 -> 2.

Example 2:
Input: startPos = 2, endPos = 5, k = 10
Output: 0
Explanation: It is impossible to reach position 5 from position 2 in exactly 10 steps.

Constraints:
- -10^3 <= startPos, endPos <= 10^3
- 1 <= k <= 1000
"""

# Solution
def numberOfWays(startPos: int, endPos: int, k: int) -> int:
    MOD = 10**9 + 7

    # Calculate the distance between startPos and endPos
    distance = abs(endPos - startPos)

    # If the distance is greater than k or (k - distance) is odd, return 0
    if distance > k or (k - distance) % 2 != 0:
        return 0

    # Calculate the number of steps to the right and left
    right_steps = (k + distance) // 2
    left_steps = k - right_steps

    # Helper function to calculate nCr % MOD
    def nCr(n, r):
        if r > n or r < 0:
            return 0
        num = 1
        den = 1
        for i in range(r):
            num = num * (n - i) % MOD
            den = den * (i + 1) % MOD
        return num * pow(den, MOD - 2, MOD) % MOD

    # Return the number of ways using nCr
    return nCr(k, right_steps)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    startPos = 1
    endPos = 2
    k = 3
    print(numberOfWays(startPos, endPos, k))  # Output: 3

    # Test Case 2
    startPos = 2
    endPos = 5
    k = 10
    print(numberOfWays(startPos, endPos, k))  # Output: 0

    # Test Case 3
    startPos = 0
    endPos = 0
    k = 4
    print(numberOfWays(startPos, endPos, k))  # Output: 6

    # Test Case 4
    startPos = 3
    endPos = 3
    k = 2
    print(numberOfWays(startPos, endPos, k))  # Output: 2

# Time and Space Complexity Analysis
"""
Time Complexity:
- Calculating nCr involves iterating up to r (or k/2 in the worst case), so the time complexity is O(k).
- Thus, the overall time complexity is O(k).

Space Complexity:
- The space complexity is O(1) since we are using a constant amount of extra space.

Topic: Dynamic Programming, Combinatorics
"""