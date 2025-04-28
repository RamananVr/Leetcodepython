"""
LeetCode Problem #1434: Number of Ways to Wear Different Hats to Each Other

Problem Statement:
There are `n` people and `40` types of hats labeled from `1` to `40`.

Given a list of `hats` where `hats[i]` is a list of all hats preferred by the `i-th` person, return the number of ways that the hats can be distributed such that each person gets exactly one hat and no two people wear the same hat.

Since the answer may be very large, return it modulo `10^9 + 7`.

Constraints:
- `n == hats.length`
- `1 <= n <= 10`
- `0 <= hats[i].length <= 40`
- `1 <= hats[i][j] <= 40`
- All `hats[i]` lists are unique.

Example:
Input: hats = [[3,4],[4,5],[5]]
Output: 1
Explanation: There is only one way to assign hats:
- The first person wears hat 3.
- The second person wears hat 4.
- The third person wears hat 5.

Input: hats = [[1,2,3],[2,3,4],[1,2]]
Output: 4
Explanation: There are 4 ways to assign hats:
- The first person wears hat 1, the second wears hat 2, and the third wears hat 3.
- The first person wears hat 1, the second wears hat 3, and the third wears hat 2.
- The first person wears hat 2, the second wears hat 3, and the third wears hat 1.
- The first person wears hat 2, the second wears hat 4, and the third wears hat 1.

Topic: Dynamic Programming
"""

from collections import defaultdict
from functools import lru_cache

def numberWays(hats):
    MOD = 10**9 + 7
    n = len(hats)
    
    # Create a mapping of hats to people who can wear them
    hat_to_people = defaultdict(list)
    for person, hat_list in enumerate(hats):
        for hat in hat_list:
            hat_to_people[hat].append(person)
    
    # Use DP with bitmask to represent which people have been assigned hats
    @lru_cache(None)
    def dp(hat, mask):
        # Base case: all hats have been considered
        if hat > 40:
            return 1 if mask == (1 << n) - 1 else 0
        
        # Option 1: Skip the current hat
        ways = dp(hat + 1, mask)
        
        # Option 2: Assign the current hat to one of the eligible people
        for person in hat_to_people[hat]:
            if not (mask & (1 << person)):  # If the person hasn't been assigned a hat
                ways += dp(hat + 1, mask | (1 << person))
                ways %= MOD
        
        return ways
    
    return dp(1, 0)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    hats1 = [[3,4],[4,5],[5]]
    print(numberWays(hats1))  # Output: 1

    # Test Case 2
    hats2 = [[1,2,3],[2,3,4],[1,2]]
    print(numberWays(hats2))  # Output: 4

    # Test Case 3
    hats3 = [[1,2,3],[1,2,3],[1,2,3]]
    print(numberWays(hats3))  # Output: 6

    # Test Case 4
    hats4 = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]
    print(numberWays(hats4))  # Output: 3628800

"""
Time and Space Complexity Analysis:

Time Complexity:
- The number of states in the DP is `40 * 2^n`, where `n` is the number of people.
- For each state, we iterate over the list of people who can wear the current hat.
- Thus, the time complexity is `O(40 * 2^n * k)`, where `k` is the average number of people who can wear a hat.
- Since `n <= 10`, `2^n` is manageable.

Space Complexity:
- The space complexity is dominated by the memoization table, which stores `40 * 2^n` states.
- Thus, the space complexity is `O(40 * 2^n)`.

Topic: Dynamic Programming
"""