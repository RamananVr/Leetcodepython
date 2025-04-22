"""
LeetCode Question #123: Best Time to Buy and Sell Stock III

Problem Statement:
You are given an array `prices` where `prices[i]` is the price of a given stock on the `i`th day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Constraints:
- 1 <= prices.length <= 10^5
- 0 <= prices[i] <= 10^5
"""

def maxProfit(prices):
    """
    This function calculates the maximum profit that can be achieved with at most two transactions.
    """
    if not prices or len(prices) < 2:
        return 0

    # Initialize variables to track the maximum profit
    first_buy, first_sell = float('-inf'), 0
    second_buy, second_sell = float('-inf'), 0

    for price in prices:
        # Update the profits for the first transaction
        first_buy = max(first_buy, -price)  # Max profit after buying the first stock
        first_sell = max(first_sell, first_buy + price)  # Max profit after selling the first stock

        # Update the profits for the second transaction
        second_buy = max(second_buy, first_sell - price)  # Max profit after buying the second stock
        second_sell = max(second_sell, second_buy + price)  # Max profit after selling the second stock

    return second_sell


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    prices1 = [3,3,5,0,0,3,1,4]
    print(maxProfit(prices1))  # Expected Output: 6

    # Test Case 2
    prices2 = [1,2,3,4,5]
    print(maxProfit(prices2))  # Expected Output: 4

    # Test Case 3
    prices3 = [7,6,4,3,1]
    print(maxProfit(prices3))  # Expected Output: 0

    # Test Case 4
    prices4 = [1]
    print(maxProfit(prices4))  # Expected Output: 0

    # Test Case 5
    prices5 = [1,2,4,2,5,7,2,4,9,0]
    print(maxProfit(prices5))  # Expected Output: 13


"""
Time Complexity Analysis:
- The algorithm iterates through the `prices` array once, performing constant-time operations for each price.
- Therefore, the time complexity is O(n), where n is the length of the `prices` array.

Space Complexity Analysis:
- The algorithm uses a constant amount of extra space to store variables (`first_buy`, `first_sell`, `second_buy`, `second_sell`).
- Therefore, the space complexity is O(1).

Topic: Dynamic Programming (DP)
"""