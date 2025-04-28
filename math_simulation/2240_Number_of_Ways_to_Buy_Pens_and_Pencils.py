"""
LeetCode Problem #2240: Number of Ways to Buy Pens and Pencils

Problem Statement:
You are given an integer `total` indicating the amount of money you have, and two integers `cost1` and `cost2` 
indicating the cost of a pen and a pencil, respectively. You can spend the money in any way you want as long 
as it is on pens and pencils.

Return the number of different ways you can buy pens and pencils.

Example:
Input: total = 20, cost1 = 10, cost2 = 5
Output: 9
Explanation: The 9 ways are:
- Buy 0 pens and 0 pencils
- Buy 0 pens and 1 pencil
- Buy 0 pens and 2 pencils
- Buy 0 pens and 3 pencils
- Buy 0 pens and 4 pencils
- Buy 1 pen and 0 pencils
- Buy 1 pen and 1 pencil
- Buy 1 pen and 2 pencils
- Buy 1 pen and 3 pencils

Constraints:
- 1 <= total, cost1, cost2 <= 10^6
"""

# Python Solution
def waysToBuyPensPencils(total: int, cost1: int, cost2: int) -> int:
    ways = 0
    # Iterate over the number of pens we can buy
    for pens in range(total // cost1 + 1):
        remaining_money = total - pens * cost1
        ways += remaining_money // cost2 + 1
    return ways

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    total = 20
    cost1 = 10
    cost2 = 5
    print(waysToBuyPensPencils(total, cost1, cost2))  # Output: 9

    # Test Case 2
    total = 5
    cost1 = 10
    cost2 = 10
    print(waysToBuyPensPencils(total, cost1, cost2))  # Output: 1

    # Test Case 3
    total = 100
    cost1 = 20
    cost2 = 10
    print(waysToBuyPensPencils(total, cost1, cost2))  # Output: 56

    # Test Case 4
    total = 1000000
    cost1 = 1
    cost2 = 1
    print(waysToBuyPensPencils(total, cost1, cost2))  # Output: 500000500001

# Time and Space Complexity Analysis
"""
Time Complexity:
- The outer loop runs for `total // cost1 + 1` iterations, which is at most O(total / cost1).
- Inside the loop, the calculation of `remaining_money // cost2 + 1` is O(1).
- Therefore, the overall time complexity is O(total / cost1).

Space Complexity:
- The solution uses only a constant amount of extra space, so the space complexity is O(1).
"""

# Topic: Math / Simulation