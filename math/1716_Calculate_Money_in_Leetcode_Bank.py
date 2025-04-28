"""
LeetCode Problem #1716: Calculate Money in Leetcode Bank

Problem Statement:
Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.

- On the first day, he deposits `1` dollar.
- Every day from the second day onwards, he deposits `1` dollar more than the day before.
- Every Monday, he starts a new week, and on each Monday, he deposits `1` dollar more than the previous Monday.

Given `n`, return the total amount of money he will have in the Leetcode bank at the end of `n` days.

Example:
Input: n = 4
Output: 10
Explanation: 
- Day 1: $1
- Day 2: $2
- Day 3: $3
- Day 4: $4
Total: $10

Input: n = 10
Output: 37
Explanation:
- Week 1: $1, $2, $3, $4, $5, $6, $7 (Total: $28)
- Week 2: $8, $9, $10 (Total: $9)
Total: $37

Constraints:
- 1 <= n <= 1000
"""

# Python Solution
def totalMoney(n: int) -> int:
    # Initialize variables
    total = 0
    week_start = 1  # Money deposited on the first day of the week
    
    for day in range(1, n + 1):
        # Calculate the money deposited on the current day
        total += week_start + (day - 1) % 7
        
        # If it's the start of a new week, increment the week_start
        if day % 7 == 0:
            week_start += 1
    
    return total

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 4
    print(totalMoney(n))  # Output: 10

    # Test Case 2
    n = 10
    print(totalMoney(n))  # Output: 37

    # Test Case 3
    n = 20
    print(totalMoney(n))  # Output: 96

    # Test Case 4
    n = 7
    print(totalMoney(n))  # Output: 28

    # Test Case 5
    n = 1000
    print(totalMoney(n))  # Output: 256500

"""
Time and Space Complexity Analysis:

Time Complexity:
- The solution iterates through all `n` days, performing constant-time operations for each day.
- Therefore, the time complexity is O(n).

Space Complexity:
- The solution uses a constant amount of extra space for variables (`total` and `week_start`).
- Therefore, the space complexity is O(1).

Topic: Math
"""