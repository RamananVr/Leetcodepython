"""
LeetCode Problem #2147: Number of Ways to Divide a Long Corridor

Problem Statement:
You are given a string `corridor` of length `n` representing a long corridor in a building, 
where `corridor[i]` is either 'S' (representing a seat) or 'P' (representing a plant). 
One room can be formed by selecting a contiguous segment of the corridor that contains exactly two seats ('S') 
and any number of plants ('P'). 

- A corridor can be divided into multiple non-overlapping rooms.
- You are tasked to determine the number of ways to divide the corridor into rooms such that each room contains exactly two seats.

Return the number of ways to divide the corridor. Since the answer may be large, return it modulo 10^9 + 7.

Constraints:
- `1 <= corridor.length <= 10^5`
- `corridor[i]` is either 'S' or 'P'.

Example 1:
Input: corridor = "SSPSSPSS"
Output: 4
Explanation: There are 4 ways to divide the corridor into rooms:
- "SSP | SSP | SS"
- "SSP | SS | PSS"
- "SS | PSP | SS"
- "SS | PS | PSS"

Example 2:
Input: corridor = "SSPSS"
Output: 2
Explanation: There are 2 ways to divide the corridor into rooms:
- "SSP | SS"
- "SS | PSS"

Example 3:
Input: corridor = "SPPSSSSP"
Output: 0
Explanation: It is impossible to divide the corridor into rooms because there are not enough seats.

"""

# Solution
def numberOfWays(corridor: str) -> int:
    MOD = 10**9 + 7

    # Count the total number of seats
    seat_count = corridor.count('S')
    
    # If the total number of seats is not even or less than 2, return 0
    if seat_count < 2 or seat_count % 2 != 0:
        return 0

    # Find the positions of all seats
    seat_positions = [i for i, c in enumerate(corridor) if c == 'S']
    
    # Calculate the number of ways to divide the corridor
    ways = 1
    for i in range(1, len(seat_positions) // 2):
        # The number of plants between two consecutive pairs of seats
        gap = seat_positions[2 * i] - seat_positions[2 * i - 1]
        ways = (ways * gap) % MOD

    return ways

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    corridor1 = "SSPSSPSS"
    print(numberOfWays(corridor1))  # Output: 4

    # Test Case 2
    corridor2 = "SSPSS"
    print(numberOfWays(corridor2))  # Output: 2

    # Test Case 3
    corridor3 = "SPPSSSSP"
    print(numberOfWays(corridor3))  # Output: 0

    # Test Case 4
    corridor4 = "SSPSSPSSPSS"
    print(numberOfWays(corridor4))  # Output: 16

    # Test Case 5
    corridor5 = "PSSPSSPSSP"
    print(numberOfWays(corridor5))  # Output: 4

"""
Time and Space Complexity Analysis:

Time Complexity:
- Counting the seats takes O(n), where n is the length of the corridor.
- Finding the positions of all seats also takes O(n).
- Calculating the number of ways involves iterating over half the number of seats, which is O(n) in the worst case.
- Overall time complexity: O(n).

Space Complexity:
- The space used to store the positions of the seats is O(k), where k is the number of seats.
- In the worst case, k = n (if all characters are 'S').
- Overall space complexity: O(n).

Topic: Greedy, String
"""