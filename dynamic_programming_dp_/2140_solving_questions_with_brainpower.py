"""
LeetCode Question #2140: Solving Questions With Brainpower

Problem Statement:
You are given a 0-indexed 2D integer array `questions` where `questions[i] = [points_i, brainpower_i]`.

The array describes the questions of an exam, where:
- `points_i` is the points you will earn if you solve the `i-th` question.
- `brainpower_i` is the number of questions that you will skip after solving the `i-th` question (including the `i-th` question itself).

- For example, if you solve question `i`, you will earn `points_i` points but you will be unable to solve the next `brainpower_i` questions.

Return the maximum points you can earn for the exam.

Constraints:
1. `1 <= questions.length <= 10^5`
2. `questions[i].length == 2`
3. `1 <= points_i, brainpower_i <= 10^5`
"""

# Solution
from typing import List

def mostPoints(questions: List[List[int]]) -> int:
    n = len(questions)
    dp = [0] * (n + 1)  # dp[i] represents the maximum points we can earn starting from question i

    for i in range(n - 1, -1, -1):
        points, brainpower = questions[i]
        # Option 1: Skip the current question
        skip = dp[i + 1]
        # Option 2: Solve the current question
        solve = points + (dp[i + brainpower + 1] if i + brainpower + 1 < n else 0)
        # Take the maximum of both options
        dp[i] = max(skip, solve)

    return dp[0]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    questions1 = [[3, 2], [4, 3], [4, 4], [2, 5]]
    print(mostPoints(questions1))  # Expected Output: 5

    # Test Case 2
    questions2 = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
    print(mostPoints(questions2))  # Expected Output: 7

    # Test Case 3
    questions3 = [[10, 1], [5, 1], [10, 1]]
    print(mostPoints(questions3))  # Expected Output: 20

    # Test Case 4
    questions4 = [[1, 1]]
    print(mostPoints(questions4))  # Expected Output: 1

    # Test Case 5
    questions5 = [[2, 2], [3, 1], [4, 2], [8, 3], [10, 1]]
    print(mostPoints(questions5))  # Expected Output: 15

"""
Time Complexity Analysis:
- The solution iterates through the `questions` array once in reverse order, performing O(1) operations for each question.
- Therefore, the time complexity is O(n), where n is the number of questions.

Space Complexity Analysis:
- The solution uses a `dp` array of size n + 1 to store intermediate results.
- Therefore, the space complexity is O(n).

Topic: Dynamic Programming (DP)
"""