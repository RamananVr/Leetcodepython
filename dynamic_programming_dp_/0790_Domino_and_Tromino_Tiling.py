"""
LeetCode Problem #790: Domino and Tromino Tiling

Problem Statement:
You have two types of tiles: a 2x1 domino and a tromino. A tromino is a shape consisting of three 1x1 squares joined together.

You may rotate these shapes. Given an integer n, return the number of ways to tile an 2 x n board. Since the answer may be very large, return it modulo 10^9 + 7.

In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 1x1 squares in different positions that are covered by different types of tiles.

Example 1:
Input: n = 3
Output: 5
Explanation: The five different ways are:
1. Three vertical dominoes.
2. Two vertical dominoes, and one horizontal domino.
3. Two horizontal dominoes, and one vertical domino.
4. One tromino (L-shape), and one vertical domino.
5. One tromino (rotated L-shape), and one vertical domino.

Example 2:
Input: n = 1
Output: 1

Constraints:
1 <= n <= 1000
"""

# Python Solution
def numTilings(n: int) -> int:
    MOD = 10**9 + 7
    
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    # Initialize dp arrays
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2
    
    # Additional array for handling tromino configurations
    dp_tromino = [0] * (n + 1)
    dp_tromino[2] = 1
    
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2] + 2 * dp_tromino[i - 1]) % MOD
        dp_tromino[i] = (dp_tromino[i - 1] + dp[i - 2]) % MOD
    
    return dp[n]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 3
    print(numTilings(n1))  # Output: 5

    # Test Case 2
    n2 = 1
    print(numTilings(n2))  # Output: 1

    # Test Case 3
    n3 = 4
    print(numTilings(n3))  # Output: 11

    # Test Case 4
    n4 = 5
    print(numTilings(n4))  # Output: 24

"""
Time and Space Complexity Analysis:

Time Complexity:
The solution uses a single loop to compute the values for dp and dp_tromino arrays up to n. 
Thus, the time complexity is O(n).

Space Complexity:
The solution uses two arrays, dp and dp_tromino, each of size n + 1. 
Thus, the space complexity is O(n).

Topic: Dynamic Programming (DP)
"""