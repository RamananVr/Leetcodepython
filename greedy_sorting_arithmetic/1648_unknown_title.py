"""
LeetCode Problem #1648: Sell Diminishing-Valued Colored Balls

Problem Statement:
You have an inventory of different colored balls, and there is a customer that wants orders of colored balls. 
The customer can order as many colored balls as they want, but you can only sell the balls in a diminishing order 
(i.e., you must sell the highest-valued ball first). If you sell a ball of value `v`, then the next ball you sell 
of the same color will have a value of `v-1`. The value of a ball cannot be less than 1.

You are given an integer array `inventory`, where `inventory[i]` represents the number of balls of the `i-th` color 
that you initially own. You are also given an integer `orders`, which represents the total number of balls that the 
customer wants. You need to maximize the total value you can obtain from selling the balls.

Return the maximum total value you can achieve modulo `10^9 + 7`.

Constraints:
- `1 <= inventory.length <= 10^5`
- `1 <= inventory[i] <= 10^9`
- `1 <= orders <= min(sum(inventory), 10^9)`
"""

from typing import List

def maxProfit(inventory: List[int], orders: int) -> int:
    MOD = 10**9 + 7

    # Helper function to calculate the sum of arithmetic series
    def sum_of_arithmetic_series(start, end, count):
        return count * (start + end) // 2

    # Sort inventory in descending order
    inventory.sort(reverse=True)
    inventory.append(0)  # Add a sentinel value to handle the last group

    max_profit = 0
    for i in range(len(inventory) - 1):
        current = inventory[i]
        next_value = inventory[i + 1]
        count = (i + 1)  # Number of colors at this level

        # Calculate how many balls we can sell at this level
        if (current - next_value) * count <= orders:
            # Sell all balls from current to next_value
            max_profit += sum_of_arithmetic_series(current, next_value + 1, current - next_value) * count
            orders -= (current - next_value) * count
        else:
            # Sell only a portion of the balls
            full_rows = orders // count
            remainder = orders % count
            max_profit += sum_of_arithmetic_series(current, current - full_rows + 1, full_rows) * count
            max_profit += (current - full_rows) * remainder
            orders = 0
            break

        max_profit %= MOD

    return max_profit % MOD

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    inventory = [2, 5]
    orders = 4
    print(maxProfit(inventory, orders))  # Expected Output: 14

    # Test Case 2
    inventory = [3, 5]
    orders = 6
    print(maxProfit(inventory, orders))  # Expected Output: 19

    # Test Case 3
    inventory = [2, 8, 4, 10, 6]
    orders = 20
    print(maxProfit(inventory, orders))  # Expected Output: 110

    # Test Case 4
    inventory = [1000000000]
    orders = 1000000000
    print(maxProfit(inventory, orders))  # Expected Output: 21

"""
Time Complexity:
- Sorting the inventory takes O(n log n), where n is the length of the inventory array.
- The loop iterates through the inventory array, and for each level, we perform constant-time arithmetic operations.
  Thus, the loop runs in O(n).
- Overall time complexity: O(n log n).

Space Complexity:
- The algorithm uses O(1) additional space apart from the input array.
- Overall space complexity: O(1).

Topic: Greedy, Sorting, Arithmetic
"""