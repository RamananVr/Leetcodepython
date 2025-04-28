"""
LeetCode Problem #1833: Maximum Ice Cream Bars

Problem Statement:
You have `n` ice cream bars, and you are given an array `costs` where `costs[i]` is the price of the `i-th` ice cream bar. 
You have `coins` coins to spend, and you want to maximize the number of ice cream bars you can buy.

Return the maximum number of ice cream bars you can buy with your coins. 
Note: You can buy the ice cream bars in any order.

Constraints:
- `costs.length == n`
- `1 <= n <= 10^5`
- `1 <= costs[i] <= 10^5`
- `1 <= coins <= 10^8`
"""

# Solution
def maxIceCream(costs, coins):
    """
    This function calculates the maximum number of ice cream bars that can be bought
    given the costs of the bars and the number of coins available.

    :param costs: List[int] - List of costs of ice cream bars
    :param coins: int - Number of coins available
    :return: int - Maximum number of ice cream bars that can be bought
    """
    # Sort the costs in ascending order
    costs.sort()
    
    # Initialize the count of ice cream bars bought
    count = 0
    
    # Iterate through the sorted costs
    for cost in costs:
        # If we can afford the current ice cream bar, buy it
        if coins >= cost:
            coins -= cost
            count += 1
        else:
            # If we can't afford the current ice cream bar, stop
            break
    
    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    costs = [1, 3, 2, 4, 1]
    coins = 7
    print(maxIceCream(costs, coins))  # Expected Output: 4

    # Test Case 2
    costs = [10, 6, 8, 7, 7, 8]
    coins = 5
    print(maxIceCream(costs, coins))  # Expected Output: 0

    # Test Case 3
    costs = [1, 6, 3, 1, 2, 5]
    coins = 20
    print(maxIceCream(costs, coins))  # Expected Output: 6

    # Test Case 4
    costs = [2, 2, 2, 2]
    coins = 8
    print(maxIceCream(costs, coins))  # Expected Output: 4

# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting the `costs` array takes O(n log n), where `n` is the length of the array.
- Iterating through the sorted array takes O(n).
- Overall time complexity: O(n log n).

Space Complexity:
- The sorting operation is performed in-place, so the space complexity is O(1) (excluding the input array).
- Overall space complexity: O(1).
"""

# Topic: Arrays