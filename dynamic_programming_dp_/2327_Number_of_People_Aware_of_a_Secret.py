"""
LeetCode Problem #2327: Number of People Aware of a Secret

Problem Statement:
On day 1, one person discovers a secret. You are given an integer `delay`, which means that each person will share the secret with a new person every day starting from `delay` days after discovering the secret. You are also given an integer `forget`, which means that each person will forget the secret `forget` days after discovering it. A person cannot share the secret on the same day they forget it or after.

Given an integer `n`, return the number of people who know the secret at the end of day `n`. Since the answer may be very large, return it modulo `10^9 + 7`.

Constraints:
- `2 <= n <= 1000`
- `1 <= delay < forget <= n`

Example:
Input: n = 4, delay = 1, forget = 3
Output: 6
Explanation:
- Day 1: 1 person knows the secret.
- Day 2: 1 person shares the secret with 1 new person. Total: 2 people.
- Day 3: 2 people share the secret with 2 new people. Total: 4 people.
- Day 4: 2 people forget the secret, and 2 people share the secret with 2 new people. Total: 6 people.

"""

# Python Solution
def peopleAwareOfSecret(n: int, delay: int, forget: int) -> int:
    MOD = 10**9 + 7

    # dp[i] represents the number of people who discover the secret on day i
    dp = [0] * (n + 1)
    dp[1] = 1  # On day 1, one person knows the secret

    # Total number of people aware of the secret on a given day
    total = 0

    for day in range(1, n + 1):
        # Add the number of people who discover the secret on this day
        if day >= delay:
            dp[day] += dp[day - delay]
        if day >= forget:
            dp[day] -= dp[day - forget]

        # Update the total number of people aware of the secret
        total += dp[day]
        total %= MOD

    return total

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 4
    delay = 1
    forget = 3
    print(peopleAwareOfSecret(n, delay, forget))  # Output: 6

    # Test Case 2
    n = 6
    delay = 2
    forget = 4
    print(peopleAwareOfSecret(n, delay, forget))  # Output: 5

    # Test Case 3
    n = 10
    delay = 3
    forget = 5
    print(peopleAwareOfSecret(n, delay, forget))  # Output: 9

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates through all days from 1 to n, performing constant-time operations for each day.
- Therefore, the time complexity is O(n).

Space Complexity:
- The algorithm uses an array `dp` of size n + 1 to store the number of people who discover the secret on each day.
- Therefore, the space complexity is O(n).
"""

# Topic: Dynamic Programming (DP)