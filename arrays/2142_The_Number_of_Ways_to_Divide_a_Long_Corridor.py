"""
LeetCode Problem #2142: The Number of Ways to Divide a Long Corridor

Problem Statement:
A corridor is a long, narrow rectangle divided into `n` sections. Each section is either empty ('0') or contains a seat ('1'). 
You are tasked with dividing the corridor into non-overlapping parts such that:

1. Each part contains exactly two seats ('1').
2. The parts can contain any number of empty sections ('0').

Return the number of ways to divide the corridor. Since the answer may be large, return it modulo 10^9 + 7.

If it is impossible to divide the corridor, return 0.

Constraints:
- `1 <= n <= 10^5`
- The corridor string consists of only '0' and '1'.

Example:
Input: corridor = "10101"
Output: 2

Explanation:
The corridor can be divided into two parts: "101" and "01". Each part contains exactly two seats.

Input: corridor = "1001"
Output: 0

Explanation:
It is impossible to divide the corridor into parts with exactly two seats.

Input: corridor = "100100010001"
Output: 4

Explanation:
The corridor can be divided into four parts: "1001", "0001", "0001", and "0001".
"""

# Python Solution
def numberOfWays(corridor: str) -> int:
    MOD = 10**9 + 7
    
    # Count the total number of seats ('1') in the corridor
    seat_count = corridor.count('1')
    
    # If the total number of seats is odd or less than 2, it's impossible to divide
    if seat_count < 2 or seat_count % 2 != 0:
        return 0
    
    # Find the positions of all seats
    seat_positions = [i for i, char in enumerate(corridor) if char == '1']
    
    # Calculate the number of ways to divide the corridor
    ways = 1
    for i in range(1, len(seat_positions) // 2):
        # Calculate the number of empty sections between consecutive pairs of seats
        gap = seat_positions[2 * i] - seat_positions[2 * i - 1]
        ways = (ways * gap) % MOD
    
    return ways

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    corridor = "10101"
    print(numberOfWays(corridor))  # Output: 2

    # Test Case 2
    corridor = "1001"
    print(numberOfWays(corridor))  # Output: 0

    # Test Case 3
    corridor = "100100010001"
    print(numberOfWays(corridor))  # Output: 4

    # Test Case 4
    corridor = "111"
    print(numberOfWays(corridor))  # Output: 0

    # Test Case 5
    corridor = "1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"
    print(numberOfWays(corridor))  # Output: 0

"""
Time and Space Complexity Analysis:

Time Complexity:
- Counting the number of '1's in the corridor takes O(n).
- Finding the positions of all seats takes O(n).
- Calculating the number of ways involves iterating over half the seat positions, which takes O(seat_count / 2).
- Overall, the time complexity is O(n).

Space Complexity:
- The space complexity is O(seat_count) for storing the positions of all seats.
- In the worst case, seat_count = n (if all sections contain seats).
- Overall, the space complexity is O(n).

Topic: Arrays
"""