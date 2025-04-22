"""
LeetCode Problem #544: Output Contest Matches

Problem Statement:
During a contest, there are `n` teams numbered from 1 to `n`. The contest consists of rounds where teams compete in pairs, and winners advance to the next round. In the first round, the 1st team competes against the `n`th team, the 2nd team competes against the `(n-1)`th team, and so on. Each round continues until there is only one winner.

You are given an integer `n`, where `n` is a power of 2 (e.g., 2, 4, 8, 16). Write a function to return a string representing the contest matches in the format:
- In the first round, the matches are represented as `(1,n),(2,n-1),...,(n/2,n/2+1)`.
- In the second round, the winners of the first round are paired in the same format.
- Continue until there is only one winner.

Example:
Input: n = 8
Output: "(((1,8),(4,5)),((2,7),(3,6)))"

Constraints:
- `n` is a power of 2.
- `1 <= n <= 2^10`
"""

# Solution
def findContestMatch(n: int) -> str:
    # Initialize the list of teams as strings
    teams = [str(i) for i in range(1, n + 1)]
    
    # While there are more than one team, pair them up
    while len(teams) > 1:
        new_round = []
        for i in range(len(teams) // 2):
            new_round.append(f"({teams[i]},{teams[-(i + 1)]})")
        teams = new_round
    
    # The final result is the single remaining match
    return teams[0]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 8
    print(findContestMatch(n))  # Expected Output: "(((1,8),(4,5)),((2,7),(3,6)))"

    # Test Case 2
    n = 4
    print(findContestMatch(n))  # Expected Output: "((1,4),(2,3))"

    # Test Case 3
    n = 2
    print(findContestMatch(n))  # Expected Output: "(1,2)"

# Time and Space Complexity Analysis
"""
Time Complexity:
- The number of rounds is log2(n), as the number of teams halves in each round.
- In each round, we iterate over all remaining teams to pair them, which takes O(n) in the first round, O(n/2) in the second round, and so on.
- The total work done is proportional to n + n/2 + n/4 + ... + 1, which is a geometric series summing to O(n).
- Therefore, the time complexity is O(n).

Space Complexity:
- The space complexity is dominated by the storage of the `teams` list, which initially contains `n` elements and reduces in size each round.
- The space complexity is O(n).
"""

# Topic: Strings, Simulation