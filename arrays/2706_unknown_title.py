"""
LeetCode Problem #2706: Buy Two Chocolates

Problem Statement:
You are given an integer array `prices` representing the prices of various chocolates in a store, and an integer `money` representing the amount of money you have.

Return the maximum amount of money you can have left after buying exactly two chocolates. If there is no way to buy two chocolates, return `money`.

Constraints:
- 2 <= prices.length <= 100
- 1 <= prices[i] <= 100
- 1 <= money <= 100
"""

def buyChocolates(prices, money):
    """
    This function calculates the maximum amount of money left after buying exactly two chocolates.

    :param prices: List[int] - List of chocolate prices
    :param money: int - Total money available
    :return: int - Maximum money left after buying two chocolates, or `money` if not possible
    """
    # Sort the prices to find the two cheapest chocolates
    prices.sort()
    
    # Calculate the cost of the two cheapest chocolates
    cost = prices[0] + prices[1]
    
    # If the cost is within the budget, return the remaining money
    if cost <= money:
        return money - cost
    
    # Otherwise, return the original money (not enough to buy two chocolates)
    return money

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    prices = [1, 2, 3]
    money = 3
    print(buyChocolates(prices, money))  # Output: 0

    # Test Case 2
    prices = [10, 2, 5, 8]
    money = 20
    print(buyChocolates(prices, money))  # Output: 13

    # Test Case 3
    prices = [5, 5, 5]
    money = 5
    print(buyChocolates(prices, money))  # Output: 5

    # Test Case 4
    prices = [1, 1, 1, 1]
    money = 2
    print(buyChocolates(prices, money))  # Output: 0

    # Test Case 5
    prices = [100, 200, 300]
    money = 50
    print(buyChocolates(prices, money))  # Output: 50

"""
Time Complexity Analysis:
- Sorting the `prices` array takes O(n log n), where n is the length of the array.
- Accessing the first two elements of the sorted array and performing arithmetic operations are O(1).
- Overall time complexity: O(n log n).

Space Complexity Analysis:
- The sorting operation is in-place, so no additional space is used apart from the input array.
- Overall space complexity: O(1).

Topic: Arrays
"""