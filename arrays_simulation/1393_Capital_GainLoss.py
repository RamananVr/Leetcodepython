"""
LeetCode Problem #1393: Capital Gain/Loss

Problem Statement:
You are given a list of transactions where transactions[i] = [stock, price, quantity] indicates that you bought or sold 
quantity shares of stock at price per share. A positive quantity indicates a buy transaction, and a negative quantity 
indicates a sell transaction.

Write a function to calculate the total capital gain or loss from the transactions. Capital gain or loss is defined as 
the difference between the selling price and the cost price of the shares sold.

Example:
Input: transactions = [["AAPL", 100, 10], ["AAPL", 120, -5], ["AAPL", 110, -5]]
Output: 50
Explanation:
- First transaction: Bought 10 shares of AAPL at $100 each.
- Second transaction: Sold 5 shares of AAPL at $120 each. Gain = (120 - 100) * 5 = 100.
- Third transaction: Sold 5 shares of AAPL at $110 each. Gain = (110 - 100) * 5 = 50.
Total gain = 100 + 50 = 150.

Constraints:
- The transactions list will contain at most 10^4 transactions.
- Each transaction will have a valid stock name, price, and quantity.
- The quantity will be an integer, and the price will be a positive integer.
"""

# Solution
def calculateCapitalGainLoss(transactions):
    """
    Calculate the total capital gain or loss from the given transactions.

    :param transactions: List[List[str, int, int]] - List of transactions where each transaction is represented as
                          [stock, price, quantity].
    :return: int - Total capital gain or loss.
    """
    stock_data = {}
    total_gain_loss = 0

    for stock, price, quantity in transactions:
        if stock not in stock_data:
            stock_data[stock] = []

        if quantity > 0:  # Buy transaction
            stock_data[stock].append((price, quantity))
        else:  # Sell transaction
            sell_quantity = -quantity
            while sell_quantity > 0:
                buy_price, buy_quantity = stock_data[stock][0]
                if buy_quantity <= sell_quantity:
                    # Sell all shares from this buy transaction
                    total_gain_loss += (price - buy_price) * buy_quantity
                    sell_quantity -= buy_quantity
                    stock_data[stock].pop(0)
                else:
                    # Sell part of the shares from this buy transaction
                    total_gain_loss += (price - buy_price) * sell_quantity
                    stock_data[stock][0] = (buy_price, buy_quantity - sell_quantity)
                    sell_quantity = 0

    return total_gain_loss

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    transactions1 = [["AAPL", 100, 10], ["AAPL", 120, -5], ["AAPL", 110, -5]]
    print(calculateCapitalGainLoss(transactions1))  # Output: 150

    # Test Case 2
    transactions2 = [["GOOG", 200, 20], ["GOOG", 250, -10], ["GOOG", 220, -10]]
    print(calculateCapitalGainLoss(transactions2))  # Output: 700

    # Test Case 3
    transactions3 = [["MSFT", 50, 5], ["MSFT", 60, -3], ["MSFT", 70, -2]]
    print(calculateCapitalGainLoss(transactions3))  # Output: 70

    # Test Case 4
    transactions4 = [["TSLA", 300, 15], ["TSLA", 350, -10], ["TSLA", 400, -5]]
    print(calculateCapitalGainLoss(transactions4))  # Output: 1250

    # Test Case 5
    transactions5 = [["NFLX", 500, 10], ["NFLX", 600, -5], ["NFLX", 550, -5]]
    print(calculateCapitalGainLoss(transactions5))  # Output: 500

# Time and Space Complexity Analysis
"""
Time Complexity:
- Each transaction is processed once, and for sell transactions, we may iterate through the buy transactions for the stock.
- In the worst case, we iterate through all buy transactions for a stock, which is O(n) for n transactions.
- Overall time complexity: O(n), where n is the number of transactions.

Space Complexity:
- We store buy transactions for each stock in a dictionary. In the worst case, we store all transactions in memory.
- Space complexity: O(n), where n is the number of transactions.
"""

# Topic: Arrays, Simulation