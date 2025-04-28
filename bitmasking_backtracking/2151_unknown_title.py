"""
LeetCode Problem #2151: Maximum Good People Based on Statements

Problem Statement:
There are n people labeled from 0 to n - 1. You are given a 2D integer array statements where statements[i][j] can be:
- 0 which represents person i says person j is bad,
- 1 which represents person i says person j is good, or
- 2 if person i does not give any statement about person j.

Additionally:
- No person can contradict their own statement.
- If person i is good, then all the statements they make are true.
- If person i is bad, then their statements may be true or false.

Return the maximum number of good people based on the statements made by the n people.

Constraints:
- n == statements.length == statements[i].length
- 2 <= n <= 15
- statements[i][j] is either 0, 1, or 2.

"""

from typing import List

def maximumGood(statements: List[List[int]]) -> int:
    def is_valid(assumption):
        for i in range(n):
            if assumption[i] == 1:  # If person i is assumed to be good
                for j in range(n):
                    if statements[i][j] != 2:  # If there's a statement about person j
                        if statements[i][j] != assumption[j]:
                            return False
        return True

    n = len(statements)
    max_good = 0

    # Iterate through all possible combinations of good/bad people
    for mask in range(1 << n):  # 2^n combinations
        assumption = [(mask >> i) & 1 for i in range(n)]  # Decode mask into binary representation
        if is_valid(assumption):
            max_good = max(max_good, sum(assumption))  # Count the number of good people in this assumption

    return max_good

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    statements1 = [
        [2, 1, 2],
        [1, 2, 2],
        [2, 0, 2]
    ]
    print(maximumGood(statements1))  # Output: 2

    # Test Case 2
    statements2 = [
        [2, 0],
        [0, 2]
    ]
    print(maximumGood(statements2))  # Output: 1

    # Test Case 3
    statements3 = [
        [2, 2, 2],
        [2, 2, 2],
        [2, 2, 2]
    ]
    print(maximumGood(statements3))  # Output: 3

"""
Time Complexity:
- There are 2^n possible combinations of good/bad people (since each person can either be good or bad).
- For each combination, we validate the assumption, which takes O(n^2) time (to check all statements).
- Therefore, the overall time complexity is O(2^n * n^2).

Space Complexity:
- The space complexity is O(n) for storing the assumption array.

Topic: Bitmasking, Backtracking
"""