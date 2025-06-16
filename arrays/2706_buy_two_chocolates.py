"""
LeetCode Problem #2706: Buy Two Chocolates

Problem Statement:
You are given an integer array `prices` representing the prices of various chocolates in a store. You are also given a single integer `money`, which represents your initial amount of money.

You must buy exactly two chocolates in such a way that you still have some money left over. That is, if the price of the two chocolates is `x` and `y`, then `x + y < money`.

Return the amount of money you will have leftover after buying the two chocolates. If there is no way to buy two chocolates without ending up with a deficit, return `money`.

Constraints:
- 2 <= prices.length <= 50
- 1 <= prices[i] <= 100
- 1 <= money <= 100
"""

def buyChoco(prices, money):
    """
    Finds the minimum cost to buy two chocolates and returns leftover money.
    
    :param prices: List[int] - Prices of chocolates
    :param money: int - Initial amount of money
    :return: int - Leftover money after buying two chocolates
    """
    # Find the two minimum prices
    prices.sort()
    min_cost = prices[0] + prices[1]
    
    # Check if we can afford the two cheapest chocolates
    if min_cost < money:
        return money - min_cost
    else:
        return money

def buyChocoOptimal(prices, money):
    """
    Optimal solution without sorting - finds two minimum values in one pass.
    
    :param prices: List[int] - Prices of chocolates
    :param money: int - Initial amount of money
    :return: int - Leftover money after buying two chocolates
    """
    # Find the two minimum prices without sorting
    first_min = float('inf')
    second_min = float('inf')
    
    for price in prices:
        if price < first_min:
            second_min = first_min
            first_min = price
        elif price < second_min:
            second_min = price
    
    min_cost = first_min + second_min
    
    # Check if we can afford the two cheapest chocolates
    if min_cost < money:
        return money - min_cost
    else:
        return money

def buyChocoOnePass(prices, money):
    """
    Alternative one-pass solution using different approach.
    
    :param prices: List[int] - Prices of chocolates
    :param money: int - Initial amount of money
    :return: int - Leftover money after buying two chocolates
    """
    if len(prices) < 2:
        return money
    
    # Initialize with first two prices
    min1, min2 = prices[0], prices[1]
    if min1 > min2:
        min1, min2 = min2, min1
    
    # Check remaining prices
    for i in range(2, len(prices)):
        if prices[i] < min1:
            min2 = min1
            min1 = prices[i]
        elif prices[i] < min2:
            min2 = prices[i]
    
    min_cost = min1 + min2
    return money - min_cost if min_cost < money else money

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    prices = [1, 2, 2]
    money = 3
    print(f"prices: {prices}, money: {money}")
    print(f"buyChoco: {buyChoco(prices.copy(), money)}")  # Output: 0
    print(f"buyChocoOptimal: {buyChocoOptimal(prices, money)}")  # Output: 0
    print(f"buyChocoOnePass: {buyChocoOnePass(prices, money)}")  # Output: 0
    print()

    # Test Case 2
    prices = [3, 2, 3]
    money = 3
    print(f"prices: {prices}, money: {money}")
    print(f"buyChoco: {buyChoco(prices.copy(), money)}")  # Output: 3
    print(f"buyChocoOptimal: {buyChocoOptimal(prices, money)}")  # Output: 3
    print(f"buyChocoOnePass: {buyChocoOnePass(prices, money)}")  # Output: 3
    print()

    # Test Case 3
    prices = [1, 2, 3, 4, 5]
    money = 10
    print(f"prices: {prices}, money: {money}")
    print(f"buyChoco: {buyChoco(prices.copy(), money)}")  # Output: 7
    print(f"buyChocoOptimal: {buyChocoOptimal(prices, money)}")  # Output: 7
    print(f"buyChocoOnePass: {buyChocoOnePass(prices, money)}")  # Output: 7
    print()

    # Test Case 4
    prices = [10, 20, 30]
    money = 25
    print(f"prices: {prices}, money: {money}")
    print(f"buyChoco: {buyChoco(prices.copy(), money)}")  # Output: 25
    print(f"buyChocoOptimal: {buyChocoOptimal(prices, money)}")  # Output: 25
    print(f"buyChocoOnePass: {buyChocoOnePass(prices, money)}")  # Output: 25
    print()

    # Test Case 5
    prices = [5, 5, 5, 5]
    money = 15
    print(f"prices: {prices}, money: {money}")
    print(f"buyChoco: {buyChoco(prices.copy(), money)}")  # Output: 5
    print(f"buyChocoOptimal: {buyChocoOptimal(prices, money)}")  # Output: 5
    print(f"buyChocoOnePass: {buyChocoOnePass(prices, money)}")  # Output: 5

    # Validation
    assert buyChoco([1, 2, 2], 3) == 0
    assert buyChocoOptimal([3, 2, 3], 3) == 3
    assert buyChocoOnePass([1, 2, 3, 4, 5], 10) == 7
    print("All test cases passed!")

"""
Time Complexity Analysis:
Sorting Solution:
- Time complexity: O(n log n) due to sorting.

Optimal Solution:
- Time complexity: O(n) - single pass through the array.

Space Complexity Analysis:
- Space complexity: O(1) for optimal solutions, O(n) for sorting solution if considering the space used by sort.

Topic: Arrays, Greedy, Sorting
"""
