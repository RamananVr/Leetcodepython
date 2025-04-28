"""
LeetCode Problem #121: Best Time to Buy and Sell Stock

Problem Statement:
You are given an array `prices` where `prices[i]` is the price of a given stock on the i-th day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Constraints:
- 1 <= prices.length <= 10^5
- 0 <= prices[i] <= 10^4
"""

def maxProfit(prices):
    """
    Function to calculate the maximum profit from buying and selling a stock.

    :param prices: List[int] - List of stock prices
    :return: int - Maximum profit achievable
    """
    # Initialize variables
    min_price = float('inf')  # Minimum price seen so far
    max_profit = 0            # Maximum profit seen so far

    # Iterate through the prices
    for price in prices:
        # Update the minimum price
        min_price = min(min_price, price)
        # Calculate the profit if sold at the current price
        profit = price - min_price
        # Update the maximum profit
        max_profit = max(max_profit, profit)

    return max_profit

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Standard case with profit
    prices1 = [7, 1, 5, 3, 6, 4]
    print(maxProfit(prices1))  # Expected Output: 5 (Buy at 1, Sell at 6)

    # Test Case 2: No profit possible
    prices2 = [7, 6, 4, 3, 1]
    print(maxProfit(prices2))  # Expected Output: 0 (No transaction is done)

    # Test Case 3: Single day (no transaction possible)
    prices3 = [5]
    print(maxProfit(prices3))  # Expected Output: 0 (No transaction is done)

    # Test Case 4: Increasing prices
    prices4 = [1, 2, 3, 4, 5]
    print(maxProfit(prices4))  # Expected Output: 4 (Buy at 1, Sell at 5)

    # Test Case 5: Decreasing prices
    prices5 = [5, 4, 3, 2, 1]
    print(maxProfit(prices5))  # Expected Output: 0 (No transaction is done)

"""
Time Complexity Analysis:
- The algorithm iterates through the `prices` array once, performing constant-time operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the `prices` array.

Space Complexity Analysis:
- The algorithm uses a constant amount of extra space (variables `min_price` and `max_profit`).
- Therefore, the space complexity is O(1).

Topic: Arrays
"""