"""
LeetCode Question #585: Investments in 2016

Problem Statement:
Suppose you have a table `StockPrices` with the following schema:

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| stock_id      | int     |
| year          | int     |
| price         | int     |
+---------------+---------+

(stock_id, year) is the primary key for this table.
Write an SQL query to find the stock_id with the highest price in 2016. If there is a tie, return the smallest stock_id.

The query result format is in the following example:

StockPrices table:
+----------+------+-------+
| stock_id | year | price |
+----------+------+-------+
| 1        | 2015 | 10    |
| 1        | 2016 | 20    |
| 2        | 2016 | 20    |
| 3        | 2016 | 30    |
+----------+------+-------+

Result table:
+----------+
| stock_id |
+----------+
| 3        |
+----------+

Explanation:
In 2016, the stock prices are:
- stock_id 1: 20
- stock_id 2: 20
- stock_id 3: 30
The highest price is 30, and the stock_id with that price is 3.
"""

# Python Solution
def find_highest_stock_id(prices):
    """
    Function to find the stock_id with the highest price in 2016.
    If there is a tie, return the smallest stock_id.

    :param prices: List of tuples representing stock_id, year, and price.
    :return: The stock_id with the highest price in 2016.
    """
    # Filter for the year 2016
    filtered_prices = [price for price in prices if price[1] == 2016]
    
    # Find the maximum price in 2016
    max_price = max(filtered_prices, key=lambda x: x[2])[2]
    
    # Find all stock_ids with the maximum price
    max_price_stocks = [price[0] for price in filtered_prices if price[2] == max_price]
    
    # Return the smallest stock_id among those with the maximum price
    return min(max_price_stocks)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    prices = [
        (1, 2015, 10),
        (1, 2016, 20),
        (2, 2016, 20),
        (3, 2016, 30)
    ]
    print(find_highest_stock_id(prices))  # Expected Output: 3

    # Test Case 2
    prices = [
        (1, 2016, 50),
        (2, 2016, 50),
        (3, 2016, 40)
    ]
    print(find_highest_stock_id(prices))  # Expected Output: 1

    # Test Case 3
    prices = [
        (1, 2015, 10),
        (2, 2015, 20),
        (3, 2016, 30),
        (4, 2016, 30),
        (5, 2016, 30)
    ]
    print(find_highest_stock_id(prices))  # Expected Output: 3

# Time and Space Complexity Analysis
"""
Time Complexity:
- Filtering the list for the year 2016 takes O(n), where n is the number of entries in the input list.
- Finding the maximum price takes O(m), where m is the number of entries in the filtered list.
- Finding all stock_ids with the maximum price takes O(m).
- Finding the minimum stock_id among those with the maximum price takes O(k), where k is the number of stock_ids with the maximum price.
Overall, the time complexity is O(n + m + k), which simplifies to O(n) in the worst case.

Space Complexity:
- The space complexity is O(m), where m is the size of the filtered list for the year 2016.
- Additional space is used for storing stock_ids with the maximum price, which is O(k).
Overall, the space complexity is O(m + k), which simplifies to O(n) in the worst case.
"""

# Topic: Arrays