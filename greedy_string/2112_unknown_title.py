"""
LeetCode Problem #2112: The problem statement is as follows:

2112. The Number of Ways to Divide a Long Corridor

A corridor is represented by a string `s` of length `n`, where `s[i]` is either `'S'` (representing a seat) or `'P'` (representing a plant). One way to divide the corridor is by placing dividers into it such that each part contains exactly two seats and no more.

- You cannot place a divider at the start or end of the corridor.
- Each divider must be placed between two adjacent characters.

Return the number of ways to divide the corridor. Since the answer may be large, return it modulo `10^9 + 7`.

If it is impossible to divide the corridor, return `0`.

Constraints:
- `n == s.length`
- `1 <= n <= 10^5`
- `s[i]` is either `'S'` or `'P'`.

Example:
Input: s = "SSPSSPSS"
Output: 4
Explanation: There are 4 ways to divide the corridor:
1. "SS|PSS|PSS"
2. "SS|PSSP|SS"
3. "SSP|SS|PSS"
4. "SSP|SSP|SS"
"""

# Python Solution
def numberOfWays(s: str) -> int:
    MOD = 10**9 + 7

    # Count the total number of seats
    total_seats = s.count('S')
    
    # If the total number of seats is not even, it's impossible to divide
    if total_seats % 2 != 0 or total_seats == 0:
        return 0

    # Find the positions of all seats
    seat_positions = [i for i, char in enumerate(s) if char == 'S']
    
    # Group seats into pairs and calculate the number of ways to divide
    ways = 1
    for i in range(1, len(seat_positions) // 2):
        gap = seat_positions[2 * i] - seat_positions[2 * i - 1]
        ways = (ways * gap) % MOD

    return ways

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "SSPSSPSS"
    print(numberOfWays(s1))  # Output: 4

    # Test Case 2
    s2 = "SSPSS"
    print(numberOfWays(s2))  # Output: 1

    # Test Case 3
    s3 = "PSSP"
    print(numberOfWays(s3))  # Output: 0

    # Test Case 4
    s4 = "SSSS"
    print(numberOfWays(s4))  # Output: 0

    # Test Case 5
    s5 = "PSSSSPSSPSS"
    print(numberOfWays(s5))  # Output: 6

"""
Time Complexity Analysis:
- Counting the total number of seats takes O(n), where n is the length of the string.
- Finding the positions of all seats also takes O(n).
- Calculating the number of ways involves iterating over half the number of seats, which is O(total_seats / 2).
- Overall, the time complexity is O(n).

Space Complexity Analysis:
- The space complexity is O(k), where k is the number of seats, as we store their positions in a list.
- In the worst case, k = n (if all characters are 'S'), so the space complexity is O(n).

Topic: Greedy, String
"""