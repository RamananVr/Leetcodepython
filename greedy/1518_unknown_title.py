"""
LeetCode Problem #1518: Water Bottles

Problem Statement:
Given two integers `numBottles` and `numExchange`. The first integer `numBottles` represents the number of full water bottles you initially have. The second integer `numExchange` represents the number of empty bottles required to exchange for one full bottle.

You can drink a full bottle of water, after which it becomes an empty bottle. You can exchange the empty bottles for full bottles as long as you have at least `numExchange` empty bottles.

Return the maximum number of water bottles you can drink.

Example 1:
Input: numBottles = 9, numExchange = 3
Output: 13
Explanation: You start with 9 bottles. After drinking them, you have 9 empty bottles. You exchange 9 empty bottles for 3 full bottles. After drinking those, you have 3 empty bottles. You exchange 3 empty bottles for 1 full bottle. After drinking that, you have 1 empty bottle left. You cannot exchange it anymore. Total bottles drunk: 9 + 3 + 1 = 13.

Example 2:
Input: numBottles = 15, numExchange = 4
Output: 19
Explanation: You start with 15 bottles. After drinking them, you have 15 empty bottles. You exchange 12 empty bottles for 3 full bottles. After drinking those, you have 3 empty bottles. You cannot exchange them anymore. Total bottles drunk: 15 + 3 + 1 = 19.

Constraints:
- 1 <= numBottles <= 100
- 2 <= numExchange <= 100
"""

def numWaterBottles(numBottles: int, numExchange: int) -> int:
    """
    Calculate the maximum number of water bottles you can drink given the initial number of bottles
    and the exchange rate for empty bottles.
    """
    total_drunk = 0
    empty_bottles = 0

    while numBottles > 0:
        # Drink all current full bottles
        total_drunk += numBottles
        empty_bottles += numBottles

        # Exchange empty bottles for new full bottles
        numBottles = empty_bottles // numExchange
        empty_bottles %= numExchange

    return total_drunk

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    numBottles = 9
    numExchange = 3
    print(numWaterBottles(numBottles, numExchange))  # Output: 13

    # Test Case 2
    numBottles = 15
    numExchange = 4
    print(numWaterBottles(numBottles, numExchange))  # Output: 19

    # Test Case 3
    numBottles = 5
    numExchange = 5
    print(numWaterBottles(numBottles, numExchange))  # Output: 6

    # Test Case 4
    numBottles = 1
    numExchange = 2
    print(numWaterBottles(numBottles, numExchange))  # Output: 1

"""
Time and Space Complexity Analysis:

Time Complexity:
- The while loop runs as long as `numBottles > 0`. In each iteration, the number of bottles decreases significantly
  (by a factor of `numExchange`), so the loop runs in O(log(numBottles)) time.

Space Complexity:
- The solution uses a constant amount of space (O(1)) since no additional data structures are used.

Topic: Greedy
"""