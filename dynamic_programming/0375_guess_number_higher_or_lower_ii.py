"""
LeetCode Question #375: Guess Number Higher or Lower II

Problem Statement:
We are playing the Guessing Game. The game will work as follows:

1. I pick a number between 1 and n.
2. You guess a number.
3. If you guess the right number, you win the game.
4. If you guess wrong, I will tell you whether the number I picked is higher or lower, and you will continue guessing.
5. Every time you guess a wrong number, you pay the price equal to the number you guessed.

Given a particular n, return the minimum amount of money you need to guarantee a win, regardless of what number I pick.

Constraints:
- 1 <= n <= 200

Example:
Input: n = 10
Output: 16
Explanation: The winning strategy is as follows:
- The range is [1, 10]. Guess 7.
    - If the number is lower, the range is [1, 6]. Guess 3.
        - If the number is lower, the range is [1, 2]. Guess 1. If wrong, guess 2. Total cost = 7 + 3 + 1 = 11.
        - If the number is higher, the range is [4, 6]. Guess 5. If wrong, guess 6. Total cost = 7 + 3 + 5 = 15.
    - If the number is higher, the range is [8, 10]. Guess 9.
        - If the number is lower, the range is [8, 8]. Guess 8. Total cost = 7 + 9 = 16.
        - If the number is higher, the range is [10, 10]. Guess 10. Total cost = 7 + 9 = 16.
The minimum amount of money required to guarantee a win is 16.
"""

# Solution
def getMoneyAmount(n: int) -> int:
    # Create a DP table where dp[i][j] represents the minimum cost to guarantee a win in the range [i, j].
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # Fill the DP table
    for length in range(2, n + 1):  # length of the range
        for start in range(1, n - length + 2):  # start of the range
            end = start + length - 1  # end of the range
            dp[start][end] = float('inf')
            for pivot in range(start, end):
                # Cost of choosing 'pivot' as the guess
                cost = pivot + max(dp[start][pivot - 1], dp[pivot + 1][end])
                dp[start][end] = min(dp[start][end], cost)

    return dp[1][n]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 10
    print(f"Minimum cost to guarantee a win for n = {n}: {getMoneyAmount(n)}")  # Expected Output: 16

    # Test Case 2
    n = 1
    print(f"Minimum cost to guarantee a win for n = {n}: {getMoneyAmount(n)}")  # Expected Output: 0

    # Test Case 3
    n = 2
    print(f"Minimum cost to guarantee a win for n = {n}: {getMoneyAmount(n)}")  # Expected Output: 1

    # Test Case 4
    n = 5
    print(f"Minimum cost to guarantee a win for n = {n}: {getMoneyAmount(n)}")  # Expected Output: 6

"""
Time Complexity Analysis:
- The outer loop iterates over all possible lengths of ranges, which is O(n).
- The second loop iterates over all possible starting points of ranges, which is also O(n).
- The innermost loop iterates over all possible pivot points within a range, which is O(n) in the worst case.
- Therefore, the overall time complexity is O(n^3).

Space Complexity Analysis:
- The DP table requires O(n^2) space to store the minimum costs for all ranges.

Topic: Dynamic Programming
"""